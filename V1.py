# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:30:04 2020

@author: 賴秉閎

ETH價到鬧鐘
"""
import schedule
import time
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import pyglet
import os
import csv
import datetime


def job():
    #抓取以太封包
    url = 'https://ftx.com/api/markets/ETHBEAR/USD/candles/last?resolution=900'
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getjson = json.loads(soup.text)
    #設定價格
    if(getjson['result']['close'] > 2900):
        #導入MP3文件
        path = 'C:\\Users\\Mooncat\\Desktop\\python\\1.WAV'
        music= pyglet.media.load(path)
        music.play()
        pyglet.app.run()

#系統排程
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
time.sleep(1)

