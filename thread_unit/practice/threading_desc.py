# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     threading_desc.py
# Author:      Jakiro
# Datetime:    2022/4/25 14:14
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# threading模块介绍：
#
# threading模块是python中专门提供用来做多线程编程的模块。
# threading模块中最常用的类是Thread。以下看一个简单的多线程程序：
# 查看线程数：
#       使用threading.enumerate()函数便可以看到当前线程的数量。
#
# 查看当前线程的名字：
#        使用threading.current_thread()可以看到当前线程的信息。


import threading
import time
from decorator.time_fuc_dec import timeit


def coding():
    for x in range(3):
        print(f'{x}正在写代码')
        time.sleep(1)


def drawing():
    for x in range(3):
        print(f'{x}正在画图')
        time.sleep(1)


@timeit()
def single_thread():
    coding()
    drawing()


@timeit()
def multi_threading():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    print(threading.enumerate(),'\n', threading.current_thread())
    # # [<_MainThread(MainThread, started 4655588864)>, <Thread(Thread-1, started 123145550004224)>, <Thread(Thread-2, started 123145555259392)>]
    #    <_MainThread(MainThread, started 4655588864)>

if __name__ == '__main__':
    # single_thread()
    # 0正在写代码
    # 1正在写代码
    # 2正在写代码
    # 0正在画图
    # 1正在画图
    # 2正在画图
    # None_single_thread duration 6.0214128494262695
    multi_threading()  # 主线程执行完 直接退出了  等子线程完成


    # 0正在写代码
    # 0正在画图None_multi_threading duration 0.0003600120544433594
