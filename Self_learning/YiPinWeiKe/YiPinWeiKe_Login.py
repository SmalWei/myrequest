#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : YiPinWeiKe_Login.py
@Time    : 2020/1/4 17:15
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  这是一个一品威客的登录_js
"""
import execjs
with open("my.js",'r',encoding='utf-8') as f:
    contend = f.read()
    js = execjs.compile(contend)
    res = js.call("hex_md5",'duanwei112')
    print(res)