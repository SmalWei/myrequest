#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : Async_IO_Base_5.py
@Time    : 2020/1/2 18:32
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  声明：本文针对的是python3.4以后的版本的，因为从3.4开始才引入asyncio，后面的3.5 3.6 3.7版本是向前兼容的，只不过语法上面有稍微的改变。比如在3.4版本中使用@asyncio.coroutine装饰器和yield from语句，但是在3.5以后的版本中使用async、await两个关键字代替，虽然语法上稍微有所差异，但是原理是一样的。本文用最通俗的语言解释了pythonasyncio背后的一些核心概念，简要解析了asyncio的设计架构，并给出了使用python进行asyncio异步编程的一般模板。
"""
# 一、一些最重要的概念
# 1、协程（coroutine）——本质就是一个函数
#  判断一个函数是不是协程函数的办法：
#  asyncio.iscoroutine（obj）和asyncio.iscoroutinefunction(func)加以判断，返回true，则是。
# （1）result = yield from future
# 作用一：返回future的结果。什么是future？后面会讲到。当协程函数执行到这一句，协程会被悬挂起来，知道future的结果被返回。如果是future被中途取消，则会触发CancelledError异常。由于task是future的子类，后面也会介绍，关于future的所有应用，都同样适用于task
# （2）result = yield from coroutine
# 等候另一个协程函数返回结果或者是触发异常 
# （3）result= yield from task
# 返回一个task的结果
# （4）return expression
# 作为一个函数，他本身也是可以返回某一个结果的
# （5）raise exception 
#  抛出异常
# 2、事件循环——event_loop
#  协程函数不像是普通函数那样直接运行的，必须添加到事件循环中去，然后由事件循环去运行，单独
# 运行协程函数是不会有结果的
#                                         import time
#                                         import asyncio
#                                         async def say_after_time(delay,what):
#                                                 await asyncio.sleep(delay)
#                                                 print(what)
#
#                                         async def main():
#                                                 print(f"开始时间为： {time.time()}")
#                                                 await say_after_time(1,"hello")
#                                                 await say_after_time(2,"world")
#                                                 print(f"结束时间为： {time.time()}")
#                                                loop=asyncio.get_event_loop()    #创建事件循环对象
#                                                #loop=asyncio.new_event_loop()   #与上面等价，创建新的事件循环
#                                                loop.run_until_complete(main())  #通过事件循环对象运行协程函数
#                                                loop.close()
# 注意：在python3.6版本中，如果我们单独像执行普通函数那样执行一个协程函数，
# 只会返回一个coroutine对象，
# （1）获取事件循环对象的几种方式
#  事件循环的简单介绍
# loop=asyncio.get_running_loop() 返回（获取）在当前线程中正在运行的事件循环，如果没有正在运行的事件循环，则会显示错误；它是python3.7中新添加的
# loop=asyncio.get_event_loop() 获得一个事件循环，如果当前线程还没有事件循环，则创建一个新的事件循环loop；
# loop=asyncio.set_event_loop(loop) 设置一个事件循环为当前线程的事件循环；
# loop=asyncio.new_event_loop() 创建一个新的事件循环
# （2） 通过事件循环运行函数的两种方式：
#  方式一：创建事件循环对象loop ：即：asyncio.get_event_loop()。通过事件循环运行协成函数
#  方式二：直接通过asyncio.run(函数名称)运行协程函数，但要注意的是：首先run函数是python3.7
# 才添加的前面的版本没有，这个run函数总是会创建一个新的时间循环并在run结束后关闭事件循环，所以
# 如果在同一个线程中已经有了一个事件循环，则不能使用这个函数了，因为同一个线程中，不能有两个事件循环，
# 而且这个run函数不能同时运行两次，因为他已经创建一个了，
#    事件循环的理解：
    # 线程一直在各个协程方法之间永不停歇的游走，遇到一个yield，await就悬挂起来，然后又走到另一个方法，
    # 一次进行下去，直到事件循环所有的方法执行完毕，实际上loop是BaseEventLoop的一个实例，我们可以查看定义，它到底有那些方法可以调用
#  (3) 什么是awaitable对象，即可暂停等待的对象
#  有三类对象是可等待的，即：coroutines，Tasks，Futures
#  coroutine:本质是一个函数，一个前面的生成器yield,yield from 为基础
#  Tasks：任务，就是要完成某件事情，其实就是对协程函数进一步封装
#  Future:它是一个更底层的概念，它代表一个异步操作的最终结果，因为一步操作一般用于耗时操作，结果不会理解得到，会在将来得到异步运行的结果，故命名为Future
#  （4）Task用来并发调度的协程，即对协程函数进行进一步包装，那为什么还需要包装，因为淡村的协程仅仅是一个函数而已
#  将其包装成任务，，任务是可以包含各种状态的，异步编程最终要的就是对异步操作状态的把控
#         a.task = asyncio.create_task(coro())
#         b.task = asyncio.ensure_future(coro())
#         也可以使用
#         loop.create_future()
#         loop.create_task(coro)
#         也是可以的。
#         备注：关于任务的详解，会在后面的系列文章继续讲解，本文只是概括性的说明\
#         （2）获取某一个任务的方法：
#         方法一：task=asyncio.current_task(loop=None)
#         返回在某一个指定的loop中，当前正在运行的任务，如果没有任务正在运行，则返回None；
#         如果loop为None，则默认为在当前的事件循环中获取，
#         方法二：asyncio.all_tasks(loop=None)
#         返回某一个loop中还没有结束的任务
# (5.)什么是future？
# Future是一个较低层的可等待（awaitable）对象，他表示的是异步操作的最终结果，当一个Future对象被等待的时候，协程会一直等待，直到Future已经运算完毕。
# Future是Task的父类，一般情况下，已不用去管它们两者的详细区别，也没有必要去用Future，用Task就可以了，
# 返回 future 对象的低级函数的一个很好的例子是 loop.run_in_executor().
# 二、asyncio的基本架构
# 前面介绍了asyncio里面最为核心的几个概念，如果能够很好地理解这些概念，对于学习协程是非常有帮助的，但是按照我个人的风格，我会先说asyncio的架构，理解asyncio的设计架构有助于更好地应用和理解。
# asyncio分为高层API和低层API，我们都可以使用，就像我前面在讲matplotlib的架构的时候所讲的一样，我们前面所讲的Coroutine和Tasks属于高层API，而Event Loop 和Future属于低层API。当然asyncio所涉及到的功能远不止于此，我们只看这么多。下面是是高层API和低层API的概览：
# High-level APIs
#         Coroutines and Tasks（本文要写的）
#         Streams
#         Synchronization Primitives
#         Subprocesses
#         Queues
#         Exceptions
# Low-level APIs
#         Event Loop（下一篇要写的）
#         Futures
#         Transports and Protocols
#         Policies
#         Platform Support
# 所谓的高层API主要是指那些asyncio.xxx()的方法，
# 1、常见的一些高层API方法
# （1）运行异步协程
#         asyncio.run(coro, *, debug=False)  #运行一个一步程序，参见上面
# （2）创建任务
#         task=asyncio.create_task(coro)  #python3.7  ,参见上面
#         task = asyncio.ensure_future(coro()) 
# （3）睡眠
#         await asyncio.sleep(delay, result=None, *, loop=None)
#         这个函数表示的是：当前的那个任务（协程函数）睡眠多长时间，而允许其他任务执行。这是它与time.sleep()的区别，time.sleep()是当前线程休息，注意他们的区别哦。
#         另外如果提供了参数result，当当前任务（协程）结束的时候，它会返回；
#         loop参数将会在3.10中移除，这里就不再说了。
# （4）并发运行多个任务
#         await asyncio.gather(*coros_or_futures, loop=None, return_exceptions=False)
#         它本身也是awaitable的。
#         *coros_or_futures是一个序列拆分操作，如果是以个协程函数，则会自动转换成Task。
#         当所有的任务都完成之后，返回的结果是一个列表的形式，列表中值的顺序和*coros_or_futures完成的顺序是一样的。
#         return_exceptions:
#                                 False,这是他的默认值，第一个出发异常的任务会立即返回，然后其他的任务继续执行；
#                            True，对于已经发生了异常的任务，也会像成功执行了任务那样，等到所有的任务执行结束一起将错误的结果返回到最终的结果列表里面。
# 如果gather()本身被取消了，那么绑定在它里面的任务也就取消了。
# （5）防止任务取消
#         await asyncio.shield(*arg, *, loop=None)
#         它本身也是awaitable的。顾名思义，shield为屏蔽、保护的意思，即保护一个awaitable 对象防止取消，一般情况下不推荐使用，而且在使用的过程中，最好使用try语句块更好。
#                         try:
#                             res = await shield(something())
#                         except CancelledError:
#                             res = None
# 6）设置timeout——一定要好好理解
#         await asyncio.wait_for(aw, timeout, *, loop=None)
#         如果aw是一个协程函数，会自动包装成一个任务task。参见下面的例子：
#                         import asyncio
#                         async def eternity():
#                             print('我马上开始执行')
#                             await asyncio.sleep(3600)  #当前任务休眠1小时，即3600秒
#                             print('终于轮到我了')
#
#                         async def main():
#                             # Wait for at most 1 second
#                             try:
#                                 print('等你3秒钟哦')
#                                 await asyncio.wait_for(eternity(), timeout=3)  #休息3秒钟了执行任务
#                             except asyncio.TimeoutError:
#                                 print('超时了！')
#                           asyncio.run(main())
# 总结：当异步操作需要执行的时间超过waitfor设置的timeout，就会触发异常，所以在编写程序的时候，如果要给异步操作设置timeout，一定要选择合适，如果异步操作本身的耗时较长，而你设置的timeout太短，会涉及到她还没做完，就抛出异常了。
# （7）多个协程函数时候的等候
#         await asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
#         与上面的区别是，第一个参数aws是一个集合，要写成集合set的形式，比如：
#         {func（），func（），func3（）}
#         表示的是一系列的协程函数或者是任务，其中协程会自动包装成任务。事实上，写成列表的形式也是可以的。
#         注意：该函数的返回值是两个Tasks/Futures的集合
# *********************************************************************************************未完待续***********************************************************************************
# 三、asyncio异步编程的基本模板
# （1）例子一：无参数、无返回值
#                                                 import asyncio
#                                                 import time
#                                                 a=time.time()
#                                                 async def hello1():
#                                                     print("Hello world 01 begin")
#                                                     await asyncio.sleep(3)  #模拟耗时任务3秒
#                                                     print("Hello again 01 end")
#
#                                                 async def hello2():
#                                                     print("Hello world 02 begin")
#                                                     await asyncio.sleep(2)   #模拟耗时任务2秒
#                                                     print("Hello again 02 end")
#
#                                                 async def hello3():
#                                                     print("Hello world 03 begin")
#                                                     await asyncio.sleep(4)   #模拟耗时任务4秒
#                                                     print("Hello again 03 end")
#
#                                                 loop = asyncio.get_event_loop()                #第一步：创建事件循环
#                                                 tasks = [hello1(), hello2(),hello3()]          #第二步:将多个协程函数包装成任务列表
#                                                 loop.run_until_complete(asyncio.wait(tasks))   #第三步：通过事件循环运行
#                                                 loop.close()                                   #第四步：取消事件循环
'''
                                                        运行结果为：
                                                        Hello world 02 begin
                                                        Hello world 03 begin
                                                        Hello world 01 begin
                                                        Hello again 02 end
                                                        Hello again 01 end
                                                        Hello again 03 end
'''
# （2）例子二：有参数、有返回值
#                                                 import asyncio
#                                                 import time
#
#
#                                                 async def hello1(a,b):
#                                                     print("Hello world 01 begin")
#                                                     await asyncio.sleep(3)  #模拟耗时任务3秒
#                                                     print("Hello again 01 end")
#                                                     return a+b
#
#                                                 async def hello2(a,b):
#                                                     print("Hello world 02 begin")
#                                                     await asyncio.sleep(2)   #模拟耗时任务2秒
#                                                     print("Hello again 02 end")
#                                                     return a-b
#
#                                                 async def hello3(a,b):
#                                                     print("Hello world 03 begin")
#                                                     await asyncio.sleep(4)   #模拟耗时任务4秒
#                                                     print("Hello again 03 end")
#                                                     return a*b
#
#                                                 loop = asyncio.get_event_loop()                #第一步：创建事件循环
#                                                 task1=asyncio.ensure_future(hello1(10,5))
#                                                 task2=asyncio.ensure_future(hello2(10,5))
#                                                 task3=asyncio.ensure_future(hello3(10,5))
#                                                 tasks = [task1,task2,task3]                    #第二步:将多个协程函数包装成任务列表
#                                                 loop.run_until_complete(asyncio.wait(tasks))   #第三步:通过事件循环运行
#                                                 print(task1.result())                               #并且在所有的任务完成之后，获取异步函数的返回值
#                                                 print(task2.result())
#                                                 print(task3.result())
#                                                 loop.close()
'''
运行结果为：
                                                        Hello world 01 begin
                                                        Hello world 02 begin
                                                        Hello world 03 begin
                                                        Hello again 02 end
                                                        Hello again 01 end
                                                        Hello again 03 end
                                                        15
                                                        5
                                                        50
'''
# （3）总结：四步走（针对python3.7之前的版本）
# 第一步·：构造事件循环
#                                 loop=asyncio.get_running_loop() #返回（获取）在当前线程中正在运行的事件循环，如果没有正在运行的事件循环，则会显示错误；它是python3.7中新添加的
#                                 loop=asyncio.get_event_loop() #获得一个事件循环，如果当前线程还没有事件循环，则创建一个新的事件循环loop；
#                                 loop=asyncio.set_event_loop(loop) #设置一个事件循环为当前线程的事件循环；
#                                 loop=asyncio.new_event_loop()  #创建一个新的事件循环
# 第二步：将一个或者是多个协程函数包装成任务Task
#高层API
                                                # task = asyncio.create_task(coro(参数列表))   # 这是3.7版本新添加的
                                                # task = asyncio.ensure_future(coro(参数列表))
                                                # #低层API
                                                # loop.create_future(coro)
                                                # loop.create_task(coro)

'''需要注意的是，在使用Task.result()获取协程函数结果的时候，使用asyncio.create_task()却会显示错
但是使用asyncio.ensure_future却正确，本人暂时不知道原因，哪位大神知道，望告知，不胜感激！'''

# 第三步：通过事件循环运行
#                                 loop.run_until_complete(asyncio.wait(tasks))  #通过asyncio.wait()整合多个task
#                                 loop.run_until_complete(asyncio.gather(tasks))  #通过asyncio.gather()整合多个task
#                                 loop.run_until_complete(task_1)  #单个任务则不需要整合
#                                 loop.run_forever()  #但是这个方法在新版本已经取消，不再推荐使用，因为使用起来不简洁
'''
                                使用gather或者wait可以同时注册多个任务，实现并发,但他们的设计是完全不一样的，在前面的2.1.(4)中已经讨论过了，主要区别如下：
                                （1）参数形式不一样
                                gather的参数为 *coroutines_or_futures,即如这种形式
                                      tasks = asyncio.gather(*[task1,task2,task3])或者
                                      tasks = asyncio.gather(task1,task2,task3)                             
                                      loop.run_until_complete(tasks)
                                wait的参数为列表或者集合的形式，如下
                                      tasks = asyncio.wait([task1,task2,task3])                               
                                      loop.run_until_complete(tasks)
                                （2）返回的值不一样
                                gather的定义如下，gather返回的是每一个任务运行的结果，
                                      results = await asyncio.gather(*tasks)                              
                                wait的定义如下,返回dones是已经完成的任务，pending是未完成的任务，都是集合类型
                                 done, pending = yield from asyncio.wait(fs)                                
                                （3）后面还会讲到他们的进一步使用
                                简单来说：async.wait会返回两个值:done和pending，done为已完成的协程Task，pending为超时未完成的协程Task，需通过future.result调用Task的result。而async.gather返回的是已完成Task的result。
'''
# 第四步：关闭事件循环
#                                                         loop.close()

'''
                                                以上示例都没有调用 loop.close，好像也没有什么问题。所以到底要不要调 loop.close 呢？
                                                简单来说，loop 只要不关闭，就还可以再运行：
                                                
                                                loop.run_until_complete(do_some_work(loop, 1))
                                                loop.run_until_complete(do_some_work(loop, 3))
                                                loop.close()
                                                但是如果关闭了，就不能再运行了：
                                                
                                                loop.run_until_complete(do_some_work(loop, 1))
                                                loop.close()
                                                loop.run_until_complete(do_some_work(loop, 3))  # 此处异常
                                                
                                                建议调用 loop.close，以彻底清理 loop 对象防止误用

'''
# 四、协程编程的优点：
                                        # 1、无cpu分时切换线程保存上下文问题（协程上下文怎么保存）
                                        # 2、遇到io阻塞切换（怎么实现的）
                                        # 3、无需共享数据的保护锁（为什么）
                                        # 4、系列文章下篇预告——介绍低层的API，事件循环到底是怎么实现的以及future类的实现。

