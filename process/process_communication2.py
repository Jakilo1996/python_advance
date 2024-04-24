# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     process_communication2.py
# Author:      Jakiro
# Datetime:    2022/4/24 14:41
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 使用Queue给Pool进程池做进程间通信

# 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，
# 而不是multiprocessing.Queue()，否则会报错。RuntimeError: Queue objects should only be shared between processes through inheritance。
# 下面代码演示进程池中的进程通信：

from multiprocessing import Pool, Queue, Process, Manager


def read_fuc(q):
    while not q.empty():
        # 按照先进先出的原则 读取数据
        print(f'读到的值:{q.get()}')


def write_func(q):
    for x in ['m1', 'm2', 'm3']:
        q.put(x)


if __name__ == '__main__':
    q = Manager().Queue()
    pool = Pool(2)
    pool.apply(write_func, args=(q,))
    pool.apply(read_fuc, args=(q,))
    pool.close()

    pool.join()
