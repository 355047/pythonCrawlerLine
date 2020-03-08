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
    'FsCRykbeNsYRTEnCFIvdqfVJAUj5dXO3Gi0kiPEtBxOiHCTTQbPOAR3hv+wHVmjRVcNJkrqS9hgyO44+FD+KE8cMFabl5urogPbCJUOT8eRefllmBZcQncPFKcFu9aPi7oQPdeV99bpLWxbOTkNPDgdB04t89/1O/w1cDnyilFU=')
line_id = 'U549d38ee4540de4c4b4bf371a1a94d60'
respComicurl = 'http://18h.animezilla.com/manga'
respOriginalDoujinshiUrl = 'http://18h.animezilla.com/doujinshi/original'
respParodyDoujinshiUrl = 'http://18h.animezilla.com/doujinshi/parody'

respComic = requests.get(respComicurl)
soupComic = BeautifulSoup(respComic.text, 'html.parser')
hcomic = soupComic.find_all('div', 'entry-content')
hcomicTop = soupComic.find_all('div', 'pure-u-1-3')
respOriginalDoujinshi = requests.get(respOriginalDoujinshiUrl)
soupOriginalDoujinshi = BeautifulSoup(respOriginalDoujinshi.text, 'html.parser')
hOriginalDoujinshi = soupOriginalDoujinshi.find_all('div', 'entry-content')
respParodyDoujinshi = requests.get(respParodyDoujinshiUrl)
soupParodyDoujinshi = BeautifulSoup(respParodyDoujinshi.text, 'html.parser')
hParodyDoujinshi = soupParodyDoujinshi.find_all('div', 'entry-content')
articles = []  # 儲存取得的文章資料(json格式)


# 傳line訊息(只有text)
def line_push_only_text(id, textInsert):
    line_bot_api.push_message(id, TextSendMessage(text=textInsert))


def line_push_img(id, img):
    line_bot_api.push_message(id, ImageSendMessage(original_content_url=img, preview_image_url=img))


def sendTitle(text):
    # 傳title
    str2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + text
    line_push_only_text(line_id, str2)


def sendHcomicLine():
    # 轉換網頁並傳Line訊息
    for d in hcomic[0:3]:
        title = d.find('h2', 'entry-title').find('a').string
        type = d.find('h2', 'entry-title').find('a').string
        img = d.find('img').get('src')
        href = d.find('h2', 'entry-title').find('a').get('href')
        str = ""
        str += title + href
        # push message to one user
        line_push_only_text(line_id, str)
        line_push_img(line_id, img)
        #
        articles.append({
            'title': title,
            'type': type
        })


# hasnt finish
def sendHcomicTopLine():
    # 轉換網頁並傳Line訊息
    for d in hcomicTop[0:3]:
        title = d.find('span').string
        type = d.find('span').string
        img = d.find('img').get('background:url')
        href = d.find('h2', 'entry-title').find('a').get('href')
        str = ""
        str += title
        # push message to one user
        line_push_only_text(line_id, str)
        line_push_img(line_id, img)
        #
        articles.append({
            'title': title,
            'type': type
        })


def sendOriginalDoujinshiLine():
    # 轉換網頁並傳Line訊息
    for d in hOriginalDoujinshi[0:3]:
        title = d.find('h2', 'entry-title').find('a').string
        type = d.find('h2', 'entry-title').find('a').string
        img = d.find('img').get('src')
        href = d.find('h2', 'entry-title').find('a').get('href')
        str = ""
        str += title + href
        # push message to one user
        line_push_only_text(line_id, str)
        line_push_img(line_id, img)
        #
        articles.append({
            'title': title,
            'type': type
        })

def sendParodyDoujinshiLine():
    # 轉換網頁並傳Line訊息
    for d in hParodyDoujinshi[0:3]:
        title = d.find('h2', 'entry-title').find('a').string
        type = d.find('h2', 'entry-title').find('a').string
        img = d.find('img').get('src')
        href = d.find('h2', 'entry-title').find('a').get('href')
        str = ""
        str += title + href
        # push message to one user
        line_push_only_text(line_id, str)
        # line_push_only_text(line_id, href)
        line_push_img(line_id, img)
        #
        articles.append({
            'title': title,
            'type': type
        })

def sendConsole():
    for article in articles:
        print(article)


if __name__ == '__main__':
    sendTitle('最新top3 h漫')
    sendHcomicLine()
    # sendHcomicTopLine()
    sendTitle('最新top3 原創同人')
    sendOriginalDoujinshiLine()
    sendTitle('最新top3 改編同人')
    sendParodyDoujinshiLine()
    sendConsole()
    line_push_only_text(line_id,
                        '------------------------------------------------------------------------------------------------')
