# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     fork_d.py
# Author:      Jakiro
# Datetime:    2022/8/16 09:54
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 导入 os 模块
import os

# 调用 fork() 方法创建子进程，并获取返回值  子进程永远返回0，父进程返回子进程的pid
pid = os.fork()
# print(type(pid))
# 输出 fork() 方法返回的值
print("pid：", pid)

# os.getpid()：获取当前进程 id
# os.getppid()：获取父进程 id
if (pid > 0):
    print("当pid不为0时，当前进程是父进程，自身id：", os.getpid())
else:
    print("当pid为0时，当前进程是子进程，子进程自身的id：%d === 子进程的父进程id：%d" % (os.getpid(), os.getppid()))
