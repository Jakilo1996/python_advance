# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     process_id.py
# Author:      Jakiro
# Datetime:    2022/4/21 20:32
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 获取进程号：

# 在Python中可以通过os模块的一个函数getpid()可以获取到当前进程的进程号。通过getppid()可以获取到这个进程的父进程的进程号。示例代码如下：


from multiprocessing import Process
import os


def zhiliao():
    print('===子进程===')
    print(f'子进程id:{os.getpid()}')
    print(f'父进程id:{os.getppid()}')
    print('===子进程===')


if __name__ == '__main__':
     p = Process(target=zhiliao)
     p.start()
     print(f'主进程id：{os.getpid()}')

# output
# 主进程id：63523
# ===子进程===
# 子进程id:63524
# 父进程id:63523
# ===子进程===

# 父进程会等待子进程执行完毕后再退出：

# 如果在父进程中执行完所有代码后，还有子进程在执行，那么父进程会等待子进程执行完所有代码后再退出。