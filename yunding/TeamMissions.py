import json
import random
from urllib import request, parse
import time

cookies = [
    # 用户1
    # 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiODcyNDY4OTMzQHFxLmNvbSIsImlkIjoiNWRmOWJiYzBlYmMxODkzZGIwYjQ2OGE4IiwiaWF0IjoxNTc3NDEyODUxLCJleHAiOjE1ODAwMDQ4NTF9.IWx7Ztzy_kTX71HBSaJSZ2N58EFM51w3SprwKQvIAr0',
    # # 用户2
    # 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552AMSIsImlkIjoiNWRmYzY2NmM3MmEyZmY1ODI5YWMyNWJiIiwiaWF0IjoxNTc2OTkxMTU3LCJleHAiOjE1Nzk1ODMxNTd9.95PcwSdQ-kOBrjC8A40aMsX7LYabCfBLctUw-W14RNQ',
    # # 用户3
    # 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552AMiIsImlkIjoiNWRmYzY3MGNmOGEyZTU1ODE2ZTQ2NDY4IiwiaWF0IjoxNTc2OTkxMjYzLCJleHAiOjE1Nzk1ODMyNjN9.cp4svEc3v6qeO3j1vSzvCVsjbT-lw1vJfS0s_-nBAmI',
    # # 用户4
    # 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552AMyIsImlkIjoiNWRmYzY5MWRmOGEyZTU1ODE2ZTQ2NjJmIiwiaWF0IjoxNTc2OTkxMzEyLCJleHAiOjE1Nzk1ODMzMTJ9.CJFsUOy_x50oJnMaOkoYIwVIGTix05GRiiQL3xsqHNg',
    # # 用户5
    # 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552ANCIsImlkIjoiNWRmYzZkMjE5NTRjNTk2NjU0ZDE0MWQ4IiwiaWF0IjoxNTc2OTkxMzQzLCJleHAiOjE1Nzk1ODMzNDN9.PX44aoZNLKn8zqbVkcVjcYao9nPR4tMSMECHMA8rghE',
    # 用户6
    'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoi5rS7552ANkBxcS5jb20iLCJpZCI6IjVlMTQwY2M0ZTI4ZWYxNjBmMzM2NDgyZiIsImxhc3RfaXAiOiIyMDIuMTg5LjEuMTgiLCJpYXQiOjE1Nzk0OTQwMTUsImV4cCI6MTU4MjA4NjAxNX0.NnVAit3DRn17yB9sBf5mpSQLjcY4vNN2rPAdhoP5MH8',
    # 布布
    # 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiODI0OTMxMTVAcXEuY29tIiwiaWQiOiI1ZGZlZWZmOGRkNzU4ZTU0MmFlNzc0ZTMiLCJsYXN0X2lwIjoiMjcuMTcuMzQuMjM0IiwiaWF0IjoxNTc3NjkzNDk1LCJleHAiOjE1ODAyODU0OTV9.2Rv8Ze1ObAnrtGoskr-1EHe6lgxpHPe0-o8F-1CWzbg',
]


