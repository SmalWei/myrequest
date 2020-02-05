import redis
#连接redis
import redis
##
red  = redis.Redis(host='127.0.0.1',port=6379,password='',db=1,decode_responses=True)
####################################### String #############################################
# red.set('name',"duanwei")
# 获取数据
# print(red.get("name"))
#  批量设置数据
# red.mset({"age":"18","birth":"1997"})
# 打印数据
# print(red.mget('name','age','birth')) #  返回一个列表的形式
# print(red.getset("name", 'duanwei2')) # 改变旧值为新值
# print(red.getrange("name",0,-1)) # 打印一个键的值
# red.append("name","haha")  #在值的后面进行一定的追加
#########################################  hash ##################################################
# red.hset("hash1", "k1", "v1")
# red.hset("hash1", "k2", "v2") #设置值
# print(red.hkeys("hash1"))  #  得到所有的键
# print(red.hget("hash1","k1"))  #   获取单个键
# print(red.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
# print(red.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
# print(red.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value --方式2
# red.hmset("hash1", {"k2": "v2", "k3": "v3"})
# print(red.hgetall('hash1'))
# print(red.hlen('hash1')) #  打印长度
# print(red.hvals("hash1"))  #  打印所有的values
# red.hde1()
# print(red.hscan("hash1")) # 取值查看–分片读取
# for item in red.hscan_iter('hash1'): # 利用yield封装hscan创建生成器，实现分批去redis中获取数据
#     print(item)
# print(red.hscan_iter("hash1"))  # 生成器内存地址
################################################## list ######################################################
# red.lpush('list1',11,22,33) #  每个新的元素都添加到列表的最左边
# red.rpush("list2",11,22,33) #  每个新的元素都添加到列表的最右边
# print(red.lrange('list2',0,-1))
# print(red.llen("list1"))
# red.lpushx("list10", 10)  # 这里list10不存在 #  lpushx 往已经有的name的列表里添加元素
# print(red.llen("list10"))  # 0
# print(red.lrange("list10", 0, -1))  # []
# r.rpushx("list2", 99)  rpushx 往已经有的name的列表里添加元素
# red.linsert("list2", "before", "11", "00")   #linsert(name, where, refvalue, value)) 在name对应的列表的某一个值前或后插入一个新值
# red.lset("list2", 0, -11) # r.lset(name, index, value)  对name对应的list中的某一个索引位置重新赋值
# red.lrem(name, value, num)   在name对应的list中删除指定的值
# red.lrem("list2", "11", 1)    # 将列表中左边第一次出现的"11"删除
# red.lrem("list2", "99", -1)    # 将列表中右边第一次出现的"99"删除
# red.lrem("list2", "22", 0)    # 将列表中所有的"22"删除
# red.lpop("list2")    # 删除列表最左边的元素，并且返回删除的元素
# red.rpop("list2")    # 删除列表最右边的元素，并且返回删除的元素
# print(red.lindex("list2", 0))  # 取出索引号是0的值  在name对应的列表中根据索引获取列表元素
# red.brpoplpush("list1", "list2", timeout=2)  #从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
#######################################################     set  ##################################################################
# red.sadd("set1", 33, 44, 55, 66) # 增加元素
# print(red.scard("set1"))  # 集合的长度是4
# print(red.smembers("set1"))
# for i in red.sscan_iter("set1"):# 遍历元素
#     print(i)


