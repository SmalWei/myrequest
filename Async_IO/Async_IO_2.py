#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : Async_IO_2.py
@Time    : 2020/1/17 19:08
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  Python 高级编程之 asyncio并发编程_获取返回值
"""
import asyncio
import time
from functools import partial
async def get_html(url):
    print(f'start get {url}')
    await asyncio.sleep(2)
    return 'bobby'
if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    loop.run_until_complete(get_future)
    print(get_future.result())
    # task = loop.create_task(get_html("http://www.imooc.com"))
    # loop.run_until_complete(task)
    # print(task.result())