from urllib import request,error
from bs4 import BeautifulSoup
import json,os
import web_lianjia
import ljDb
#读取页面内容
with open('lj/lianjia.txt','r+',encoding='utf8') as f:
    content=f.read()
content=json.loads(content)
###print(len(content))
for i in content:
    res_bs=BeautifulSoup(i,'html.parser')
    #print(res_bs)
    #获取li下的所有内容
    body_li=res_bs.find('ul',class_='resblock-list-wrapper').findAll('li')
    #print(body_li)
    #对li下的所有内容进行遍历
    for li in body_li:
        #获取li下div属性为'resblock-desc-wrapper'的内容
        li_a=li.find('div',class_='resblock-desc-wrapper')
        li_a1=li.find('a',class_='resblock-img-wrapper')
        #获取住宅名
        name=li_a.a.string
        hrefs=li_a.a['href']
        #获取图片链接
        img_src=li_a1.img['data-original']
        #print(img_src)
        #获取户型
        room=li_a.find('a',class_='resblock-room').get_text().replace('\n','')
        #获取建筑面积
        mianji=li_a.find('div',class_='resblock-area').get_text().replace('\n','')
        #获取价格
        price=li_a.find('div',class_='resblock-price').find('div',class_='main-price').get_text().replace('\n','')
        #price_sum=li_a.find('div',class_='resblock-price').find('div',class_='second').get_text().replace('\n','')
        ljDb.addContent(name,img_src,room,mianji,price)
        #获取图片
        try:
            os.mkdir('lj/'+ name)
        except:
            pass
        #采集图片
        end=img_src.split('.')[-1]
        #图片文件名拼接
        img_addr='lj/'+name+'/'+name+'.'+end
        try:
            if not img_src:
                request.urlretrieve(img_src,img_addr)
        except error.HTTPError as e:
            print(e.reason)

##        print(name,img_src,room,mianji,price)
##












        






                 
