import requests
import time
import random


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiODcyNDY4OTMzQHFxLmNvbSIsImlkIjoiNWRmOWJiYzBlYmMxODkzZGIwYjQ2OGE4IiwiaWF0IjoxNTc3NDEyODUxLCJleHAiOjE1ODAwMDQ4NTF9.IWx7Ztzy_kTX71HBSaJSZ2N58EFM51w3SprwKQvIAr0',
    'Host': 'joucks.cn:3344',
    'Origin': 'http://joucks.cn:3344',
    'Referer': 'http://joucks.cn:3344/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url = 'http://joucks.cn:3344/api/makeGoods'  # 合成
params = {
    'sell_json': '[{"id":"5dfc79047dc8ed1267cfbe50","count":"1","name":"残魂碎片六","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"},{"id":"5dfc35637dc8ed1267cf7fab","count":"1","name":"残魂碎片七","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"},{"id":"5df9ca0394ab8c4e3cfd268d","count":"1","name":"残魂碎片五","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"},{"id":"5df9c92994ab8c4e3cfd22bb","count":"1","name":"残魂碎片四","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"},{"id":"5df9bc3aebc1893db0b4694c","count":"1","name":"残魂碎片三","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"},{"id":"5df9bcdfb21e193dc6022b23","count":"1","name":"残魂碎片二","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"},{"id":"5df9bcf95d17b33db592d810","count":"1","name":"残魂碎片一","style":"text-shadow:1px+1px+px+dimgray;color:dimgray;background-color:beige;"}]',
    'sell_type': 'make',
}
joucks = requests.Session()
while True:
    timeout = 1
    try:
        resp = joucks.post(url, data=params, headers=headers, timeout=timeout)
        print(resp.text)
        print("暂停 %d  秒" % (timeout))
        time.sleep(timeout)
    except Exception as e:
        print(e)
