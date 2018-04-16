#coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
#导入数据库包
import tianyaDbs
#读文件
with open("tianyalt/tianya.txt","r+",encoding="utf8") as f:
        content=f.read()
#创建bs对象
bsObj=BeautifulSoup(content,"html.parser")

tyztUrl=bsObj.findAll("div",class_="nav_child_box")[0].li.a['href']

tyztTitle=bsObj.findAll("div",class_="nav_child_box")[0].li.a.string

print(tyztUrl,tyztTitle)
zjlsUrl=bsObj.find("div",class_="nav_child_box").findAll("ul")[1].findAll("li")[3].a['href']
zjlsTitle=bsObj.find("div",class_="nav_child_box").findAll("ul")[1].findAll("li")[3].a.string
#给数据库插入数据
user="root"
passwd="9638"
db="tianya"
host="localhost"
tianyaDbs.mysql0p('zjlsUrl','zjlsTitle','id','title','author','url','time')
#tianyaDb.databased(zjlsUrl,zjlsTitle,host,user,passwd,db)
