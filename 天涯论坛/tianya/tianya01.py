#coding=utf-8
from urllib import request
req=request.urlopen("http://bbs.tianya.cn/list-666-1.shtml")
content=req.read().decode("utf8")
with open("tianyalt/tianya.txt","w",encoding="utf8") as f:
        f.write(str(content))
