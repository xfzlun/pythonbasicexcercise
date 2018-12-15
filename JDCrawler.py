# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-15;15:03
@author: aLuren
#@FileName: JDCrawler.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
试着爬取ROGphone 35页评论
'''

import requests

for i in range(0, 36):
    url1 = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv5537&productId=100000232304&score=0&sortType=5&page='
    url2 = str(i)
    url3 = '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    finalurl = url1+url2+url3
    print(finalurl)