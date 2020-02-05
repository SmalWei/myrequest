# -*- encoding: utf-8 -*-
"""
@File    : Async_IO_Base_1.py
@Time    : 2020/1/1 21:41
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Software: PyCharm
"""

###   生成器最重要的三个部分next(),send(),throw()

#  一个最简单的生成器
# def my_generator(n):
#     for i in range(n):
#         yield i
# for i in my_generator(10):
#     print(i)

# def my_generator(n):
#     for i in range(n):
#         temp = yield i
#         print(f'我是{temp}')
# g = my_generator(5)
# print(next(g)) #输出0
# print(next(g)) #输出1
# g.send(100)    #本来输出2，但是传入新的值100，改为输出100
# print(next(g)) #输出3
# print(next(g)) #输出4
# def my_generator(n):
#     for i in range(n):
#         yield i
#
# g=my_generator(5)
#
# print(next(g))
# print(next(g))
# print(g.send(100))#之所以没有打印，是没有被接受，所以不打印
# print(next(g))
# print(next(g))




