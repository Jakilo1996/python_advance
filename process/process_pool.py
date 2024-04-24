# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     process_pool.py
# Author:      Jakiro
# Datetime:    2022/4/21 21:15
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 进程池
# multiprocessing模块中有一个类Pool，这个类相当于一个池，专门用来存储进程。
# Pool的__init__可以传递一个参数，这个参数指定这个进程池中同一时刻最多只能拥有多少个进程。
# 并且，在使用进程池，父进程不会等待子进程池中的子进程执行完毕后退出，
# 而是当父进程中的代码执行完毕以后会立即退出。相关的示例代码如下：
# 1、apply() — 该函数用于传递不定参数，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不在出现），函数原型如下
# apply(func, args=(), kwds={})
#
# 2、apply_async — 与apply用法一致，但它是非阻塞的且支持结果返回后进行回调，函数原型如下：
# apply_async(func[, args=()[, kwds={}[, callback=None]]])
#
# 3、map() — Pool类中的map方法，与内置的map函数用法基本一致，它会使进程阻塞直到结果返回，函数原型如下：
#
# map(func, iterable, chunksize=None)
# 4、map_async() — 与map用法一致，但是它是非阻塞的。其有关事项见apply_async，函数原型如下：
#
# map_async(func, iterable, chunksize, callback)
# 5、close() — 关闭进程池（pool），使其不在接受新的任务。
#
# 6、terminal() — 结束工作进程，不在处理未处理的任务。
#
# 7、join() — 主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。

from multiprocessing import Process, Pool
import os
import time

import sys

# c = lambda: sys.stdout.write('Hello,World\n')


def worker(num):
    for x in range(5):
        print(f'num:{num},pid:{os.getpid()}')
        time.sleep(1)
    # return lambda :sys.stdout.write('Hello,World\n')
    return num
    #
a = worker(2)
print(a)

if __name__ == '__main__':
    # 这个池子中同一时刻最多只有3个进程
    # res =  []
    pool = Pool(3)
    # for x in range(10):
    #     res=pool.apply_async(worker,(x,))
    # pool.apply_async(lambda: sys.stdout.write('Hello,World\n'))
    #
    # res = [pool.apply_async(c) for i in range(3)]

    res = [pool.apply_async(worker, (i,)) for i in range(3)]
    # 关闭进程池，不能再添加新进程了
    pool.close()
    # 主进程把子进程添加到进程池后，不会等待进程池中其他的子进程都执行完毕后再退出
    # 而是当主进程的代码执行完毕后会立刻退出，因此如果这个地方没有join，那么子进程将得不到执行   不join()  不执行子进程
    pool.join()
    # 通过get方法拿进程函数的执行结果
    print([r.get() for r in res])
    # output
    # 有3个子进程同时执行打印语句
    # 老进程执行的时候，新进程进入执行
