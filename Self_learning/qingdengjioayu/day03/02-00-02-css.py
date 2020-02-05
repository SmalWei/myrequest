"""
    使用 css 选择器将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
import parsel
urls  = [f'https://maoyan.com/board/4?offset={num}' for num in range(0,100,10)]
for i in urls:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Referer': 'https://maoyan.com/board/4?offset=0'
    }
    res = requests.get(i,headers=headers)
    sel = parsel.Selector(res.content.decode())
    dds = sel.css('.main dd')
    # 一个很好的思路就是先提取到他的父集，在提取到他的子集
    for dd in dds:
        name = dd.css(".name>a::text").get()
        star  = dd.css(".star::text").get().strip()
        releasetime = dd.css('.releasetime::text').get()
        score = dd.css('p.score i.integer::text').get()+dd.css("p.score i.fraction::text").get()
        print(name,star,releasetime,score)








