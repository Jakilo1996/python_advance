# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     client.py
# Author:      Jakiro
# Datetime:    2022/3/10 13:54
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import socket_demo
import sys

s = socket_demo.socket(socket_demo.AF_INET, socket_demo.SOCK_STREAM)

host = socket_demo.gethostname()

port = 9999
#如果不是本机，host用server的，ip和name都可以。
s.connect((host,port))

msg = s.recv(1024)
msg2 = sys.argv[1]
# print(msg2)
s.send(msg2.encode("utf-8"))
msg3 = s.recv(1024)

s.close()

print(msg.decode("utf-8"))
print(msg3.decode("utf-8"))