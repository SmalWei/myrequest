# 1. 导入工具包
import requests
# 导入正则 解析数据
import re

# 2. 发送请求
response = requests.get('http://www.shuquge.com/txt/8659/2324752.html')
"""
http://         请求协议，http 超文本（图片、网页、视频、音频）传输协议 
www             是服务器的名字 www（world wide web），代表网站服务
shuquge.com     网站名 服务器名+域名 cn
/               服务器的根目录
txt/8659/       文件存放给的路径
2324752.html    文件的名字 
"""
# http 协议 url 部分
response.encoding = response.apparent_encoding
# print(response.text)
# print(response)
"""
200     凡是以2开头的状态码 都是成功
404     凡是以4开有的状态码 都是客户端的问题（请求不存在的内容）
500     凡是以5开头的状态吗 都是服务器的问题
"""
html = response.text
# with open('demo.html', mode='w', encoding='utf-8') as f:
#     f.write(html)
# 解析小说数据
# re.findall 返回的是一个列表 re.S 使.能匹配\n
result = re.findall('<div id="content" class="showtxt">(.*?)</div>', html, re.S)

with open('a.txt', mode='w', encoding='utf-8') as f:
    f.write(result[0].replace('<br/>&nbsp;&nbsp;&nbsp;&nbsp;', "").replace('<br/>', ""))
