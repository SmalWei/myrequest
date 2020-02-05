# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ZhilianPipeline(object):
    def process_item(self, item, spider):
        return item
class JsonPipeline(object):
   def __init__(self):
   ####写入方式，，，，wb,,,,,,,
     self.file = open('job_info.json', 'a', encoding="utf-8")
   def process_item(self, item, spider):
       ###参照以上写法
       print(item)
       lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
       self.file.write(lines)
       #### 实现该方式#############
       return item

   def close_spider(self, spider):
       self.file.close()