# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     alarm.py
# Author:      Jakiro
# Datetime:    2023/2/9 17:26
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import signal
import time


def work():

    print('working')

signal.alarm(5)


while True:
    time.sleep(1)
    work()

