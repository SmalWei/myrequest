# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LyNetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    userid=scrapy.Field()
    province=scrapy.Field()
    city=scrapy.Field()
    height=scrapy.Field()
    education=scrapy.Field()
    username=scrapy.Field()
    monolog=scrapy.Field()
    birthdayyear=scrapy.Field()
    avatar=scrapy.Field()
    gender=scrapy.Field()
    salary=scrapy.Field()
    marry=scrapy.Field()
    monologflag=scrapy.Field()
