# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     demo3.py
# Author:      Jakiro
# Datetime:    2022/5/9 15:28
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

def file_open(file_path, mode):
    try:
        fp = open(file_path, mode)
        yield fp
    finally:

        print(fp.read())
        fp.close()

b = file_open('aaa.txt','w')
next(b)