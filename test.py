# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
import datetime

line_bot_api = LineBotApi(
    'n443DirXp6ghBp2+Q5hpCZlX/+ZcrMBcS4DKyWuPSshrpI9PwS+lKOD53rYzCwSw65MT+cEbmG8BPEoiIuaiZfGHzwh6q2BqV7tURH3bRRmLnzGT/BRVkMQDPEVmKjBvxGyc4QIJrKtJqsOwfTK8rAdB04t89/1O/w1cDnyilFU=')
line_id = 'Ud4b0c48834fe2b1adf22cddc56b15373'
url = 'https://acg.gamer.com.tw/index.php?t=1&p=PS4'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
game = soup.find_all('div', 'ACG-mainbox1')
articles = []  # 儲存取得的文章資料(json格式)


# 傳line訊息(只有text)
def line_push_only_text(id, textInsert):
    line_bot_api.push_message(id, TextSendMessage(text=textInsert))


def line_push_img(id, img):
    line_bot_api.push_message(id, ImageSendMessage(original_content_url=img, preview_image_url=img))


# 傳title
str2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + '巴哈最新ps4遊戲'
line_push_only_text(line_id, str2)

# 轉換網頁並傳Line訊息
for d in game:
    title = d.find('a').string
    type = d.find('li').string
    href = d.find('a').get('href')
    img = d.find('div', 'ACG-mainbox2B').find('img').get('src')
    imgSub = d.find('img').get('src')
    str = ""
    str += title + "," + type + href +"\n"
    # push message to one user
    line_push_only_text(line_id, str)
    line_push_img(line_id, imgSub)
    #
    articles.append({
        'title': title,
        'type': type,
        'url': href
    })

line_push_only_text(line_id,
                    '------------------------------------------------------------------------------------------------')

for article in articles:
    print(article)
