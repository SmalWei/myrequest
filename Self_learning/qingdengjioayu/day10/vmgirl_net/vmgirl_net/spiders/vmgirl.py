# -*- coding: utf-8 -*-
import scrapy
from ..items import VmgirlNetItem

class VmgirlSpider(scrapy.Spider):
    name = 'vmgirl'
    allowed_domains = ['vmgirls.com']
    ### 因为发送的是post请求，所以将starturls 删掉了
    def start_requests(self):
        for i in range(1,2):
            yield scrapy.FormRequest(
                url="https://www.vmgirls.com/wp-admin/admin-ajax.php",
                formdata={'append': 'list-home',
                          'paged': str(i),
                          'page': 'home',
                          'action': 'ajax_load_posts',
                          'query':''},

            )
    def parse(self, response):
        urls = response.css("div.list-content div.list-body>a::attr(href)").extract()
        titles = response.css("div.list-content div.list-body>a::text").extract()
        for url,title in zip(urls,titles):
            yield scrapy.Request(url,meta={'title':title},callback=self.detail_page)
    def detail_page(self,response):
        page_url_set = response.css("div.nav-links>a.post-page-numbers::attr(href)").extract()
        item = VmgirlNetItem()
        title = response.meta.get("title")
        imgurls = response.css("div.nc-light-gallery a::attr(href)").extract()
        item['title'] = title
        item['imgurls'] = imgurls
        yield item
        for page_url in page_url_set:
            print(page_url)
            yield scrapy.Request(page_url, meta={'title': title}, callback=self.detail_page_other)
    def detail_page_other(self,response):
        item = VmgirlNetItem()
        item['title'] = response.meta.get("title")
        item['imgurls'] = response.css("div.nc-light-gallery a::attr(href)").extract()
        yield item


