#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : xianyu_data.py
@Time    : 2020/1/5 15:20
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  请更换这个文件的描述信息：作用以及目的
"""
import requests
import time
import execjs
def page():
    timestemp = round(time.time())
    url = 'https://h5api.m.taobao.com/h5/mtop.taobao.idle.mach.item.service.faas.item/1.0/?'
    with open('my.js', 'r', encoding='utf-8') as f:
        js = f.read()
        excute = execjs.compile(js)
        data = '{"utdid":"e7ee65617aebd","dataSourceId":"376","pageNumber":2,"catIds":""}'
        sign = excute.call('xianyu',1578215076451,data)
    print(sign)
    params ={
        'jsv':'2.5.6',
        'appKey':'12574478',
        't':str(timestemp),
        'sign':sign,
        'api':'mtop.taobao.idle.mach.item.service.faas.item',
        'v':'1.0',
        'uttid':'e7ee65617aebd',
        'type':'jsonp',
        'dataType':'jsonp',
        'callback':'mtopjsonp4',
        'data':data,
    }
    headers = {
        'cookie': 'thw=cn; t=3cca68e18168b906fd2ecd80e9f19a12; cna=qkmQFovXdEICAXPu8abjrDK5; miid=288752082092749610; cookie2=1bf2bb8c7b32dd9f82b052f0be2b5b07; v=0; _tb_token_=e7ee65617aebd; _m_h5_tk=961f86a2a0324d38bb8d14f8c23af9fd_1578217443291; _m_h5_tk_enc=0a173e31a9df91d23a327566c59b35c8; l=dBMwP0luQjuTg_aMBOCwourza77OSIRAguPzaNbMi_5wJ6L1ynbOox1CRFp6VjWfTYYB4WtSLw29-etumoxkzDmk11shxxDc.; isg=BPX1oRe0x6V_5iMBEBOQ8DNFBHGvcqmEQ45wRHcasWy7ThVAP8K5VANImFJdDsE8',
        'referer': 'https://2.taobao.com/',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    res = requests.get(url,params=params,headers=headers)
    print(res.text)
page()
