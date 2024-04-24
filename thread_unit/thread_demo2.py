# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     thread_demo2.py
# Author:      Jakiro
# Datetime:    2022/1/20 20:00
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
#
# _thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
#
# threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
#
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
#
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。


import threading
import time


# exitFlag = 0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.delay, 5)
#         print("退出线程：" + self.name)
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# # 创建新线程
# thread1 = MyThread(1, "Thread-1", 1)
# thread2 = MyThread(2, "Thread-2", 1)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join(10)
#
# print("退出主线程")
#
# thread2.join()
# print('2执行完成')


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, delay):
        threading.Thread.__init__(self)
        self.name = name

        self.delay = delay

    def run(self):
        print('线程开始' + self.name)
        print_time(self.name,self.delay,5)
        print('线程结束' + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        # if
        time.sleep(delay)
        print(f'{thread_name}:{time.ctime(time.time())}')
        counter -= 1

thread1 = MyThread(1,'thread_1',1)
thread2 = MyThread(2,'thread_2',2)
thread1.start()
thread2.start()
thread1.join(10)
thread2.join(20)
print('退出主线程')