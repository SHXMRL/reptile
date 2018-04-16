from urllib import request,error
from bs4 import BeautifulSoup
import os
import json
import mtDb

user="root"
passwd="9638"
db="meituan"
host="localhost"
title="美团"
for p in range(52):
        url="https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=4ED25D0BBBE6917E2BA742ECAA9C935F5B0C7C027F820845964385A0E3D6C777%401517821331737&cityId=42&offset="+str(p*20)+"&limit=20&startDay=20180205&endDay=20180205&q=&sort=defaults"
        headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
                    'Host':'ihotel.meituan.com',
                    'Origin':'http://hotel.meituan.com',
                    'Referer':'http://hotel.meituan.com/xian/'
        }

        #打开请求地址
        re=request.Request(url,headers=headers)
        req=request.urlopen(re)
        #获取页面信息
        content=req.read().decode("utf8")
        #将str类型转成字典类型
        content=json.loads(content)
        with open("mtjd/mt.txt","w",encoding="utf8") as f:
                f.write(str(content))
        #遍历得到酒店名和评分
        for hotel in content['data']['searchresult']:
                name=hotel['name']
                avgScore=hotel['avgScore']
        
                try:
                        os.mkdir('F:\Reptile\Exicise\meituanw\meituan\\'+name)
                except:
                        pass
                #采集图片
                end=hotel['frontImg'].split('.')[-1]
                #图片名拼接
                img_addr='F:\Reptile\Exicise\meituanw\meituan\\'+name+'/'+name+'.'+end
                #print(name,p,avgScore)
                try:
                        imgurl='https://p1.meituan.net/320.0/'+hotel['frontImg'].split('/')[-2]+'/'+hotel['frontImg'].split('/')[-1]
                        print(imgurl)
                        request.urlretrieve(imgurl,img_addr)
                        mtDb.addContent(name,imgurl,img_addr,avgScore)
                except error.HTTPError as e:
                        print(e.reason)
                try:
                        imgurl='https://p0.meituan.net/320.0/'+hotel['frontImg'].split('/')[-2]+'/'+hotel['frontImg'].split('/')[-1]
                        print(imgurl)
                        request.urlretrieve(imgurl,img_addr)
                        mtDb.addContent(name,imgurl,img_addr,avgScore)
                except error.HTTPError as e:
                        print(e.reason)        
               






















                        





                
