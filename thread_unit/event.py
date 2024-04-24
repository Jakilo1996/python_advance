# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     event.py
# Author:      Jakiro
# Datetime:    2022/2/18 14:11
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

#
# 事件对象管理一个内部标志，通过set()方法将其设置为True，并使用clear()方法将其设置为False。wait()方法阻塞，直到标志为True。该标志初始为False。
#
# 方法：
# is_set()
# 当且仅当内部标志为True时返回True。
#
# set()
# 将内部标志设置为True。所有等待它成为True的线程都被唤醒。当标志保持在True的状态时，线程调用wait()是不会阻塞的。
#
# clear()
# 将内部标志重置为False。随后，调用wait()的线程将阻塞，直到另一个线程调用set()将内部标志重新设置为True。
#
# wait(timeout=None)
# 阻塞直到内部标志为真。如果内部标志在wait()方法调用时为True，则立即返回。否则，则阻塞，直到另一个线程调用set()将标志设置为True，或发生超时。
# 该方法总是返回True，除非设置了timeout并发生超时。
#
# 总结：Event是一个能在多线程中共用的对象，这和信号量是相同的，信号量基于计数器，而event基于共享标志位，一开始它包含一个为 False的信号标志，一旦在任一一个线程里面把这个标记改为 True，那么所有的线程都会看到这个标记变成了 True。看到这里，event要么把共享此标志的线程全部给阻塞，要么大家一起运行。
#
# 设想这样一个场景：
#
# 你创建了10个子线程，每个子线程分别爬一个网站，一开始所有子线程都是阻塞等待。一旦某个事件发生：例如有人在网页上点了一个按钮，或者某人在命令行输入了一个命令，10个爬虫同时开始工作。

import threading
import time

event = threading.Event()


class SpiderThread(threading.Thread):
    def __init__(self, thread_n, event):
        threading.Thread.__init__(self)
        self.thread_n = thread_n
        self.event = event

    def run(self):
        print(f'{self.thread_n}已就绪')
        self.event.wait()
        print(f'信号量变为Ture!!{self.thread_n}开始运行',end='\n')


for n in range(10):
    current_thread = SpiderThread(n,event)
    current_thread.start()

# input('按下回车')
print('按下回车')
print(event.is_set())
event.set()
print(event.is_set())
time.sleep(3)
event.clear()
a_thread = SpiderThread(11,event)
a_thread.start()
print(event.is_set())