def do_fation_task():
    userNo = 1
    for cookie in cookies:
        game_gold = 0
        game_silver = 0
        game_copper = 0
        repair_num = 0
        count = 0
        active = 0
        payForActive = 0

        try:
            # 获取帮派任务
            getFationTask = request.Request('http://joucks.cn:3344/api/getFationTask')
            getFationTask.add_header('Cookie', cookie)
            # 获取用户任务列表
            getUserTask = request.Request('http://joucks.cn:3344/api/getUserTask')
            getUserTask.add_header('Cookie', cookie)
            # 交付用户任务
            payUserTask = request.Request('http://joucks.cn:3344/api/payUserTask')
            payUserTask.add_header('Cookie', cookie)
            # 放弃任务
            closeUserTask = request.Request('http://joucks.cn:3344/api/closeUserTask')
            closeUserTask.add_header('Cookie', cookie)
            # 商城买东西
            byGoodsToMyUser = request.Request('http://joucks.cn:3344/api/byGoodsToMyUser')
            byGoodsToMyUser.add_header('Cookie', cookie)
            # 获取任务背包列表
            getUserGoods = request.Request('http://joucks.cn:3344/api/getUserGoods?tid=all&page=1')
            getUserGoods.add_header('Cookie', cookie)
            # 使用背包东西
            useGoodsToUser = request.Request('http://joucks.cn:3344/api/useGoodsToUser')
            useGoodsToUser.add_header('Cookie', cookie)
            # 获取用户信息
            getUserInfo = request.Request('http://joucks.cn:3344/api/getUserInfo')
            getUserInfo.add_header('Cookie', cookie)
            userInfo = request.urlopen(getUserInfo)
            userInfoStr = userInfo.read().decode('utf-8')
            userInfoJson = json.loads(userInfoStr)
            user_active = userInfoJson['data']['user']['vitality_num']
            unFinish = True
            while unFinish:
                if user_active < 100:
                    buy_data = parse.urlencode({'gid': '5df6ee69f6ffda1f2ccc4739'})
                    request.urlopen(byGoodsToMyUser, data=buy_data.encode('utf-8'))
                    with request.urlopen(getUserGoods) as i:
                        getUserGoodsRes = i.read().decode('utf-8')
                        getUserGoodsJson = json.loads(getUserGoodsRes)
                        userGoodsList = getUserGoodsJson['data']
                        if len(userGoodsList) != 0:
                            for ele1 in userGoodsList:
                                if ele1['goods']['name'] == "500活力丹":
                                    use_data = parse.urlencode({'ugid': ele1['_id']})
                                    request.urlopen(useGoodsToUser,
                                                    data=use_data.encode('utf-8'))
                                    payForActive += 5000
                                    user_active += 500
                                    print("用户" + str(userNo) + "：使用了500活力丹")
                                    break

                with request.urlopen(getUserTask) as f:
                    jsonStr = f.read().decode('utf-8')
                    jsonObj = json.loads(jsonStr)
                    userTask = jsonObj['data']
                    if len(userTask) != 0:
                        for ele in userTask:
                            id = ele['utid']
                            if ele['task']['task_type'] == 4:
                                if ele['task']['name'] == "武器库储备":
                                    id = ele['utid']
                                    pay_data = parse.urlencode({'utid': id})
                                    with request.urlopen(payUserTask, data=pay_data.encode('utf-8')) as g:
                                        payTaskRep = g.read().decode('utf-8')
                                        payTaskJson = json.loads(payTaskRep)
                                        if payTaskJson['code'] == 200:
                                            count += 1
                                            print("用户" + str(userNo) + "：任务提交成功,当前成功:" + str(count) + "次")
                                            repair_num += payTaskJson['data']['repair_num']
                                            game_gold += payTaskJson['data']['game_gold']
                                            game_silver += payTaskJson['data']['game_silver']
                                            game_copper += payTaskJson['data']['game_copper']
                                        else:
                                            print("用户" + str(userNo) + "：任务需求不满足,放弃")
                                            active += 5
                                            user_active -= 5
                                            close_data = parse.urlencode({'tid': id})
                                            request.urlopen(closeUserTask, data=close_data.encode('utf-8'))
                                        time.sleep(random.uniform(1, 2))
                                else:
                                    print("用户" + str(userNo) + "：不是指定任务,放弃")
                                    active += 5
                                    user_active -= 5
                                    close_data = parse.urlencode({'tid': id})
                                    request.urlopen(closeUserTask, data=close_data.encode('utf-8'))
                                    time.sleep(random.uniform(0.5, 1))
                                break
                with request.urlopen(getFationTask) as e:
                    getFationStr = e.read().decode('utf-8')
                    getFationJson = json.loads(getFationStr)
                    if getFationJson['code'] == 304 and getFationJson['msg'] == "少侠，当日已领取100个任务~":
                        unFinish = False
                        print(
                            "用户" + str(userNo) + "：任务结束,总共做了" + str(count) + "个任务,获得奖励如下：\n经验：" + str(
                                repair_num) + "\n金叶：" + str(
                                game_gold) + "\n银叶：" + str(game_silver) + "\n竹叶：" + str(
                                game_copper) + "\n用掉活力：" + str(active) +
                            "\n购买活力用了：" + str(payForActive) + "金叶"
                            + "\n------------------------------------")
                time.sleep(random.uniform(0.5, 1))
        except Exception as e:

            print(
                "用户" + str(userNo) + "：报错了,总共做了" + str(count) + "个任务,获得奖励如下：\n经验：" + str(
                    repair_num) + "\n金叶：" + str(
                    game_gold) + "\n银叶：" + str(game_silver) + "\n竹叶：" + str(
                    game_copper) + "\n用掉活力：" + str(active) +
                "\n购买活力用了：" + str(payForActive) + "金叶"
                + "\n------------------------------------")
            print(e)
            print(e.__traceback__.tb_lineno)
            time.sleep(5)
            userNo += 1
            continue
        userNo += 1


while True:
    try:
        do_fation_task()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)
        time.sleep(5)
        continue
