#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : Async_IO_2.py
@Time    : 2020/1/17 19:08
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  Python 高级编程之 asynciowait和gather
"""
from functools import partial
import asyncio
import time

# gather 比 wait 更加高层。gather 可以将任务分组，一般优先使用 gather。在某些定制化任务需求的时候，会使用 wait。
# async def get_html(url):
#     print("start get url")
#     # 这里不能使用 time.sleep(2) 模拟 HTTP 请求，因为这是一个同步阻塞的方式
#     # 这个地方必须加 await
#     await asyncio.sleep(2)
#     print("end get url")
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("http://www.imooc.com") for i in range(10)]
#     # 这儿使用 gather 的时候，需要加一个星号，会将列表中的元素传进去
#     loop.run_until_complete(asyncio.gather(*tasks))
#     print(time.time()-start_time)
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     group1 = [get_html("http://projectsedu.com") for i in range(2)]
#     group2 = [get_html("http://www.imooc.com") for i in range(2)]
#     loop.run_until_complete(asyncio.gather(*group1, *group2))
#     print(time.time() - start_time)
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     group1 = [get_html("http://projectsedu.com") for i in range(2)]
#     group2 = [get_html("http://www.imooc.com") for i in range(2)]
#     group1 = asyncio.gather(*group1)
#     group2 = asyncio.gather(*group2)
#
#     loop.run_until_complete(asyncio.gather(group1, group2))
#     print(time.time() - start_time)








