# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     threading_class.py
# Author:      Jakiro
# Datetime:    2022/4/25 15:39
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 继承自threading.Thread类：
# 为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，然后实现run方法，
# 线程就会自动运行run方法中的代码。示例代码如下：


import threading
import time
from decorator.time_fuc_dec import timeit


class CodingThread(threading.Thread):
    @timeit()
    def run(self):
        for x in range(3):
            print(f'{threading.current_thread()}正在编码')
            time.sleep(1)


class DrawingThread(threading.Thread):
    @timeit()
    def run(self):
        for x in range(3):
            print(f'{threading.current_thread()}正在画图')
            time.sleep(1)


@timeit()
def multi_threading():
    coding = CodingThread()
    drawing = DrawingThread()
    coding.start()
    drawing.start()
    coding.join()
    drawing.join()
    print(f'{__name__}执行完成')


if __name__ == '__main__':
    multi_threading()


    # output
    # <CodingThread(Thread-1, started 123145452445696)>正在编码
    # <DrawingThread(Thread-2, started 123145457700864)>正在画图
    # <CodingThread(Thread-1, started 123145452445696)>正在编码<DrawingThread(Thread-2, started 123145457700864)>正在画图
    #
    # <DrawingThread(Thread-2, started 123145457700864)>正在画图<CodingThread(Thread-1, started 123145452445696)>正在编码
    #
    # _run duration 3.006542205810547
    # _run duration 3.0065767765045166
    # __main__执行完成
    # _multi_threading duration 3.00705623626709