# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     by_threading.py
# Author:      Jakiro
# Datetime:    2023/2/9 19:31
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import time
import threading
from functools import wraps

def callback_func(e):
    print(e.msg)


def time_out(interval, callback=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.setDaemon(True)  # 设置主线程结束 子线程立刻结束
            t.start()
            t.join(interval)  # 主线程阻塞等待interval秒
            if t.is_alive() and callback:
                return threading.Timer(0, callback).start()  # 立即执行回调函数
            else:
                return

        return wrapper

    return decorator


@time_out(2, callback_func)
def task3(hh):
    print('**********task3****************')
    for i in range(3):
        time.sleep(1)
        print(i)
        print(hh)


@time_out(2, callback_func)
def task4(hh):
    print('**********task4****************')
    for i in range(3):
        # time.sleep(1)
        print(i)
        print(hh)


def callback_func():
    print('callback')


def time_out(interval, callback=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ########## 该部分必选在requests之前导入
            import gevent
            from gevent import monkey
            monkey.patch_all()
            ##########

            try:
                gevent.with_timeout(interval, func, *args, **kwargs)
            except gevent.timeout.Timeout as e:
                callback() if callback else None

        return wrapper

    return decorator


@time_out(3, callback_func)
def func(a, b):
    import time
    time.sleep(2)
    print(a, b)


func(1, 2)

if __name__ == '__main__':
    task3('参数')
    task4('参数')