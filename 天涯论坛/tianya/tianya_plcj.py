#coding=utf-8
#采集天涯杂谈下的所有帖子并存入数据库
from urllib import request
from bs4 import BeautifulSoup
import tianyaDbs
import sys
user="root"
passwd="9638"
db="tianya"
host="localhost"
title="天涯杂谈"
#版块id，可以从数据库中获取

with open("tianyalt/tianya.txt","r+",encoding="utf8") as f:
        content=f.read()
bsObj=BeautifulSoup(content,"html.parser")
for i in range(1,8):
        aTable=bsObj.find("table",class_="tab-bbs-list tab-bbs-list-2").findAll("tbody")[i].findAll("tr")

        for tr in aTable:
                #帖子链接
                aHref=tr.a['href']
                #这里使用getText(),并且将标题的空格去掉
                #帖子标题
                
                aTitle=tr.a.getText().strip()
                result=tianyaDbs.sel('localhost','root','9638','tianya')
                aTitle=(aTitle,)
                
                if  aTitle not in result:
                        #帖子作者
                        author=tr.find("a",class_="author").string
                        print(aHref,aTitle,author)
                        #采集帖子下的主贴内容
                        #帖子url地址
                        aUrl="http://bbs.tianya.cn"+aHref
                        #打开地址并读入
                        req=request.urlopen(aUrl).read().decode("utf8")
                        #创建bs4对象
                        absObj=BeautifulSoup(req,"html.parser")
                        #发帖时间
##                        aTime=absObj.find("div",class_="atl-menu clearfix js-bbs-act").findAll("div")[1].findAll("span")[1].string
##                        #帖子内容
##                        aContent=absObj.find("div",class_="bbs-content clearfix").getText().strip()
####                        print(aTime)
####                        print(aContent)
##                        tianyaDbs.addArticle(host,user,passwd,db,aTitle,aUrl,aContent,author,aTime)
                        try:
                                aTime=absObj.find("div",class_="atl-menu clearfix js-bbs-act").findAll("div")[1].findAll("span")[1].string
                                aContent=absObj.find("div",class_="bbs-content clearfix").getText().strip()
##                              print(aTime)
##                              print(aContent)
                                tianyaDbs.addArticle(host,user,passwd,db,aTitle,aUrl,aContent,author,aTime)

                        except AttributeError:
                                print("'NoneType' object has no attribute 'findAll'")










                                
                                
                                
                                
                                
               
                        
                
        
