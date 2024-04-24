# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     process_join.py
# Author:      Jakiro
# Datetime:    2022/4/21 20:48
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# Process对象的join方法：
# 使用Process创建了子进程，调用start方法后，父子进程会在各自的进程中不断的执行代码。
# 有时候如果想等待子进程执行完毕后再执行下面的代码，那么这时候可以调用join方法。示例代码如下：
import time
from multiprocessing import Process


def zhiliao():
    for x in range(5):
        print(f'子进程中的代码{x}')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=zhiliao)
    p.start()
    # 主进程阻塞 等待子进程完成才执行下面的代码  join方法还可以传一个timeout，用来指定等待的最长时间。
    p.join(2)
    print('父进程中的代码')


# output   如果不设置等待时间  父进程要等待所有子进程执行完成 才会执行 join之后的代码
# 子进程中的代码0
# 子进程中的代码1
# 子进程中的代码2
# 子进程中的代码3
# 子进程中的代码4
# 父进程中的代码

# output  设置了超时等待时间，等待2秒后  父进程代码执行 等待子进程执行完成后 才会才会执行join之后的打印语句
# 子进程中的代码0
# 子进程中的代码1
# 子进程中的代码2
# 父进程中的代码
# 子进程中的代码3
# 子进程中的代码4

"""
多进程使用
"""
# from multiprocessing import Process
# import time

# def f(name, i):
#     time.sleep(i)

#     print('hello', name, i)

# if __name__ == '__main__':
#     plist = []
#     for i in range(3):
#         p = Process(target=f, args=('bob', i))
#         p.start()
#         plist.append(p)
#     # for i in plist:
#         # i.join()
#         # print("i")
#         # print(i)
#     time.sleep(1)
#     print("main")
#     plist[2].join()
#     print("main2")

# plist[1].join()
