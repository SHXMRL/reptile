from urllib import request
import json
import re
#所有的类都继承自'object'
class BaiduImg(object):
    def __init__(self):
        #完全继承'BaiduImg'类(超类/父类/基类)
        super(BaiduImg,self).__init__()
        print('图片采集中......')
        self.page = 30
        #访问请求
    def request(self):
        #查找每页图片规律(页数)
        #第一页
        while self.page<=120:
            #请求地址
            request_url=r'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8+%E5%8A%A8%E7%89%A9+%E8%80%81%E8%99%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E5%A3%81%E7%BA%B8+%E5%8A%A8%E7%89%A9+%E8%80%81%E8%99%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=&fr=&cg=wallpaper&pn=30&rn=30&gsm=1e&1517409840586='
            #请求头部信息
            headers={
                        'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
                        'Content-type': 'text/html',
                        'Referer':'http://image.baidu.com/search/index?ct=201326592&z=&tn=baiduimage&ipn=r&word=%E5%A3%81%E7%BA%B8%20%E5%8A%A8%E7%89%A9%20%E8%80%81%E8%99%8E&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=1517409648657_R&ic=0&se=&sme=&width=&height=&face=0',
                        'Host':'image.baidu.com'
                }
            
            req=request.Request(request_url,headers=headers)
            
            with request.urlopen(req) as f:
                #按状态进行判断
                #如果请求成功
                if f.status==200:
                    #读取内容,并转成字符串格式
                    content=f.read().decode('utf-8')
                    #将json格式转为字典格式
                    dict1=json.loads(content)
                    #dict1[]
                    self.download(dict1['data'])
                    
            self.page+=30
    #使用urllib标准方法保存图片,注意文件保存类型
    def download(self,data):
        for img in data:
            #字典的get()方法
            #判断文件类型
            if img.get('middleURL'):
                url=img['middleURL']
            elif img.get('thumbURL'):
                url=img['thumbURL']
            #文件为空
            else:
                url=''
            if url:
                data=request.urlopen(url).read()
                #文件名
                imgName=strip(img['fromPageTitleEnc'])
                #文件存放地址及文件名字符串拼接
                FileName=str('imgs7/')+imgName+str('.jpg')
                with open(FileName,'wb') as f:
                    f.write(data)
                    
##    def download2(self,data):
##                for image in data:
##                        if image.get('middleURL'):
##                                url = image['middleURL']
##                        elif image.get('thumbURL'):
##                                url = image['thumbURL']
##                        else:
##                                url=""
##                        if url:
##                                imageName=strip(image['fromPageTitleEnc'])
##                                filePath = str('images/')+imageName+str('.jpg')
##                                request.urlretrieve(url,filePath)
#过滤函数
def strip(path):
    path=re.sub(r'[? \\*| "<>:/!?]','',str(path))
    return path
if __name__=='__main__':
    bi=BaiduImg()
    bi.request()
                


















            
            
