# 连接mongo
import pymongo
# 指定参数
client = pymongo.MongoClient('mongodb://192.168.8.103:27017/')
# 连接db
db = client.Yang
#  连接collections
collections = db.test
#  查询所有的数据
# for data in collections.find():
# #    print(data)
#  插入数据
# collections.insert({"name":"zhangsan","age":18})
for  i  in collections.find():
    print(i)

