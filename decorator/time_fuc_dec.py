# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   study
# FileName:     time_fuc_dec.py
# Author:      Jakiro
# Datetime:    2022/4/14 20:17
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import time
from datetime import datetime
from functools import wraps

# 写一个装饰器  用于打印一个函数的执行时长


def timeit(prefix=''):
    '''
    我们在 timeit 中定义了 2 个内部方法，然后让 timeit 可以接收参数，返回 decorator 对象，而在 decorator 方法中再返回 wrapper 对象。
    通过这种方式，带参数的装饰器由 2 个内部方法嵌套就可以实现了。
    :param prefix:
    :return:
    '''

    def dec(func):
        @wraps(func)
        # 使用@wraps装饰器  保留 func自身的属性
        def inner(*args, **kwargs):
            start_time = time.time()
            reason = func(*args, **kwargs)
            end_time = time.time()
            print(f'{prefix}_{func.__name__} duration {end_time - start_time}')
            return reason

        return inner

    return dec


class TimeIt():
    '''
    用类实现一个装饰器，与方法实现类似，只不过用类利用了 __init__ 和 __call__ 方法，其中 __init__ 定义了装饰器的参数，__call__ 会在调用 Timeit 对象的方法时触发。
    你可以这样理解：t = Timeit('prefix') 会调用 __init__，而调用 t(hello) 会调用 __call__(hello)。
    '''

    def __init__(self, prefix=None):
        self.prefix = prefix

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()
            reason = func(*args, **kwargs)
            end_time = time.time()
            print(f'{self.prefix}_{func.__name__} duration {end_time - start_time}')
            return reason

        return inner


if __name__ == '__main__':
    '''
    这里的 @timeit
    其实就等价于
    hello = timeit(hello)
    '''


    # @timeit('前缀')
    # def hello(b):
    #     time.sleep(1)
    #     # print(b)
    #     return b
    #
    #
    # # hello = timeit(hello)  # 重新定义hello
    # print(hello(2))


    # hello(2)

    @TimeIt('前缀')  # TimeIt 实例化对象   #
    def b(a):
        time.sleep(1)
        return a


    print(b(2))


