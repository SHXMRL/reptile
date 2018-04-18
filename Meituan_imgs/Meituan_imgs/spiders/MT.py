# -*- coding: utf-8 -*-
import scrapy
from Meituan_imgs.items import MeituanImgsItem
import re
import json

class MtSpider(scrapy.Spider):
    default_headers={
        'Referer': 'http://hotel.meituan.com/4366603/?ci=2018-03-12&co=2018-03-13',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
        'Host': 'hotel.meituan.com',

    }
    name = 'MT'

    allowed_domains = ['hotel.meituan.com']
    start_urls=['https://hotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=630812E79F35B5213D19E3D7B4DF0ACBC4A35B453FEE9D7FBABFB9C76FBA5E58%401520505672281&cityId=42&offset='+str(p*20)+'&limit=20&startDay=20180308&endDay=20180308&q=&sort=defaults' for p in range(51)]
    def parse(self, response):
        data_list = json.loads(response.body)['data']
        hotel_list=data_list['searchresult']
        for x in range(20):
            try:
                item = MeituanImgsItem()
                #酒店名
                item['title'] = hotel_list[x].get('name')
                #酒店地址
                item['addr'] = hotel_list[x].get('addr')
                #酒店评分
                item['av_score']=hotel_list[x].get('scoreIntro')
                #酒店档次
                item['level']=hotel_list[x].get('poiRecommendTag')
                #价格
                pc=hotel_list[x].get('priceExtInfo')
                if pc:
                    item['price']=pc
                else:
                    item['price'] = ''
                #评论条数
                item['common'] = hotel_list[x].get('commentsCountDesc')
                #详情页面地址
                page_id=hotel_list[x].get('poiid')
                pages1='http://hotel.meituan.com/'+str(page_id)+'/?ci=2018-03-12&co=2018-03-13'
                item['hotel_url']=pages1

                #ajax请求地址
                pages='https://ihotel.meituan.com/group/v1/poi/'+str(page_id)+'/imgs?utm_medium=touch&version_name=999.9&classified=true'
                item['page_url']= pages

            except Exception as e:
                print('数据出现为空')
            yield scrapy.Request(url=item['hotel_url'],meta={'item':item},headers=self.default_headers,callback=self.parse_detail,dont_filter=True)

    def parse_detail(self,response):
##        print(response)
        item = response.meta['item']
        #联系方式
        item['telephone']=response.css('div.poi-hotelinfo-content').xpath('div[1]/dd/span').xpath('string(.)').extract()[0]
        #酒店信息
        item['message']=response.css('div.poi-hotelinfo-content').xpath('div[2]/dd/span').xpath('string(.)').extract()[0]
        #酒店简介
        jieshao=response.css('div.poi-hotelinfo-content').xpath('div[3]/dd/span').xpath('string(.)').extract()[0].replace('/n',' ')
        item['introduce']=str(jieshao)
        yield scrapy.Request(url=item['page_url'], meta={'item': item}, callback=self.parse_imgs, dont_filter=True)

    def parse_imgs(self,response):
##        print(response.url)
##        print(313132135165135132131321321231321231)
        
        item = response.meta['item']
        ref_url=response.url
        url1=ref_url.split('/')[-2]
        url2= 'http://hotel.meituan.com/'+str(url1)+'/'+'?ci=2018-03-12&co=2018-03-13'
        item['url'] = url2
        img_paths=[]
        # 图片地址
        try:
            img_list = json.loads(response.body)['data'][2]
            a = img_list.get('imgs')
            b = (a[4:5])[0]

            d = b.get('urls')
            for i in d:
                image=i.replace('w.h','200.0.0')
                img_paths.append(image)
                item['img_url']=img_paths
        except (IndexError,KeyError) as e:
            print('图片未获取到',e)
        yield item


