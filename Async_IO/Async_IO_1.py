#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : Async_IO_1.py
@Time    : 2020/1/17 19:01
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : # Python 高级编程之 asyncio并发编程_demo
"""
import asyncio
import time
async def get_html(url):
    print(f"start get {url}")
    await asyncio.sleep(2)
    print(f'end get {url}')
if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com/"+str(i)) for i in range(10)]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time()-start_time)