# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     signal.py
# Author:      Jakiro
# Datetime:    2023/2/9 17:49
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import time
import signal

# 自定义超时异常
from functools import wraps


#


def time_out(time, callback):
    '''
    声明一个装饰器函数，传入超时时间，超时后调用方法，在被装饰函数执行超时后，调用超时后回调函数
    '''

    class TimeoutError(Exception):
        def __init__(self, msg):
            super(TimeoutError, self).__init__()
            self.msg = msg

    def decorator(func):
        @wraps(func)
        def handler(signum, frame):
            raise TimeoutError(f"run func:{func.__name__}timeout")

        def wrapper(*args, **kwargs):
            try:
                #  设置信号处理函数，接收一个闹钟信号，收到信号的处理方式为报错 TimeoutError
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(time)  # interval秒后向进程发送SIGALRM信号
                result = func(*args, **kwargs)  # 执行一个函数
                signal.alarm(0)  # 函数在规定时间执行完后关闭alarm闹钟，覆写闹钟
                return result
            except TimeoutError as e:
                callback(e)
        return wrapper
    return decorator


def timeout_callback(e):
    print(e.msg)


@time_out(2, timeout_callback)
def task1():
    print("task1 start")
    time.sleep(3)
    print("task1 end")


@time_out(2, timeout_callback)
def task2():
    print("task2 start")
    time.sleep(1)
    print("task2 end")


if __name__ == "__main__":
    task1()
    task2()
