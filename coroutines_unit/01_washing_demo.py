# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     01_washing_demo.py
# Author:      Jakiro
# Datetime:    2023/2/13 18:01
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import time

# def washing1():
#     time.sleep(3)  # 第一台洗衣机,
#     print('washer1 finished')  # 洗完了
#
#
# def washing2():
#     time.sleep(8)
#     print('washer2 finished')
#
#
# def washing3():
#     time.sleep(5)
#     print('washer3 finished')
import time


async def washing1():
    time.sleep(3)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


async def washing2():
    time.sleep(8)
    print('washer2 finished')


async def washing3():
    time.sleep(5)
    print('washer3 finished')


if __name__ == '__main__':
    start_time = time.time()
    washing1()
    washing2()
    washing3()
    end_time = time.time()
    print('总共耗时：{}'.format(end_time - start_time))

# if __name__ == '__main__':
#     start_time = time.time()
#     washing1()
#     washing2()
#     washing3()
#     end_time = time.time()
#     print('总共耗时：{}'.format(end_time - start_time))
