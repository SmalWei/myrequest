# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
import re


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['ankule.com']
    start_urls = ['https://ty.anjuke.com/sale/p{page}/#filtersort' for i in range(1,100)]

    def parse(self, response):
        lis = response.css("#houselist-mod-new>li.list-item")
        for li in lis:
            title = li.css("div.house-title>a::text").extract_first().strip()
            detail = li.css("div.details-item>span::text").extract()
            detail =[re.sub('[\\xa0|\\s]','',content.strip()) for content in detail if content.strip()!='']
            price = li.css("div.pro-price strong::text").extract_first()
            print(title,detail,price)

