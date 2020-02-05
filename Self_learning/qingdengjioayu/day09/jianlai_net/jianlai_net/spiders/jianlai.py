# -*- coding: utf-8 -*-
import scrapy

from ..items import JianlaiNetItem
class JianlaiSpider(scrapy.Spider):
    name = 'jianlai'
    allowed_domains = ['shuquge.com']
    start_urls = ['http://www.shuquge.com/txt/8659/index.html']
    def parse(self, response):
        dds = response.css("div.listmain>dl>dd")
        print(len(dds))
        for dd in dds:
            url = dd.xpath("./a/@href").extract_first()
            yield scrapy.Request("http://www.shuquge.com/txt/8659/"+url,callback=self.chapter,meta={'url':url})
    def chapter(self,response):
        item = JianlaiNetItem()
        item['url'] = response.meta.get('url')
        item['title'] = response.css('div.content>h1::text').extract_first()
        content = response.css("div.content>div.showtxt::text").extract()
        item['content'] = [x.strip() for x in content if x.strip() != '']
        yield item