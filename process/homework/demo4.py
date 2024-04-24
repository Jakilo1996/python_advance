# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo4.py
# Author:      Jakiro
# Datetime:    2022/4/24 17:28
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 1、计算1~100000000之间所有偶数的和。（提示：可以使用内置的sum函数计算和。如list=[1, 2];sum(list))。然后思考以下问题：
# 使用多进程和不使用多进程，哪种速度更快                   开启多进程速度较快
# 对比开启4个多进程和开启10个多进程两种方法哪个速度更快。    4进程快, 开启10进程的时候过程需要时间
# 多进程在哪些方面具有优势？


from multiprocessing import Manager, Pool
import time
from decorator.time_fuc_dec import timeit

@timeit()
def sum_data(start_position, end_position, queue2):
    queue2.put(sum(range(start_position, end_position, 2)))


if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(10)
    queue1 = Manager().Queue(10)
    for x in range(1, 1000000001, 100000000):
        print(x)
        pool.apply_async(
            sum_data, args=(x, x + 100000000, queue1)
        )

    pool.close()
    pool.join()
    sum3 = 0
    for _ in range(10):
        sum3 += queue1.get(block=False)

    print(f'{time.time() - start_time}:{sum3}')
