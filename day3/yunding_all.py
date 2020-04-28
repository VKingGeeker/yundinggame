# coding=utf-8
import time

from urllib import request, parse

import json

# 扫货专用


buyReq = request.Request('http://joucks.cn:3344/api/byPalyerGoods')
# buyReq.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
# buyReq.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
buyReq.add_header('Cookie',
                  'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiODcyNDY4OTMzQHFxLmNvbSIsImlkIjoiNWRmOWJiYzBlYmMxODkzZGIwYjQ2OGE4IiwiaWF0IjoxNTc3NDEyODUxLCJleHAiOjE1ODAwMDQ4NTF9.IWx7Ztzy_kTX71HBSaJSZ2N58EFM51w3SprwKQvIAr0')
toFilter = ["兰花","毛刺"]
x = 0
while True:
    y = 1
    while True:
        req = request.Request('http://joucks.cn:3344/api/getSellGoods?pageIndex=' + str(y) + '&tid=all')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('Cookie',
                       'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiODcyNDY4OTMzQHFxLmNvbSIsImlkIjoiNWRmOWJiYzBlYmMxODkzZGIwYjQ2OGE4IiwiaWF0IjoxNTc3NDEyODUxLCJleHAiOjE1ODAwMDQ4NTF9.IWx7Ztzy_kTX71HBSaJSZ2N58EFM51w3SprwKQvIAr0')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')

        with request.urlopen(req) as f:
            jsonStr = f.read().decode('utf-8')
            jsonObj = json.loads(jsonStr)
            usersSell = jsonObj['data']['playerSellUser']
            if len(usersSell) != 0:
                for ele in usersSell:
                    if ele['goods'] != None :
                        user = ele['user']['nickname']
                        id = ele['_id']
                        goods = ele['goods']['name']
                        price = ele['game_gold']
                        count = ele['count']
                        # print("user:" + user + "\t名称:" + goods + "\t价格" + str(price))
                        if price <= 2:
                            buy_data = parse.urlencode({'usgid': id})
                            with request.urlopen(buyReq, data=buy_data.encode('utf-8')) as g:
                                print("user:" + user + "\t名称:" + goods + "\t价格：" + str(price) +"\t 数量："+str(count))
                                time.sleep(0.5)
                y += 1
            else:
                break
    x += 1
    print("第" + str(x) + "次循环")
    if x % 50 == 0:
        time.sleep(5)
    else:
        time.sleep(1)
