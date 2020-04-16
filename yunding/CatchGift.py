# -*- coding: UTF-8 -*-

import requests
import time
import random
import os
import json


def starts(url, params, cookie):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': 'joucks.cn:3344',
        'Origin': 'http://joucks.cn:3344',
        'Referer': 'http://joucks.cn:3344/',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        resp = requests.post(url, headers=headers, data=params, timeout=15)
        return json.loads(resp.text)
    except Exception as e:
        return e


dir = os.path.dirname(os.path.abspath(__file__))
f = open(dir+'/key.txt', 'r')
cbmids = f.read().splitlines()
cookies = [
    'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiODcyNDY4OTMzQHFxLmNvbSIsImlkIjoiNWRmOWJiYzBlYmMxODkzZGIwYjQ2OGE4IiwiaWF0IjoxNTc3NDEyODUxLCJleHAiOjE1ODAwMDQ4NTF9.IWx7Ztzy_kTX71HBSaJSZ2N58EFM51w3SprwKQvIAr0',  # 用户1
    'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552AMSIsImlkIjoiNWRmYzY2NmM3MmEyZmY1ODI5YWMyNWJiIiwiaWF0IjoxNTc2OTkxMTU3LCJleHAiOjE1Nzk1ODMxNTd9.95PcwSdQ-kOBrjC8A40aMsX7LYabCfBLctUw-W14RNQ',  # 用户2
    'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552ANiIsImlkIjoiNWUxNDBjYzRlMjhlZjE2MGYzMzY0ODJmIiwiaXAiOiIyMDIuMTg5LjEuMTgiLCJpYXQiOjE1NzgzNzIyOTIsImV4cCI6MTU4MDk2NDI5Mn0.AwIQLPqRUBrcox8CafKiY_6g8qM2xf6X1ds9GotpYYI',  # 用户3
]

# 读取key

for cbmid in cbmids:
    times = random.randint(0, 1)
    url = 'http://joucks.cn:3344/api/exchangeVolume'
    params = {
        'volume': cbmid
    }
    if len(cookies) < 1:
        print("未配置cookie或任务已执行完毕")
        exit()
    for cookie in cookies:
        res = starts(url, params, cookie)
        if not isinstance(res, dict):
            print(res)
            exit()
        if res['code'] == 200 or res['code'] == 401:
            cookies.remove(cookie)
        print(res['msg'])
    time.sleep(times)
    print('-----------等待%d秒-------' % (times))