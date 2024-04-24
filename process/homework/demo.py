# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo.py
# Author:      Jakiro
# Datetime:    2022/4/24 15:50
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 1、计算1~100000000之间所有偶数的和。（提示：可以使用内置的sum函数计算和。如list=[1, 2];sum(list))。然后思考以下问题：
# 使用多进程和不使用多进程，哪种速度更快                   开启多进程速度较快
# 对比开启4个多进程和开启10个多进程两种方法哪个速度更快。    4进程快, 开启10进程的时候过程需要时间
# 多进程在哪些方面具有优势？


from decorator.time_fuc_dec import timeit


# @timeit()
# def get_result():
#     print(sum(range(0, 1000000001, 2)))


# get_result()
# None_get_result duration 10.00149416923523


from multiprocessing import Pool, Manager
import time

@timeit()
def get_result_by_4pro(start_position, end_position, q):
    sum33 = sum(range(start_position, end_position, 2))
    print(sum33)
    q.put_nowait(sum33)


if __name__ == '__main__':

    start_time =time.time()
    pool = Pool(4)
    queue_1 = Manager().Queue(4)
    for x in range(1, 1000000001, 250000000):
        print(x)
        pool.apply_async(get_result_by_4pro,args=( x, x + 250000000, queue_1))
    pool.close()
    pool.join()
    sum2 = 0
    # print(queue_1.get(block=False))
    for _ in range(4):
        # print(_)
        sum2 += queue_1.get(block=False)
    # print(sum2)
    end_time = time.time()
    print(f'get_result_by_4pro_用时{end_time-start_time},{sum2}')

    # output
    # None_get_result_by_4pro
    # duration
    # 2.5461440086364746
    # 109375000000000000
    # None_get_result_by_4pro
    # duration
    # 2.552816152572632
    # 46875000000000000
    # 78125000000000000
    # None_get_result_by_4pro
    # duration
    # 2.5598220825195312
    # None_get_result_by_4pro
    # duration
    # 2.55967116355896
    # get_result_by_4pro_用时2
    # 2.706862211227417, 250000000000000000