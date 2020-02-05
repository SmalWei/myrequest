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

################无参数的时候
# import asyncio
# import time
# from functools import partial
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     return "bobby"
#
# # 注意，这里必须有一个 future 参数，这个 Future 就是下面的 task
# def callback(future):
#     print("send email to bobby")
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(get_html("http://www.imooc.com"))
#     task.add_done_callback(callback)
#     loop.run_until_complete(task)
#     print(task.result())

##########有参数的时候####################
import asyncio
import time
from functools import partial
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"

# 注意，这里必须有一个 Future 参数
def callback(url, future):
    print(url)
    print("send email to bobby")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.imooc.com"))
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())

