# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     process_communication1.py
# Author:      Jakiro
# Datetime:    2022/4/24 13:36
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# queue用法及进程通信


# from queue import Queue

# 进程之间数据都是不共享的，因此想要在两个进程之间使用相同的数据，那么这时候就需要使用进程间的通信，
# 进程间通信有多种方式。两种，第一种是管道（Pipe）、第二种是队列（Queue）。以下讲解下使用Queue的通信。
#
# Queue的一些常用方法的   详解在threading模块
#
# Queue(n)：初始化一个消息队列，并指定这个队列中最多能够容纳多少条消息。
# put(obj,[block[,timeout]])：推入一条消息到这个队列中。默认是阻塞的，也就是说如果这个消息队列中已经满了，那么会会一直等待，将这个消息添加到消息队列中。
# timeout可以指定这个阻塞最长的时间，如果超过这个时间还是满的，就会抛出异常。 queue.full
# put_nowait() ：非阻塞的推入一条消息，如果这个队列已经满了，那么会立马抛出异常。
# qsize()：获取这个消息队列消息的数量。
# full()：判断这个消息队列是否满了。
# empty()：判断这个消息队列是否空了。
# get([block[,timeout]])：获取队列中的一条消息，然后将其从队列中移除，block默认为True。如果设置block为False，那么如果没值，会立马抛出异常。timeout指定如果多久没有获取到值后会抛出异常。


# # 初始化一个Queue对象 最多能存放3条信息
# q = Queue(3)
#
# # 存放第一条消息
# q.put('message1')
# # 存放第二条消息
# q.put('message2')
#
# # 判断这个队列中是否已经满了
# print(q.full())
#
# # 存放第三条信息
# q.put('message3')
#
# # 判断队列是否已经满了
# print(q.full())
#
# # 因为如果队列已经满了，那么再put信息就会报错
# try:
#     q.put_nowait('message4')
# except:
#     print('队列已满')
#
# # 获取队列的第一组数据
# print(q.get())

#  在进程中使用queue  只能使用包中自带的类  使用自带的Queue不生效
from multiprocessing import Process,Queue
import time


def read_func(q):
    # 已阻塞的方式获得数据
    value = q.get(True)
    print(f'read value {value}')
    time.sleep(1)


def write_func(q):
    for x in ['m1', 'm2', 'm3', 'm4']:
        # 最好设置等待时间，不然 写不进去了也会一直等待
        q.put(x,timeout=3)
        time.sleep(1)


if __name__ == '__main__':
    #  如果小于4  由于数据写不进去 会一直等待
    q = Queue(4)
    process_w = Process(target=write_func,args=(q,))
    process_r = Process(target=read_func,args=(q,))

    process_w.start()
    process_w.join()
    process_r.start()

