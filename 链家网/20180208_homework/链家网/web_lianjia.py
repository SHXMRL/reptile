#coding=utf-8
from urllib import request
import json
a=[]
for page in range(1,4):
    request_url=r"https://xa.fang.lianjia.com/loupan/pg"+str(page)+"/"

    headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
                'Host':'xa.fang.lianjia.com'
            }
    re=request.Request(request_url,headers=headers)
    req=request.urlopen(re)
    #print(req)
    content=req.read().decode("utf8")
    #print(content)
    a.append(content)
with open("lj/lianjia.txt","w",encoding="utf8") as f:
    json.dump(a,f)
