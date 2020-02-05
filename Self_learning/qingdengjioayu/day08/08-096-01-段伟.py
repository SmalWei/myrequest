# encoding:utf-8
"""
    使用线程池爬取猫眼100的数据
"""
import concurrent.futures
import requests
import parsel
urls  = [f'https://maoyan.com/board/4?offset={num}' for num in range(0,100,10)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': 'https://maoyan.com/board/4?offset=0'
}
def parsel_url(url):
    res = requests.get(url,headers=headers)
    sel = parsel.Selector(res.content.decode())
    dds = sel.css('.main dd')
    # 一个很好的思路就是先提取到他的父集，在提取到他的子集
    for dd in dds:
        name = dd.css(".name>a::text").get()
        star  = dd.css(".star::text").get().strip()
        releasetime = dd.css('.releasetime::text').get()
        score = dd.css('p.score i.integer::text').get()+dd.css("p.score i.fraction::text").get()
        print(name,star,releasetime,score)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(parsel_url,urls)


