# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     pause.py
# Author:      Jakiro
# Datetime:    2023/2/9 17:34
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
# import signal, time

import signal
import time
signal.alarm(5)



while True:
    time.sleep(1)
    print("学习python中...")
# 阻塞等待信号的发生，如论什么信号都可以
# print(signal.getsignal(signalnum))
signal.pause()