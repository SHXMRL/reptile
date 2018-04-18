# -*- coding: utf-8 -*-
from urllib import request
from chardet import detect
from bs4 import BeautifulSoup
import gzip
import os
#获取html代码
def get_html(url):
    r = request.urlopen(url)
    html=r.read()
    #检测压缩并解压
    if r.getheader('Content-Encoding'):
        html=gzip.decompress(html)
    #html解码
    return html.decode(detect(html)['encoding'],'ignore')
#获取书籍目录链接
def get_book(url):
    print(url,'aaa')
    html=get_html(url)
    bs=BeautifulSoup(html,'html.parser')
    book_name=bs.find('div',id='title').get_text().split(' ')[0]
    book_m_l=bs.find('div',id='TabCss').find_all('a')
    print(book_name)
    with open('./book/'+book_name+'.href','w',encoding='utf8') as f:
        for book_name in book_m_l:
            f.write(i+'/'+book_name['href']+'\n')
if __name__=='__main__':
    from threading import Thread
    from multiprocessing import pool
    #获取书籍列表页链接编号
    start_urls='https://www.bxwx9.org/modules/article/index.php?fullflag=1'
    html=get_html(start_urls)
    bs=BeautifulSoup(html,'html.parser')
    num=bs.find("a",class_='last').get_text()
    print('书籍总页数获取完成，总页数为%s'%(num,))
    #获取数据链接以及书籍编号
    def page_list(url,num):
        html=get_html(url)
        bs=BeautifulSoup(html,'html.parser')
        booklist=bs.find('div',id='centerm').find_all('table')[1].find_all('tr')[1:]
        with open('./book_log/'+num,'w',encoding='utf8') as f:
            for book_i in booklist:
                book_id=book_i.find('a')['href'].split('/')[-1].split('.')[0]
                book_c=book_i.find('a')['href'].split('/')[-2]
                f.write(book_c+'/'+book_id+'\n')
    
    for i in range(1,int(num)+1):
        #拼接列表页的链接地址
        url='https://www.bxwx9.org/modules/article/index.php?fullflag=1&page='+str(i)
        t=Thread(target=page_list,args=(url,str(i)))
        t.start()
    t.join()
    print('书籍列表加载完成。。。')
    #获取每一本书的章节url
    book_list=[x for x in os.listdir('./book_log') if os.path.isfile('./book_log/'+x)]
    p=pool.Pool(15)
    for i in book_list:
        with open('./book_log/'+i,'r',encoding='utf8') as f:
            r_list=f.readlines()
            for i in r_list:
                url='https://www.bxwx9.org/b/'+i.replace('\n','')+'/index.html'
                p.apply_async(get_book,args=(url,))
    p.close()
    p.join()
    print('书籍的目录加载已完成。。。')
    #保存书籍数据
    book_list=[x for x in os.listdir('./book') if os.path.isfile('./book/'+x)]
    for x in book_list:
        os.mkdir('./book/'+x.split('.')[0])
        with open('./book/'+x,'r',encoding='utf8') as f:
            url_list=f.readlines()
            for url in url_list:
                url='https://www.bxwx9.org/b/'+url
                html=get_html(url)
                bs=BeautifulSoup(html,'html.parser')
                title=bs.find('div',id='title').get_text()
                content=bs.find('div',id='content').get_text()
                with open('./book/'+x.split('.')[0]+'/'+title.replace(' ','_')+'.txt','w',encoding='utf8') as f1:
                    f1.write(content)        
    
