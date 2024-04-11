# -*- coding:utf-8 -*-
from cgi import test
import requests
import json
import datetime

now_raw = datetime.datetime.now()
today = now_raw.strftime('%Y%m%d'+'12')

url = "https://www.jma.go.jp/bosai/amedas/data/map/" + today + "0000.json"
header = {"content-type": "application/json"}

response = requests.get(url, headers=header)
# 名古屋市(51106)のtempを表示
data = response.json()
temp_arry = data["51106"]["temp"]
print(temp_arry[0])
temp_today = temp_arry[0]

## 昨日の気温を取得
yesterday_raw = datetime.datetime.now() - datetime.timedelta(1)
yesterday = yesterday_raw.strftime('%Y%m%d'+'12')

url = "https://www.jma.go.jp/bosai/amedas/data/map/" + yesterday + "0000.json"
header = {"content-type": "application/json"}

response = requests.get(url, headers=header)
# 名古屋市のtempを表示
data = response.json()
temp_arry = data["51106"]["temp"]
print(temp_arry[0])
temp_yestarday = temp_arry[0]


## 明日の気温を取得
tommorow_raw = datetime.datetime.now() + datetime.timedelta(1)
tommorow = tommorow_raw.strftime('%Y%m%d'+'12')

url = "https://www.jma.go.jp/bosai/amedas/data/map/" + tommorow + "0000.json"
header = {"content-type": "application/json"}

response = requests.get(url, headers=header)
# 名古屋市のtempを表示
data = response.json()
temp_arry = data["51106"]["temp"]
print(temp_arry[0])
temp_tommorow = temp_arry[0]

print(temp_yestarday)
print(temp_today)
print(temp_tommorow)