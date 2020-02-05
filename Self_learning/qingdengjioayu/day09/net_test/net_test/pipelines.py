# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#import pymongo
#import MySQLdb
#import redis
class NetTestPipeline(object):
    def process_item(self, item, spider):
        return item
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
#         for i in zip(links,titles):
#             sql = 'insert into article(title,links) values(%s,%s)'
#             self.cursor.execute(sql,[i[0],i[1]])
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
