# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChinazSpider(CrawlSpider):
    name = 'chinaz'
    allowed_domains = ['chinaz.com']
    start_urls = ['https://top.chinaz.com/hangyemap.html']
    rules = (
        Rule(LinkExtractor(allow=r'https://top.chinaz.com/hangye/index_shopping.*?.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'index_shopping.*?.html'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        print(response.url)
        lis = response.css("li.clearfix")
        for li in lis:
            name = li.xpath("./div[2]/h3/a/text()").extract_first()
            rank = li.xpath("./div[2]/div/p/a/text()").extract_first()
            intro = li.xpath("./div[2]/p/text()").extract_first()
            score = li.xpath("./div[3]//span/text()").extract_first()
            print(name,rank,intro,score)
            item = {'name':name,'rank':rank,'intro':intro,"score":score}
            yield item
