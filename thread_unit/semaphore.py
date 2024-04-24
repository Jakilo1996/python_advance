# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     semaphore.py
# Author:      Jakiro
# Datetime:    2022/2/18 13:54
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 信号量（Python Semaphore对象）
# Semaphore对象内部管理一个计数器，该计数器由每个acquire()调用递减，并由每个release()调用递增。计数器永远不会低于零，当acquire()发现计数器为零时，线程阻塞，等待其他线程调用release()。
# Semaphore对象支持上下文管理协议。
#
# 此计数器是线程共享的，每个线程都可以操作此计数器。
#
# 方法：
#
# Semaphore(value=1)：创建一个计数器对象，默认值为1。
#
# acquire(blocking=True, timeout=None)
# 获取信号，使计数器递减1。
# 当blocking=True时：如果调用时计数器大于零，则将其减1并立即返回。如果在调用时计数器为零，则阻塞并等待，直到其他线程调用release()使其大于零。这是通过适当的互锁来完成的，因此如果多个acquire()被阻塞，release()将只唤醒其中一个，这个过程会随机选择一个，因此不应该依赖阻塞线程的被唤醒顺序。返回值为True。
# 当blocking=False时，不会阻塞。如果调用acquire()时计数器为零，则会立即返回False.
# 如果设置了timeout参数，它将阻塞最多timeout秒。如果在该时间段内没有获取锁，则返回False，否则返回True。
#
# release()
# 释放信号，使计数器递增1。当计数器为零并有另一个线程等待计数器大于零时，唤醒该线程。
#
# 总结：信号量基于计数器来实现线程同步，此计数器为线程之间共享，利用信号量，你可以实现限量线程同时访问临界区，这句话怎么理解，因为你可以设置不同大小的value即可实现。
#
# 来看下面的代码：

import time
import threading

# def foo():
#     time.sleep(2)
#     print(f'ok{time.ctime()}',end='\n')
#
# for i in range(20):
#     thread_1 = threading.Thread(target=foo,args=())
#     thread_1.start()

# 可以看到，程序会在很短的时间内生成20个线程来打印一句话。
#
# 这时候就可以为这段程序添加一个信号量的计数器功能，来限制一个时间点内的线程数量。
#
# 代码如下：


se_1 = threading.Semaphore(2) ### 添加一个计数器


def foo():
    se_1.acquire()  ### 计数器获得锁
    time.sleep(2)
    print(f'ok{time.ctime()}', end='\n')
    se_1.release() # 计数器释放锁


for i in range(20):
    thread_1 =threading.Thread(target=foo)
    thread_1.start()

# 可以看到每隔两秒钟就有五条信息产生，对应了五个线程，我们实现了限量线程访问临界区。