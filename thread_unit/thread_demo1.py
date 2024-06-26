# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     thread_demo1.py
# Author:      Jakiro
# Datetime:    2022/1/20 19:44
# Description: python多线程
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 多线程类似于同时执行多个不同程序，多线程运行有如下优点：
#
# 使用线程可以把占据长时间的程序中的任务放到后台去处理。
# 用户界面可以更加吸引人，比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度。
# 程序的运行速度可能加快。
# 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。
# 每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
#
# 每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
#
# 指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。
#
# 线程可以被抢占（中断）。
# 在其他线程正在运行时，线程可以暂时搁置（也称为睡眠） -- 这就是线程的退让。
# 线程可以分为:
#
# 内核线程：由操作系统内核创建和撤销。
# 用户线程：不需要内核支持而在用户程序中实现的线程。
# Python3 线程中常用的两个模块为：
#
# _thread
# threading(推荐使用)
# thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。


# Python中使用线程有两种方式：函数或者用类来包装线程对象。
# 函数式：调用 _thread 模块中的start_new_thread()函数来产生新线程。语法如下
# _thread.start_new_thread ( function, args[, kwargs] )
# function - 线程函数。
# args - 传递给线程函数的参数,他必须是个tuple类型。
# kwargs - 可选参数。


import _thread
import time


# 定义一个输出时间函数
def print_time(thread_name, delay_time):
    count = 0
    while count < 5:
        time.sleep(delay_time)
        count += 1
        time1 = time.ctime(time.time())
        print(f'{thread_name}:{time1}')

# print('a')

# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2))
    _thread.start_new_thread(print_time, ("Thread-2", 4))
except:
    print('无法启动线程')
