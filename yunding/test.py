import json
import time

from urllib import request, parse

import requests


def main():
    cookie = 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552ANCIsImlkIjoiNWRmYzZkMjE5NTRjNTk2NjU0ZDE0MWQ4IiwiaWF0IjoxNTc2OTkxMzQzLCJleHAiOjE1Nzk1ODMzNDN9.PX44aoZNLKn8zqbVkcVjcYao9nPR4tMSMECHMA8rghE'
    # 获取用户信息
    useGoodsToUser = request.Request('http://joucks.cn:3344/api/useGoodsToUser')
    useGoodsToUser.add_header('Cookie', cookie)
    # for i in range(1000,9999):
    buy_data = parse.urlencode({'ugid':'5dfc8bd278111f6f4cbb900b',
                            })
    count = 0
    while True:
        with request.urlopen(useGoodsToUser,data=buy_data.encode('utf-8')) as f:
            getUserGoodsRes = f.read().decode('utf-8')
            getUserGoodsJson = json.loads(getUserGoodsRes)
            if getUserGoodsJson['code'] == 200:
                count+=1
                print(count)
                time.sleep(0.3)

            # if getUserGoodsJson['code']==200:
            #     print('成功,密码是:'+str(i))
        # time.sleep(1)
    # userInfo = request.urlopen(getUserTask)
    # userInfoStr = userInfo.read().decode('utf-8')
    # userInfoJson = json.loads(userInfoStr)
    # user_active = userInfoJson['data']['user']['vitality_num']


if __name__ == '__main__':
    main()