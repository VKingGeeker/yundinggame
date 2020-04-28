# coding=utf-8
import requests
import re

#获取12306站点及其对应缩写
def send_request():
    try:
        response = requests.get(
            url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js",
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))

        line = str(response.content, encoding="utf8")
        clean_data = line.split('|')
        dictx = {}
        resultx = clean_data[1:len(clean_data):5]  # 观察数据后,切片,从i=1开始,每次间隔5个,做字典key
        resulty = clean_data[2:len(clean_data):5]  # 观察数据后,切片,从i=2开始,每次间隔5个,做字典value
        for i in range(len(resultx)):
            dictx[resultx[i]] = resulty[i]
        f = open("ceshi_result.txt", 'w+')  # 最终数据写入文件
        f.truncate()
        f.write(str(dictx))
        # f.truncate()
        # f.write(strr)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


send_request()