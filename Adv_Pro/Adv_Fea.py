#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : Adv_Fea.py
@Time    : 2020/1/2 21:41
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  请更换这个文件的描述信息：作用以及目的
"""
#  使用generations
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
# for i in fib():
#     if i>1000:
#         break
#     print(i)

# collections的使用
# （1）
    # from collections import Counter
    # a = Counter('blue')
    # b = Counter('yellow')
    # print(a)
    # print(b)
    # print((a + b).most_common(3))
    # print(b)
    # print((a + b).most_common(3))
# （2） 构建一棵树
#     from collections import defaultdict
#     import json
#     my_dict = defaultdict(lambda :"Default Value")
#     my_dict['a'] = 42
#     print(my_dict['a'])
#     print(my_dict['b'])
#     def tree():
#         """
#         :return:
#         """
#         return defaultdict(tree)
#     root = tree()
#     root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
#     root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
#     root['Page']['Java'] = None
#     print(json.dumps(root, indent=4))
#  itertools包的使用
#  （1） 创建一个生成序列
#     from itertools import permutations
#     for p in permutations([1,2,3]):
#         print(p)
# (2) 将多个可迭代对象合并在一起
#     from itertools import chain
#     for c in chain(range(3),range(12,15)):
#         print(c)
# Decorators装饰器
# def cache(function):
#     cached_values = {}  # Contains already computed values
#     def wrapping_function(*args):
#         if args not in cached_values:
#             # Call the function only if we haven't already done it for those parameters
#             cached_values[args] = function(*args)
#         return cached_values[args]
#     return wrapping_function
#
# @cache
# def fibonacci(n):
#     print('calling fibonacci(%d)' % n)
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print([fibonacci(n) for n in range(1, 9)])
# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     print('calling fibonacci(%d)' % n)
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print([fibonacci(n) for n in range(1, 9)])
# from time import time
#
# class Timer():
#     def __init__(self, message):
#         self.message = message
#
#     def __enter__(self):
#         self.start = time()
#         return None  # could return anything, to be used like this: with Timer("Message") as value:
#
#     def __exit__(self, type, value, traceback):
#         elapsed_time = (time() - self.start) * 1000
#         print(self.message.format(elapsed_time))
#
# with Timer("Elapsed time to compute some prime numbers: {}ms"):
#     primes = []
#     for x in range(2, 500):
#         if not any(x % p == 0 for p in primes):
#             primes.append(x)
#     print("Primes: {}".format(primes))