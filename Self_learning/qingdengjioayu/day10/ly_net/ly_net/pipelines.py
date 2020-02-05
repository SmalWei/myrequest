# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#import pymongo
#import MySQLdb
#import redis
import csv
import os

from scrapy.exceptions import DropItem
import scrapy
from scrapy.pipelines.images import ImagesPipeline
#import os
import json
# class LyNetPipeline(object):
#     def process_item(self, item, spider):
#         print(item,"*"*20)
#         return item
######################################redis的配置文件########################################
# class RedisPipeline(object):
#     def __init__(self, redis_url, redis_db):
#         self.redis_url = redis_url
#         self.redis_db = redis_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         '''
#         scrapy为我们访问settings提供了这样的一个方法，这里，
#         我们需要从settings.py文件中，取得数据库的URI和数据库名称
#         '''
#         return cls(
#             redis_url=crawler.settings.get('REDIS_URL'),
#             redis_db=crawler.settings.get('REDIS_DB')
#         )
#     def open_spider(self, spider):  # 爬虫一旦开启，就会实现这个方法，连接到数据库
#         self.client = pymongo.MongoClient(self.redis_url)
#         self.db = self.client[self.redis_db]
#############################mongodb的配置文件#######################################################
# class MongoPipeline(object):
#
#     def __init__(self, mongo_uri, mongo_db,mongo_collection):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#         self.mongo_collection = mongo_collection
#
#     def process_item(self, item, spider):
#         table = self.db[self.mongo_collection]
#             #####自己写####
#         return item
#     @classmethod
#     def from_crawler(cls, crawler):
#         '''
#         scrapy为我们访问settings提供了这样的一个方法，这里，
#         我们需要从settings.py文件中，取得数据库的URI和数据库名称
#         '''
#         return cls(
#            mongo_uri=crawler.settings.get('MONGODB_URI'), #   数据库url
#            mongo_db=crawler.settings.get('MONGODB_DB'),#  数据库名
#            mongo_collection=crawler.settings.get('MONGODB_COLLECTION')  #  数据库的集合
#         )
#     def open_spider(self, spider):  # 爬虫一旦开启，就会实现这个方法，连接到数据库
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#         self.mongo_collection = self.mongo_collection
#     def close_spider(self, spider):  # 爬虫一旦关闭，就会实现这个方法，关闭数据库连接
#         self.client.close()
##########################################mysql的配置文件############################################
# class MysqlPipeline(object):
#     def __init__(self, mysql_host, mysql_port,mysql_dbname,mysql_user,mysql_password):
#         self.mysql_host = mysql_host
#         self.mysql_port = mysql_port
#         self.mysql_dbname = mysql_dbname
#         self.mysql_user = mysql_user
#         self.mysql_password = mysql_password
#     def process_item(self, item, spider):
#         titles = item['title']
#         links = item['link']
#         for links,titles in zip(links,titles):
#             sql = 'insert into article(title,links) values(%s,%s)'
#             self.cursor.execute(sql,[links,titles])
#         self.conn.commit()
#         return item
#     @classmethod
#     def from_crawler(cls, crawler):
#         '''
#         scrapy为我们访问settings提供了这样的一个方法，这里，
#         我们需要从settings.py文件中，取得数据库的URI和数据库名称
#         '''
#         return cls(
#             mysql_host=crawler.settings.get('MYSQL_HOST'),
#             mysql_port=crawler.settings.get('MUSQL_PORT'),
#             mysql_dbname = crawler.settings.get("MYSQL_DBNAME"),
#             mysql_user = crawler.settings.get("MYSQL_USER"),
#             mysql_password = crawler.settings.get("MYSQL_PASSWORD")
#         )
#     def open_spider(self, spider):  # 爬虫一旦开启，就会实现这个方法，连接到数据库
#         self.conn = MySQLdb.connect(
#             host=self.mysql_host,  # mysql所在的主机
#             port=self.mysql_port,  # 端口号
#             user=self.mysql_user,  # 连接的用户名
#             password=self.mysql_password,  # 密码
#             db=self.mysql_dbname,  # 连接的数据库
#             charset="utf8"  # 连接使用的字符集
#         )
#         self.cursor = self.conn.cursor()
#
#     def close_spider(self, spider):  # 爬虫一旦关闭，就会实现这个方法，关闭数据库连接
#         self.conn.close()
#######################################json的配置文件##########################################################
#class JsonPipeline(object):
#    def __init__(self):
#    ####写入方式，，，，wb,,,,,,,
#      self.file = open('item.json', 'w', encoding="utf-8")
#
#    def process_item(self, item, spider):
#        ###参照以上写法
#        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
#        self.file.write(lines)
#        #### 实现该方式#############
#        return item
#
#    def close_spider(self, spider):
#        self.file.close()
######################################csv的配置文件########################################################
class CSVPipeline(object):
   def __init__(self):
       self.file = open('data.csv', mode='w', encoding='utf-8', newline="")
       self.csv_write = csv.writer(self.file)
   def process_item(self, item, spider):
       self.csv_write.writerow(dict(item).values())
       return item
   def close_spider(self, spider):
       self.file.close()
###########################################下载图片的配置文件######################################################
class DownloadPicturePipeline(ImagesPipeline):
   def get_media_requests(self, item, info):
             ###从item获取的到item中url，发送请求，将参数传入
       yield scrapy.Request(item['avatar'], meta={'username': item['username']})

   def file_path(self, request, response=None, info=None):
       ## 重命名，若不重写这函数，图片名为哈希
       ## 提取url前面名称作为图片名。
       filename = request.meta.get('username') + os.path.splitext(request.url)[-1]
       # if r'/' in filename:
       #      filename = "\/".join(filename.split("/"))
       return filename

   def item_completed(self, results, item, info):
       ## 保存图片下载的路径
       image_paths = [x['path'] for ok, x in results if ok]
       if not image_paths:
           raise DropItem("Item contains no images")
       return item
###############################################下载文件的配置文件############################################
####  以后有需求了 再写####################################