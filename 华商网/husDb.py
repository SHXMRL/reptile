#coding=utf-8
from pymysql import *
#args 元组：0=url，1=title,2=host,3=user,4=passwd,5=db       
#添加表字段
def mysql0p(*args):
        #连接数据库
        conn=connect(host='127.0.0.1',port=3306,user='root',passwd='9638',db='hus',charset="utf8")
        #创建游标
        cursor=conn.cursor() 
        #执行sql
        query=cursor.execute("insert into huslt(url,title) values(%s,%s)",(args[5],args[4]))
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
#结果查询函数
#args 元组：0=host,1=user,2=passwd,3=db,4=title
def selectForum(*args):
        #连接数据库
        conn=connect(host='127.0.0.1',port=3306,user='root',passwd='9638',db='hus',charset="utf8")
        #创建游标
        cursor=conn.cursor()
        #执行sql
        query=cursor.execute("select * from huslt where title=%s",(args[4]))
        result=cursor.fetchone()
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
        return result
#添加文章数据
def addArticle(*args):
        #连接数据库
        conn=connect(host='127.0.0.1',port=3306,user='root',passwd='9638',db='hus',charset="utf8")
        #创建游标
        cursor=conn.cursor() 
        #执行sql
        query=cursor.execute("insert into hslt(title,url,author,time) values(%s,%s,%s,%s)",(args[4],args[5],args[7],args[8]))
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
       
def sel(*args):
        #连接数据库
        conn=connect(host=args[0],port=3306,user=args[1],passwd=args[2],db=args[3],charset="utf8")
        #创建游标
        cursor=conn.cursor() 
        #执行sql
        result=cursor.execute("select title from hslt")
        re=cursor.fetchall()
        #提交执行
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
        return re
   
