#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : unpack_in_fun.py
@Time    : 2020/1/2 19:56
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  请更换这个文件的描述信息：作用以及目的
"""
def func(a,b,c):
    print(a,b,c)
func(1,2,3)
func(*[1,2,3])
func(*'abc')
func(*{"a":1,"b":2,"c":3})
func(**{"a":1,"b":2,"c":3})
#  看到了吗？和上面例子的区别是多了一个星号，结果完全不一样，原因是什么？ 答案是 ** 符号作用的对象是字典对象，它会自动解包成关键字参数 key=value 的格式：
print(*[1],*[1,2,3],3)#  从3.5开始，可以使用任务的多个解包操作
print([*range(4,),4])
print({"x":1,**{"y":2}})