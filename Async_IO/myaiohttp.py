import asyncio
import requests
@asyncio.coroutine
def fetch_async(func, *args):
    # 获取事件循环：就是有个循环一直等待这用户的响应
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, func, *args) # 执行传递进来的get函数
    response = yield from future
    print(response.url, response.content)
tasks = [
    fetch_async(requests.get, 'http://www.cnblogs.com/ftl1012/'),
    fetch_async(requests.get, 'http://dig.chouti.com/images/homepage_download.png')
]
loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()