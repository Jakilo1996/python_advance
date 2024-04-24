# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     event.py
# Author:      Jakiro
# Datetime:    2022/2/21 14:53
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 1：事件机制共享队列：
#
# 利用消息机制在两个队列中，通过传递消息，实现可以控制的生产者消费者问题
# 要求：readthread读时，writethread不能写；writethread写时，readthread不能读。
# 基本方法 时间类（Event）
# set：设置事件。将标志位设为True。
# wait：等待事件。会将当前线程阻塞，直到标志位变为True。
# clear：清除事件。将标志位设为False。
# set() clear() 函数的交替执行 也就是消息传递的本质


# 事件消息机制
import queue
import threading
import random
from threading import Event
from threading import Thread


class WriteThread(Thread):
    def __init__(self, q, wt, rt):
        super().__init__();
        self.queue = q;
        self.rt = rt;
        self.wt = wt;

    def run(self):
        data = [random.randint(1, 100) for _ in range(0, 10)]
        self.queue.put(data)
        print('wt写队列',data)
        self.rt.set() # 发送读事件
        print('wt通知读')
        print('wt等待写')
        self.wt.wait();
        print('wt收到写事件')
        self.wt.clear();


class ReadThread(Thread):
    def __init__(self, q, wt, rt):
        super().__init__();
        self.queue = q;
        self.rt = rt;
        self.wt = wt;

    def run(self):
        while True:
            self.rt.wait(); # 等待写事件
            print("rt收到读事件")
            print(f'rt开始读{self.queue.get()}')
            print('rt发送写事件')
            self.wt.set();
            self.wt.clear()


que = queue.Queue()
rt_event = Event()
wt_event = Event()
wt = WriteThread(q=que, wt=wt_event, rt=rt_event)
rt = ReadThread(q=que, wt=wt_event, rt=rt_event)

wt.start()
rt.start()


# output
# wt写队列 [20, 96, 41, 6, 70, 2, 99, 27, 92, 30]
# wt通知读
# wt等待写
# rt收到读事件
# rt开始读[20, 96, 41, 6, 70, 2, 99, 27, 92, 30]
# rt发送写事件
# rt收到读事件
# wt收到写事件