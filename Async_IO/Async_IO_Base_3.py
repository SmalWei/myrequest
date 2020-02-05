#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : Async_IO_Base_3.py
@Time    : 2020/1/2 17:06
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  主要是关于yield from的一些用法和解释
"""
# 一、yield from  的简单应用
# def generator1():
#     for i in range(10):
#         yield i
# def generator2():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#     yield from generator1() #yield from iterable本质上等于 for item in iterable: yield item的缩写版
#     yield from [11,22,33,44]
#     yield from (12,23,34)
#     yield from range(3)
# for i in generator2():
#     print(i,end=' , ')
'''运行的结果为：
a , b , c , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 11 , 22 , 33 , 44 , 12 , 23 , 34 , 0 , 1 , 2 ,
'''
# 二、yielf from 的高级应用：
# def my_generator():
#     for i in range(5):
#         if i==2:
#             return '我被迫中断了'
#         else:
#             yield i
#
# def main(generator):
#     try:
#         for i in generator:  #不会显式触发异常，故而无法获取到return的值
#             print(i)
#     except StopIteration as exc:
#         print(exc.value)
#
# g=my_generator()  #调用
# main(g)
'''运行结果为：
0
1
'''
# def my_generator():
#     for i in range(5):
#         if i==2:
#             return '我被迫中断了'
#         else:
#             yield i
#
# def main(generator):
#     try:
#         print(next(generator))   #每次迭代一个值，则会显式出发StopIteration
#         print(next(generator))
#         print(next(generator))
#         print(next(generator))
#         print(next(generator))
#     except StopIteration as exc:
#         print(exc.value)     #获取返回的值
#
# g=my_generator()
# main(g)
'''运行结果为：
0
1
我被迫中断了
'''
# def my_generator():
#     for i in range(5):
#         if i==2:
#             return '我被迫中断了'
#         else:
#             yield i
#
# def wrap_my_generator(generator):  #定义一个包装“生成器”的生成器，它的本质还是生成器
#     result=yield from generator    #自动触发StopIteration异常，并且将return的返回值赋值给yield from表达式的结果，即result
#     print(result)
#
# def main(generator):
#     for j in generator:
#         print(j)
#
# g=my_generator()
# wrap_g=wrap_my_generator(g)
# main(wrap_g)  #调用
'''运行结果为：
0
1
我被迫中断了
'''
# 三、yield from的用法示例
## 解释：其实yield from最重要的作用就是提供了一个“数据传输的管道”，下面通过一个简单的例子加以说明为什么是管道：
# def average():
#     total = 0.0  # 数字的总和
#     count = 0  # 数字的个数
#     avg = None  # 平均值
#     while True:
#         num = yield avg
#         total += num
#         count += 1
#         avg = total / count
#
#
# def wrap_average(generator):
#     yield from generator
#
#
# # 定义一个函数，通过这个函数向average函数发送数值
# def main(wrap):
#     print(next(wrap))  # 启动生成器
#     print(wrap.send(10))  # 10
#     print(wrap.send(20))  # 15
#     print(wrap.send(30))  # 20
#     print(wrap.send(40))  # 25
#
#
# g = average()
# wrap = wrap_average(g)
# main(wrap)
'''
从上面我们可以发现，调用方发送的数据是发给wrap_average的，怎么依然到了生成器函数average里面呢？这就是“数据传输管道的作用”。即主函数调用方main把各个value传给grouper ，而这个传入的值最终到达averager函数中； grouper并不知道传入的是什么值，因为从上面的代码看出，wrap_average里面完全没有处理这个值的任何代码！
'''

