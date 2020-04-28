# coding=utf-8
import urllib
from urllib import request
import requests
from prettytable import PrettyTable
from colorama import init, Fore

# 12306查票系统
# 0.得到站点对应编码的json

station = requests.get(url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js")
line = str(station.content, encoding="utf8")
clean_data = line.split('|')
# 站名:代码
dictX = {}
# 代码:站名
dictY = {}
resultX = clean_data[1:len(clean_data):5]  # 观察数据后,切片,从i=1开始,每次间隔5个,做字典key
resultY = clean_data[2:len(clean_data):5]  # 观察数据后,切片,从i=2开始,每次间隔5个,做字典value
for i in range(len(resultX)):
    dictX[resultX[i]] = resultY[i]
    dictY[resultY[i]] = resultX[i]
# # 1.接收用户输入出发站,到达站,出发时间,存入变量
onStation = dictX[input('出发站:\t').strip().replace('站', '')]
offStation = dictX[input('到达站:\t').strip().replace('站', '')]
onDate = input('出发日期(例如:2019-07-23):\t'.strip())
# 2.在url中加入出发站,到达站,出发时间变量
reqUrl = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
    onDate, onStation, offStation)
# 3.请求url,得到json,循环解析json,每次取出一个车次的信息,储存,得到票价相关的参数,储存,请求票价url,打印
res = requests.get(reqUrl)
# json -> data -> result  json逐层取出车次的数组
resultArr = res.json()['data']['result']
ptable = PrettyTable(
    ['车次', '出发/到达站', '出发/到达时间', '历时', '商务座', '一等座', '二等座', '高级软卧', '软卧', '动卧', '硬卧', '软座', '硬座', '无座', '其他'])

# 遍历车次数组,取出每个车次的信息
for result in resultArr:
    # 将该车次的信息以'|'分割成数组,就可以得到固定位置的值
    resultStrArr = str(result).split('|', -1)

    # 车次
    trainId = resultStrArr[3]
    # 首发站
    startStation = dictY[resultStrArr[4]]
    # 终点站
    endStation = dictY[resultStrArr[5]]
    # 出发站
    onStation = Fore.LIGHTRED_EX + dictY[resultStrArr[6]] + Fore.RESET
    # 到达站
    offStation = Fore.LIGHTGREEN_EX + dictY[resultStrArr[7]] + Fore.RESET
    # 出发时间
    onTime = Fore.LIGHTRED_EX + resultStrArr[8] + Fore.RESET
    # 到达时间
    offTime = Fore.LIGHTGREEN_EX + resultStrArr[9] + Fore.RESET
    # 历时
    during = resultStrArr[10]
    # 商务座特等座
    shangwuzuo = resultStrArr[20] if (resultStrArr[20] != '') else '--'
    # 一等座
    yidengzuo = resultStrArr[21] if (resultStrArr[21] != '') else '--'
    # 二等座
    erdengzuo = resultStrArr[22] if (resultStrArr[22] != '') else '--'
    # 高级软卧
    gaojiruanwo = resultStrArr[23] if (resultStrArr[23] != '') else '--'
    # 软卧一等卧
    ruanwoyidengwo = resultStrArr[24] if (resultStrArr[24] != '') else '--'
    # 动卧
    dongwo = resultStrArr[25] if (resultStrArr[25] != '') else '--'
    # 硬卧二等卧
    yingwoerdengwo = resultStrArr[26] if (resultStrArr[26] != '') else '--'
    # 软座
    ruanzuo = resultStrArr[27] if (resultStrArr[27] != '') else '--'
    # 硬座
    yingzuo = resultStrArr[28] if (resultStrArr[28] != '') else '--'
    # 无座
    wuzuo = resultStrArr[29] if (resultStrArr[29] != '') else '--'
    # 其他
    other = resultStrArr[30] if (resultStrArr[30] != '') else '--'
    # 票价参数 train_no
    trainNo = resultStrArr[2]
    # 票价参数 from_station_no
    fromStationNo = resultStrArr[16]
    # 票价参数 to_station_no
    toStationNo = resultStrArr[17]
    # 票价参数 seat_types
    seatTypes = resultStrArr[35]
    priceUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no={}&from_station_no={}&to_station_no={}&seat_types={}&train_date={}'.format(
        trainNo, fromStationNo, toStationNo, seatTypes, onDate)
    priceRes = requests.get(priceUrl)
    priceData = priceRes.json()['data']
    for key in list(dict(priceRes.json()['data']).keys()):
        if key == 'A9' or key == 'P':
            shangwuzuo += '\n' + priceData[key]
        elif key == 'M':
            yidengzuo += '\n' + priceData[key]
        elif key == 'O':
            erdengzuo += '\n' + priceData[key]
        elif key == 'A6':
            gaojiruanwo += '\n' + priceData[key]
        elif key == 'A4':
            ruanwoyidengwo += '\n' + priceData[key]
        elif key == 'F':
            dongwo += '\n' + priceData[key]
        elif key == 'A3':
            yingwoerdengwo += '\n' + priceData[key]
        elif key == 'A2':
            ruanzuo += '\n' + priceData[key]
        elif key == 'A1':
            yingzuo += '\n' + priceData[key]
        elif key == 'WZ':
            wuzuo += '\n' + priceData[key]
    infos = [trainId, onStation + '\n' + offStation, onTime + '\n' + offTime + '\n', during,
             shangwuzuo, yidengzuo,
             erdengzuo, gaojiruanwo,
             ruanwoyidengwo, dongwo,
             yingwoerdengwo, ruanzuo,
             yingzuo, wuzuo, other]

    ptable.add_row(infos)
##金额存在bug
print(ptable)
# priceReq = requests.Request('https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=27000K783306&from_station_no=02&to_station_no=05&seat_types=113&train_date=2019-07-23')
# req=request.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-07-23&leftTicketDTO.from_station=TNV&leftTicketDTO.to_station=FAV&purpose_codes=ADULT')


# r = requests.get(
#     'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-07-23&leftTicketDTO.from_station=TNV&leftTicketDTO.to_station=FAV&purpose_codes=ADULT')
# # json -> data -> result
# print(str(r.json()['data']['result']))
