# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     global_variable.py
# Author:      Jakiro
# Datetime:    2022/4/25 16:25
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 多线程共享全局变量的问题：
# 多线程都是在同一个进程中运行的。因此在进程中的全局变量所有线程都是可共享的。
# 这就造成了一个问题，因为线程执行的顺序是无序的。有可能会造成数据错误。比如以下代码：


import threading
from decorator.time_fuc_dec import timeit
tickets = 0


def get_ticket():
    global tickets
    for x in range(10000000):
        tickets += 1
    print(f'ticket:{tickets}')

@timeit()
def main_threading():
    for x in range(2):
        t = threading.Thread(target=get_ticket)
        t.start()
        # t.join()


if __name__ == '__main__':
    main_threading()
    print(tickets)   #  主线程执行完成时， 全局变量是多少 就打印什么
#

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