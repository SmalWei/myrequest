#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@Time    : 2020/1/17 11:38
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  请更换这个文件的描述信息：作用以及目的
"""
from selenium import webdriver
import time
import csv

drive = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://music.163.com/#/playlist?id=924680166'
drive.get(url)
drive.switch_to.frame(0)

def parser_conmment(drive):
    items = drive.find_elements_by_css_selector('div.itm')
    with open("comment.csv",'a',encoding='utf-8',newline='') as f2:
        for item in items:
            user = item.find_element_by_css_selector("div.cnt").text
            cnt_time = item.find_element_by_css_selector("div.time").text
            print(user,cnt_time)
            spamwriter = csv.writer(f2, delimiter=',')
            data = [user,cnt_time]
            spamwriter.writerow(data)
js = 'window.scrollBy(0, 8000)'
drive.execute_script(js)
for i in range(3):
    parser_conmment(drive)
    drive.find_element_by_css_selector('a.znxt').click()
    time.sleep(1)
input()
drive.quit()
