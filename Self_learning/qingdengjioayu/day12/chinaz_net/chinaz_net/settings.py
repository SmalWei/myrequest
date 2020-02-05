# -*- coding: utf-8 -*-

# Scrapy settings for chinaz_net project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'chinaz_net'

SPIDER_MODULES = ['chinaz_net.spiders']
NEWSPIDER_MODULE = 'chinaz_net.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'chinaz_net (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
    'Referer': 'https://top.chinaz.com/hangye/index_yule_shishang.html',
    'Upgrade-Insecure-Requests': '1',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'chinaz_net.middlewares.ChinazNetSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
###################################下载器中间件##########################################################
DOWNLOADER_MIDDLEWARES = {
    'chinaz_net.middlewares.ChinazNetDownloaderMiddleware': 543,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'chinaz_net.middlewares.UserAgentDownloaderMiddleware': 400,
  #  'chinaz_net.middlewares.ProxyDownloaderMiddleware': 400,
}
#################################下载器中间件完毕##############################################################
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'chinaz_net.pipelines.ChinazNetPipeline': 300,
#    'chinaz_net.pipelines.RedisPipeline': 400,
#    'chinaz_net.pipelines.MongoPipeline': 400,
#    'chinaz_net.pipelines.MysqlPipeline': 400,
#    'chinaz_net.pipelines.JsonPipeline':400,
   'chinaz_net.pipelines.CSVPipeline':400,
#    'chinaz_net.pipelines.DownloadPicturePipeline':400,
#    'scrapy.pipelines.images.ImagesPipeline': 1,
#    'scrapy.pipelines.files.FilesPipeline': 1
}
##########################################图片和文件的共同需要的设置###################
#project_dir = os.path.abspath(os.path.dirname(__file__))
######################################图片配置############################################################
############## 目前就设置了这么多###其他就没了
#IMAGES_STORE = os.path.join(project_dir,'images')
# 设定处理图片的最小高度，宽度
#IMAGES_MIN_HEIGHT = 100
#IMAGES_MIN_WIDTH = 10
###########################################################################################################


#####################################文件配置##############################################################
#FILES_STORE = os.path.join(project_dir,'files')
###########################################################################################################



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# mongo
#MONGODB_URI = 'mongodb://127.0.0.1:27017'
#MONGODB_SERVER="127.0.0.1"
#MONGODB_PORT=27017
#MONGODB_DB = "abckg" # 库名
#MONGODB_COLLECTION="content" # 集合（表）

# redis
#REDIS_URL = 'redis://127.0.0.1:6379'
#REDIS_SERVER = "127.0.0.1"
#REDIS_PORT = 6379
#REDIS_DB = 0   # 指定连接的库，0代表索引为0的库
#MY_REDIS='myspider:urls' #redis数据表中的myspider文件夹下的urls列表


# mysql
#MYSQL_HOST = "127.0.0.1"
#MUSQL_PORT =3306
#MYSQL_DBNAME ="junk"
#MYSQL_USER = "root"
#MYSQL_PASSWORD = "123456"
#LOG_LEVEL = 'DEBUG'


############################################## scrapy-Redis配置#################################
#SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#SCHEDULER_PERSIST = True
#REDIS_HOST = '127.0.0.1'
#REDIS_PORT = 6379
#REDIS_PASSWORD = ''
##########################################   scrapy-Redis配置完毕##############################


