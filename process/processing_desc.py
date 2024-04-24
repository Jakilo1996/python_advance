# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     processing_desc.py
# Author:      Jakiro
# Datetime:    2022/4/21 20:22
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# multiprocessing模块介绍：
# multiprocessing是Python中一个专门用来创建创建多进程的库，multiprocessing提供了一个Process类来创建进程。以下用一个例子讲解Process类的使用：

from multiprocessing import Process

import time


def zhiliao():
    print('zhiliao process')


if __name__ == '__main__':
    # 开启一个子进程  ，如果需要参数 一定要用  args = () 的方式传入
    p = Process(target=zhiliao)
    p.start()

    while True:
        print('main process')
        time.sleep(3)


# output
# main process
# zhiliao process
# main process