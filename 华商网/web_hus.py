#coding=utf-8
from urllib import request
request_url=r"http://bbs.hsw.cn/thread-htm-fid-5.html"
headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
            'Host':'bbs.hsw.cn'
        }
re=request.Request(request_url,headers=headers)
req=request.urlopen(re)
print(req)
content=req.read().decode("utf8")
print(content)
with open("huslt/hus.txt","w",encoding="utf8") as f:
        f.write(str(content))
