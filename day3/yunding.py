# coding=utf-8
import time
import urllib
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request, parse
import requests
import json

# Post请求

req = request.Request('http://joucks.cn:3344/api/getSellGoods?pageIndex=1&tid=all')
# req.add_header('Accept', '*/*')
# req.add_header('Accept-Encoding', 'gzip, deflate')
# req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2')
# req.add_header('Connection', 'keep-alive')
# req.add_header('Content-Length', '30')
# req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
req.add_header('Cookie',
               'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552AIiwiaWQiOiI1ZGY5YmJjMGViYzE4OTNkYjBiNDY4YTgiLCJpYXQiOjE1NzY5OTAzMDUsImV4cCI6MTU3OTU4MjMwNX0.vzllL3JRzBNImcPUrZTqL9N5T72keYwlZKWF14PGe2c')
# req.add_header('Host', 'joucks.cn:3344')
# req.add_header('Origin', 'http://joucks.cn:3344')
# req.add_header('Referer', 'http://joucks.cn:3344')
# req.add_header('X-Requested-With', 'XMLHttpRequest')
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')

buyReq = request.Request('http://joucks.cn:3344/api/byPalyerGoods')
buyReq.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
buyReq.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
buyReq.add_header('Cookie',
                  'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552AIiwiaWQiOiI1ZGY5YmJjMGViYzE4OTNkYjBiNDY4YTgiLCJpYXQiOjE1NzY5OTAzMDUsImV4cCI6MTU3OTU4MjMwNX0.vzllL3JRzBNImcPUrZTqL9N5T72keYwlZKWF14PGe2c; io=GhYOBdeMCES02vgqAAFF; left-click=%23transaction')

x = 0
while True:
    with request.urlopen(req) as f:
        # print('Status:', f.status)
        # for k, v in f.getheaders():
        #     print('%s:%s' % (k, v))
        jsonStr = f.read().decode('utf-8')
        jsonObj = json.loads(jsonStr)
        if jsonObj['data'] == None:
            print("none")
            break
        usersSell = jsonObj['data']['playerSellUser']
        for ele in usersSell:
            user = ele['user']['nickname']
            id = ele['_id']
            goods = ele['goods']['name']
            price = ele['game_gold'] / ele['count']
            if '宠物升级丹' in goods:
                if price <= 13:
                    buy_data = parse.urlencode({'usgid': id})
                    with request.urlopen(buyReq, data=buy_data.encode('utf-8')) as g:
                        print("user:" + user + "\t名称:" + goods + "\t价格" + str(price))
    x += 1
    print("第" + str(x) + "次循环")
    if x%50 == 0:
        time.sleep(5)
    else:
        time.sleep(1)

