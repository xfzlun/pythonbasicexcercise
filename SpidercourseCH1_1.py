# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-15;9:40
@author: aLuren

#@FileName: SpidercourseCH1_1.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
Python爬虫(入门+进阶）CH1-2 爬虫三步骤模板
'''

import urllib.request
import requests
#url1 = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv5530&productId=100000232304&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
url = 'https://www.baidu.com/'
'''
f = urllib.request.urlopen(url)
print(f.read(10))
print(f.read(10).decode('utf-8'))
'''
#1.分析网页后，获取header讯息，取得request位置后使用request模组，获取数据
r = requests.get(url)
print(r)
r.encoding = 'utf-8'
print(r.text)



