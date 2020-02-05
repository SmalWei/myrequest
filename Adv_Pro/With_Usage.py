#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : With_Usage.py
@Time    : 2020/1/2 22:04
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  只是copy  尚未研究
"""
#  上下文管理器史实现了 _enter_和_exit_的两个方法
# class T:
#     def __enter__(self):
#         print('T.__enter__')
#         return '我是__enter__的返回值'
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('T.__exit__')
#
# with T() as t:
#     print(t)
# import sys
#
# class HaHa:
#
#     def __init__(self, word):
#         self.word = word
#
#     def reverse_write(self, text):
#         self.original_write(text[::-1])
#
#     def __enter__(self):
#         self.original_write = sys.stdout.write
#         sys.stdout.write = self.reverse_write
#         return self.word
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         sys.stdout.write = self.original_write
#         return True
# obj1 = HaHa('你手机拿反了')
# with obj1 as content:
#     print('哈哈镜花缘')
#     print(content)
# print('#### with 执行完毕后，再输出content: ####')
# print(content)
import sys
import contextlib

@contextlib.contextmanager
def WoHa(n):
    original_write = sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write
    yield n
    sys.stdout.write =  original_write
    return True

obj1 = WoHa('你手机拿反了')
with obj1 as content:
    print('哈哈镜花缘')
    print(content)
print('#### with 执行完毕后，在输出content: ####')
print(content)