#采集论坛帖子并存入数据库
from urllib import request
from bs4 import BeautifulSoup
import husDb
import sys
#数据库用户名,密码,数据库名,主机,标题
user='root'
passwd='9638'
db='tianya'
host='localhost'
#
title='华商论坛'
#打开已经获取的网页内容,并读入
with open ('huslt/hus.txt','r+',encoding='utf8') as f:
    content=f.read()
#创建BeautifulSoup对象
bs_1=BeautifulSoup(content,'html.parser')
#循环去取标签名相同内容不同的标签,用索引处理
for i in range(3,63):
    #获取bs对象下,我们要采集的内容(找节点)
    Htable=bs_1.find('div',class_='z threadCommon').findAll('tr')[i].findAll('td')
    #print(Htable)
    #遍历出所有的tr标签下的a标签
    try:
        for td in Htable:
            #获取帖子链接
            Hhref=td.a['href']
            #获取帖子标题(getText().strip()去掉标题的空格)
            Htitle=td.a.getText().strip()
            #print(Hhref)
            #数据去重准备
            dbqc=husDb.sel('localhost','root','9638','hus')
            Htitle=(Htitle,)
            #如果查询数据库中帖子不存在,再添加,反之跳过该帖
            if Htitle not in dbqc:
                #发帖作者
                author=td.find('a').string
                #主帖内容
                #帖子url地址
                
                Hurl='http://bbs.hsw.cn/'+Hhref
                
                #打开Hurl地址并读入
                headers={
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
                        'Host':'bbs.hsw.cn'
                        }
                re=request.Request(Hurl,headers=headers)
                res=request.urlopen(re)
                coont=res.read().decode('utf8')
                #创建bs4对象
                bs_2=BeautifulSoup(coont,'html.parser')
                #zip
            
                Htime=bs_2.find('div',class_='tipTop s6').findAll('span')[1].string
                #帖子内容
                Hcontent=bs_2.find('div',class_='tpc_content').getText().strip()
                print(Hurl,Htitle,1,author,2,Htime)
                husDb.addArticle(host,user,passwd,db,Htitle,Hurl,Hcontent,author,Htime)
    except AttributeError or TypeError:
        print("'NoneType' object has no attribute 'findAll'")
        print("'NoneType' object is not subscriptable")


























