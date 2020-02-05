"""
作业提交格式
    + 使用源代码的方式提交，题目用 `注释` 的方式写在源代码里面。
    + 作业文件命名：第几次作业-编号-作业编号-姓名.py（例如01-00-01-正心.py）
    + 提交到QQ邮箱：2328074219@qq.com
    + 作业在第二天上课课后讲解

将上课的案例-爬取小说完善。爬取《剑来》所有章节用章节名分别保存。
"""
"""清下下方开始编写代码"""
import requests
from lxml import etree
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url = 'http://www.shuquge.com/txt/8659/index.html'
res = requests.get(url,headers=headers)
ele = etree.HTML(res.text)
urls = ele.xpath("//div[@class='listmain']//dd/a/@href")
for i in urls:
    i = 'http://www.shuquge.com/txt/8659/'+i
    res = requests.get(i,headers=headers)
    ele = etree.HTML(res.content.decode())
    title = ele.xpath("//div[@class='content']/h1/text()")[0]
    content = ele.xpath("//div[@id='content']/text()")
    page = [x.strip() for x in content if x.strip() != '']
    with open('book/'+title+'.txt','w',encoding='utf-8') as f:
        f.write(''.join(page))




