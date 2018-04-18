from urllib import request, error
from bs4 import BeautifulSoup
import os
import json
#import mtDb

##user="root"
##passwd="9638"
##db="meituan"
##host="localhost"
##title="美团"
for p in range(52):
    url = "https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=4ED25D0BBBE6917E2BA742ECAA9C935F5B0C7C027F820845964385A0E3D6C777%401517821331737&cityId=42&offset=" + str(p * 20) + "&limit=20&startDay=20180205&endDay=20180205&q=&sort=defaults"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host': 'ihotel.meituan.com',
        'Origin': 'http://hotel.meituan.com',
        'Referer': 'http://hotel.meituan.com/xian/'
    }
    # 打开请求地址
    re = request.Request(url, headers=headers)
    req = request.urlopen(re, timeout=10)
    # 获取页面信息
    content = req.read().decode("utf8")
    # 将str类型转成字典类型
    content = json.loads(content)
    with open("mtjd/mt.txt", "w", encoding="utf8") as f:
        f.write(str(content))
    # 遍历得到poiid
    for hotel in content['data']['searchresult']:
        page_id = hotel['poiid']
        name = hotel['name']
        try:
            os.mkdir('F:\Reptile\Exicise\photo\\' + name)
        except:
            pass

#############################################酒店详情##################################################
        # 酒店图片地址采集
        page_url = 'https://ihotel.meituan.com/group/v1/poi/' + str(
            page_id) + '/imgs?utm_medium=touch&version_name=999.9&classified=true'
        # print(page_url)
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        #     'Host': 'ihotel.meituan.com',
        #     'Origin': 'http://hotel.meituan.com',
        #     'Referer': 'http://hotel.meituan.com/1537104/?ci=2018-03-11&co=2018-03-12'
        # }
        # 打开请求地址
        re1 = request.Request(page_url, headers=headers)
        req = request.urlopen(re1, timeout=10)
        # 获取页面信息
        content = req.read().decode("utf8")
        # 将str类型转成字典类型
        content = json.loads(content)
        # print(content)
        with open("mtjd/mting.txt", "w", encoding="utf8") as f:
            f.write(str(content))
        try:
            img_list = (content['data'])[2]
            a = img_list.get('imgs')
            try:
                b = (a[4:5])[0]
            except IndexError as e:
                print('继续执行')
            if b:
                print(b)
                d = b.get('urls')
                for i in d:
                    image = i.replace('w.h', '200.0.0')
                    print(image)
                    end = image.split('.')[-1]
                    img_addr = 'F:/Reptile/Exicise/photo/'+name+'/'+name+'.'+end
                    request.urlretrieve(image, img_addr)
            else:
                continue
        except (KeyError,IndexError) as e:
            print('下载出错')
            
                    
        

