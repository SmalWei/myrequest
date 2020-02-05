# -*- coding: utf-8 -*-
import scrapy
from ..items import LyNetItem
import json
import re
class LySpider(scrapy.Spider):
    name = 'ly'
    allowed_domains = ['7799520.com']
    start_urls = [f'http://www.7799520.com/api/recommend/pc/luck/list?token=&page={page}' for page in range(1,20)]

    def parse(self, response):
        data  =  json.loads(response.text,encoding='utf-8')
        user_list = data['data']['list']
        for user in user_list:
            item = LyNetItem()
            for k,v in user.items():
                item[k] = v.replace("\n","").replace("\t","")
            yield item
