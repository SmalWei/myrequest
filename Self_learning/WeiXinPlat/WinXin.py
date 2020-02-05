#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : WinXin.py
@Time    : 2020/1/5 8:25
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  调用WinXinMD5.js
"""
import execjs
with open("my.js",'r',encoding='utf-8') as f:
    js = f.read()
    func = execjs.compile(js)
    print(func.call("Winxin",'duanwei112'))