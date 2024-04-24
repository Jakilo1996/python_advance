# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     child_process.py
# Author:      Jakiro
# Datetime:    2022/4/21 21:06
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 使用类的方式创建子进程：
# 有些时候，你想以类的形式定义子进程的执行代码。
# 那么你可以自定义一个类，让他继承自Process，然后在这个类中实现run方法，以后这个子进程在执行的时候就会调用这个run方法中的代码。示例代码如下：

from multiprocessing import Process

import os

import time


class MyProcess(Process):
    def run(self):
        for x in range(5):
            print(f'子进程：{x}')
            time.sleep(1)


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print(f'主进程id:{os.getpid()}')