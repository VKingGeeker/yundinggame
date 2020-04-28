import requests
from prettytable import PrettyTable

priceUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no={}&from_station_no={}&to_station_no={}&seat_types={}&train_date={}'.format(
    '27000K783306', '02', '05', '113', '2019-07-23')
priceRes = requests.get(priceUrl)


print(list(dict(priceRes.json()['data']).keys()))
for key in list(dict(priceRes.json()['data']).keys()):
    if key == 'A1':
        print(priceRes.json()['data'][key])
    elif key == 'A2':
        print(priceRes.json()['data'][key])
    elif key == 'A3':
        print(priceRes.json()['data'][key])