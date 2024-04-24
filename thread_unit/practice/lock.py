# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     lock.py
# Author:      Jakiro
# Datetime:    2022/4/25 16:49
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 锁机制：
# 为了解决以上使用共享全局变量的问题。
# threading提供了一个Lock类，这个类可以在某个线程访问某个变量的时候加锁，
# 其他线程此时就不能进来，直到当前线程处理完后，把锁释放了，其他线程才能进来处理。示例代码如下


import threading
from decorator.time_fuc_dec import timeit

value = 0

glock = threading.Lock()


def add_value():
    global value
    for x in range(10000000):
        glock.acquire()
        value += 1
        glock.release()
    print(f'value:{value}')

def add_value2():
    global value
    glock.acquire()
    for x in range(10000000):

        value += 1
    glock.release()
    print(f'value:{value}')

@timeit()
def main_threading():
    for x in range(3):
        # t = threading.Thread(target=add_value)
        # 大量的加锁释放锁 导致实际处理速度偏慢
        t = threading.Thread(target=add_value2)
        # 类似于线性处理3次加运算
        t.start()


if __name__ == '__main__':
    main_threading()


# import threading
#
# tickets = 0
#
# def get_ticket():
#     global tickets
#     for x in range(1000000):
#         tickets += 1
#     print('tickets:%d'%tickets)
#
# def main():
#     for x in range(2):
#         t = threading.Thread(target=get_ticket)
#         t.start()
#
# if __name__ == '__main__':
#     main()