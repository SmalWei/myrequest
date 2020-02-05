"""
将此页面下的图片全部获取下来：https://www.vmgirls.com/12985.html
"""
"""清下下方开始编写代码"""
import requests
from lxml import etree
import os.path as p
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/12985.html', headers=headers)
ele = etree.HTML(response.text)
img_urls= ele.xpath("//div[@class='nc-light-gallery']/p/a/@href")
for i in img_urls:
    res = requests.get(i,headers=headers)
    name = "images/"+p.split(i)[-1]
    print(name)
    with open(name,'wb') as w:
        w.write(res.content)



