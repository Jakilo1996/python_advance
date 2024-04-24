# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     fork_d.py
# Author:      Jakiro
# Datetime:    2022/4/24 16:43
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 1、计算1~100000000之间所有偶数的和。（提示：可以使用内置的sum函数计算和。如list=[1, 2];sum(list))。然后思考以下问题：
# 使用多进程和不使用多进程，哪种速度更快                   开启多进程速度较快
# 对比开启4个多进程和开启10个多进程两种方法哪个速度更快。    4进程快, 开启10进程的时候过程需要时间
# 多进程在哪些方面具有优势？

# 2、python进程和线程的使用场景
# 多进程适用于CPU计算密集的工作，多线程适合IO、文件读写的工作

# 3、IO密集型和CPU密集型的区别，分别在什么样的情况下使用多进程还是多线程
# CPU计算密集的情况下使用多进程，IO密集的情况下使用多线程

from decorator.time_fuc_dec import timeit

from multiprocessing import Pool, Manager
import time


@timeit()
def get_result_by_10pro(start_position, end_position, q):
    sum33 = sum(range(start_position, end_position, 2))
    print(sum33)
    q.put_nowait(sum33)


if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(10)
    queue1 = Manager().Queue(10)
    for x in range(1, 1000000001, 100000000):
        print(x)
        pool.apply_async(get_result_by_10pro, args=(x, x + 100000000, queue1))
    pool.close()
    pool.join()
    sum2 = 0
    for x in range(10):
        sum2 += queue1.get(block=False)
    print(f'{time.time() - start_time}:{sum2}')

    # output
    # 1
    # 100000001
    # 200000001
    # 300000001
    # 400000001
    # 500000001
    # 600000001
    # 700000001
    # 800000001
    # 900000001
    # 2500000000000000
    # 17500000000000000
    # None_get_result_by_10pro duration 2.578486919403076
    # None_get_result_by_10pro duration 2.579611301422119
    # 7500000000000000
    # 22500000000000000
    # None_get_result_by_10pro duration 2.5846309661865234
    # None_get_result_by_10pro duration 2.5844058990478516
    # 27500000000000000
    # 42500000000000000
    # None_get_result_by_10pro duration 2.5817110538482666
    # None_get_result_by_10pro duration 2.585577964782715
    # 47500000000000000
    # None_get_result_by_10pro duration 2.5807788372039795
    # 12500000000000000
    # None_get_result_by_10pro duration 2.5926342010498047
    # 32500000000000000
    # None_get_result_by_10pro duration 2.586750030517578
    # 37500000000000000
    # None_get_result_by_10pro duration 2.5993030071258545
    # 2.6982531547546387:250000000000000000
