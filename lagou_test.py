#coding=utf-8
#使用request模块模拟浏览器请求拉勾网页面
from urllib import request,parse
url = r'http://search.jd.com/shop_new.php?ids=157646%2C195491'
headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Referer': r'http://search.jd.com/Search?keyword=%E9%95%BF%E6%AC%BE%E7%BE%BD%E7%BB%92%E6%9C%8D%E7%94%B7&enc=utf-8&wq=%E9%95%BF%E6%AC%BE%E7%BE%BD%E7%BB%92%E6%9C%8D%E7%94%B7&pvid=e228b7df0b12497e837bcc79ee4edbf8',
        'Connection': 'close',
        'Host':'search.jd.com',
        'Origin':'https://search.jd.com'
        }
data={}
data['first']="true"
data['pn']=1
data['kd']="python"
#使用urllib.parse将data 进行格式化
data = parse.urlencode(data).encode('utf8')
#使用Request()定义请求地址的头信息和请求地址
req = request.Request(url=url, headers=headers,method="POST",data=data)
#将Request()实例加载到urlopen()中并进行采集
page = request.urlopen(req).read()
#设定下载内容的编码为utf-8
page = page.decode('utf-8')
with open("test/jd.txt","w",encoding="utf8") as f:
        f.write(page)
