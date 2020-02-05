# encoding:utf-8
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@Time    : 2020/1/17 10:04
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : # 使用selenium进行问卷调查填写
"""
from selenium import webdriver
import concurrent.futures
import random
import time
def submit_wenjuan():
    drive = webdriver.Chrome()
    url = 'https://www.wjx.cn/jq/53732451.aspx'
    drive.get(url)
    time.sleep(2)
    click_div = [0, 1, 3, 4, 5, 7, 9]
    check_div = [2, 8, 10, 11, 13]
    elements = drive.find_elements_by_css_selector('.div_question')
    for c in click_div:
        answer1 = elements[c]
        lis = answer1.find_elements_by_css_selector('li')
        lis[random.randint(0, len(lis) - 1)].click()
    for c in check_div:
        answer2 = elements[c]
        lis = answer2.find_elements_by_css_selector('li')
        length = len(lis)
        l = [i for i in range(length)]
        l = random.choices(l, k=int(length / 2))
        for i in l:
            lis[i].click()
    order_lis = elements[6].find_elements_by_css_selector('li')
    random.shuffle(order_lis)
    for i in order_lis:
        i.click()
    trs = elements[12].find_elements_by_css_selector('tr')
    for tr in trs[1:]:
        inputs = tr.find_elements_by_css_selector('a.jqRadio')
        inputs[random.randint(0, len(inputs) - 1)].click()
    answer3 = elements[14].find_element_by_css_selector('textarea')
    answer3.send_keys('也就一般吧')
    submit_button = drive.find_element_by_css_selector('input.submitbutton')
    time.sleep(2)
    submit_button.click()
    quit()
if __name__ == '__main__':
    process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=1)
    for i in range(2):
        process_pool.submit(submit_wenjuan)
    process_pool.shutdown()