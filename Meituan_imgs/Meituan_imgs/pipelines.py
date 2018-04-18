# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import re
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import pymysql
user='root'
password='9638'
name='meituan'
host='localhost'
port=3306

class MeituanPipeline(object):
    def __init__(self):

        self.conn=pymysql.connect(user=user,password=password,db=name,host=host,port=3306,charset='utf8')
        self.cursor=self.conn.cursor()
        #清空表中数据
##        self.cursor.execute('truncate mt;')
##        self.conn.commit()
    def process_item(self, item, spider):

        self.cursor.execute("""INSERT INTO mt (Title,Addr,Av_score,Levels,Telephone,Price,Common,Message,Introduce,Url)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (
            item['title'],
            item['addr'],
            item['av_score'],
            item['level'],
            item['telephone'],
            item['price'],
            item['common'],
            item['message'],
            item['introduce'],
            item['url'],
            )
        )
        self.conn.commit()
        return item

#数据存入Mongodb
class MongoDBPipeline(object):
    def process_item(self, item, spider):
        client = MongoClient('mongodb://localhost:27017/')
        # 获取数据库
        db = client.meituan
        data = {
            'Title':item['title'],
            'Addr':item['addr'],
            'Av_score':item['av_score'],
            'Level':item['level'],
            'Telephone':item['telephone'],
            'Price':item['price'],
            'Common':item['common'],
            'Message':item['message'],
            'Introduce':item['introduce'],
            'Url':item['url'],
            }
        # 获取集合
        collection = db.MeiTuan_collection.insert_one(data)
        return item
#采集图片
class MeituanImgPipeline(ImagesPipeline):
    default_headers={

         'Host':'ihotel.meituan.com',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
         #'Referer': 'http://hotel.meituan.com/162850135/'
        }

    # 设置图片保存目录
    def file_path(self, request, response=None, info=None):
        """
        :param request: 每一个图片下载管道请求
        :param response:
        :param info:
        :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
        :return: 每套图的分类目录
        """
        item = request.meta['item']
        folder = item['title']
        # 处理图片目录里的非法字符
        #folder_strip=strip(folder)
        # 通过图片url地址获取图片文件名
        image_guid=request.url.split('/')[-1]
        # 拼接图片路径
        filename = 'full/{0}/{1}'.format(folder,image_guid)
        # filename = 'full/%s/%s'%(folder_strip, image_guid)
        return filename

    def get_media_requests(self,item,info):
        if 'img_url' in item:
            for imageurl in item['img_url']:
                referer=item['hotel_url']
                yield scrapy.Request(url=imageurl,
                                     headers=self.default_headers,
                                     meta={'item': item,'referer':referer})
    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        print(results)
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths']=image_paths
        return item

    def strip(path):
        path = re.sub(r'[？\\*|“<>:/]', '', str(path))
        return path
    
