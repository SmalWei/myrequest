# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash
from scrapy_splash import SplashRequest

# splash lua script
script = """
function main(splash, args)
  splash:go(args.url)
  splash:wait(args.wait)
  splash:runjs("foo = function(){ var f = document.getElementById('g_iframe'); return f.contentDocument.getElementsByTagName('body')[0].innerHTML; }")
  local result = splash:evaljs("foo()")
  return result
end
"""
class Music163Spider(scrapy.Spider):
    name = 'music163'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/#/discover/toplist/']
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait':2,'lua_source':script}, endpoint='render.html')
            # yield SplashRequest(url, self.parse_result, callback  # 任务完成之后对应的回调函数
            # # args设置的是端点API的参数，关于API参数问题，请参考: `Splash HTTP API <./api.html>`_
            # args = {
            #            # 可选参数，表示spalsh在执行完成之后会等待一段时间后返回
            #            'wait': 0.5,
            #            # url是一个必须的参数，表明将要对哪个url进行请求
            #            'url': "http://www.example.com",
            #            # http_method:表示Splash将向目标url发送何种请求
            #            'http_method': 'GET'
            #            # 'body' 用于POST请求，作为请求的请求体
            #            # 'lua_source' 如果需要执行lua脚本，那么这个参数表示对应lua脚本的字符串
            #        },
            #        endpoint = 'render.json',  # optional; default is render.html
            #                   splash_url = '<url>',  # optional; overrides SPLASH_URL
            #                                slot_policy = scrapy_splash.SlotPolicy.PER_DOMAIN,  # optional,
            # # "meta" 是一个用来向回调函数传入参数的方式，在回调函数中的response.meta中可以取到这个地方传入的参数
            # )
    def parse(self, response):
        with open('a.txt','w',encoding='utf-8') as f:
            f.write(response.text)
