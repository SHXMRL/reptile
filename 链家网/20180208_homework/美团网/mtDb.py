#coding=utf-8
from pymysql import *
#args 元组：args[0]=name,args[1]=imgurl,args[2]=img_addr,args[3]=avgScore 
#添加表字段
def mysql0(*args):
        #连接数据库
        conn=connect(host='127.0.0.1',port=3306,user='root',passwd='9638',db='meituan',charset="utf8")
        #创建游标
        cursor=conn.cursor() 
        #执行sql
        query=cursor.execute("insert into mtw(mturl,title) values(%s,%s)",(args[1],args[0]))
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
#结果查询函数
#args 元组：
def selectmtw(*args):
        #连接数据库
        conn=connect(host='127.0.0.1',port=3306,user='root',passwd='9638',db='meituan',charset="utf8")
        #创建游标
        cursor=conn.cursor()
        #执行sql
        query=cursor.execute("select * from mtw where title=%s",(args[0]))
        result=cursor.fetchone()
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
        return result
#添加文章数据 args[0]=name,args[1]=imgurl,args[2]=img_addr,args[3]=avgScore
def addContent(*args):
        #连接数据库
        conn=connect(host='127.0.0.1',port=3306,user='root',passwd='9638',db='meituan',charset="utf8")
        #创建游标
        cursor=conn.cursor() 
        #执行sql
        query=cursor.execute("insert into mtw(title,mturl,imgs,avscore) values(%s,%s,%s,%s)",(args[0],args[1],args[2],args[3]))
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
#数据库所有数据查看       
##def sel(*args):
##        #连接数据库
##        conn=connect(host=args[0],port=3306,user=args[1],passwd=args[2],db=args[3],charset="utf8")
##        #创建游标
##        cursor=conn.cursor() 
##        #执行sql
##        result=cursor.execute("select title from mtw")
##        re=cursor.fetchall()
##        #提交执行
##        conn.commit()
##        #关闭游标
##        cursor.close()
##        #关闭连接
##        conn.close()
##        return re
   
