"""
    使用 xpath 选择器将猫眼250的所有电影信息全部提取出来。
    title（获取中文名即可）
    start（导演、主演、时间、地点）
    score（分数）
    releasetime（发布时间）
    image（图片在互联网上的地址）

    通过对字段的凭借处理，成功实现了提取主演，发布时间等数据

    将数据以逗号分割，写入txt文本
"""
import parsel
import requests
import re
urls = [f'https://movie.douban.com/top250?start={num}&filter=' for num in range(0,250,25)]
for url in urls[:1]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Referer': 'https: // movie.douban.com / top250?start = 25 & filter =',
    }
    res = requests.get(url,headers=headers)
    selector = parsel.Selector(res.text)
    lis = selector.xpath("//ol[@class='grid_view']/li")
    with open("a.txt",'a',encoding='utf-8') as f:
        for li in lis:
            # title = li.xpath(".//div[@class='hd']/a/span[1]/text()").get()
            start = li.xpath(".//div[@class='bd']/p[1]").get()
            start1 = re.sub(r'[<p class="">,<br>,</p>," ","  ","\n"]','',start)
            # score = li.xpath(".//div[@class='star']/span[2]/text()").get() # ok
            releasetime = li.xpath(".//div[@class='bd']/p").re('\d{4}')[0]
            # image = li.xpath(".//div[@class='pic']//img/@src").get()
            print(releasetime,start1,sep='\n')




