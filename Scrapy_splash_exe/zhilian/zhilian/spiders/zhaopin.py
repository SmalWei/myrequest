# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
class ZhaopinSpider(scrapy.Spider):
    name = 'zhipin'
    # allowed_domains = ['zhaopin.com']
    start_urls = [f'https://sou.zhaopin.com/?p={page}&jl=530&kw=python&kt=3' for page in range(1,3)]
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait':2}, endpoint='render.html')

    def parse(self, response):
        divs = response.xpath("//div[@id='listContent']/div[@class='contentpile__content__wrapper clearfix']")
        print(divs)
        for div in divs:
            from Scrapy_splash_exe.zhilian.zhilian.items import ZhilianItem
            item = ZhilianItem()
            item['jobName'] = div.css("div.jobName span::attr(title)").extract_first()
            item['commpanyName'] = div.css("div.commpanyName a::text").extract_first()
            intro = div.css("div.jobDesc  li::text").extract()
            item['intro'] = ','.join([x.strip() for x in intro])
            yield item

