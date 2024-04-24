# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo.py
# Author:      Jakiro
# Datetime:    2023/3/10 11:16
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser(description='store const args')
# parser.add_argument('--foo_5', action='append')
parser.add_argument('-a', action='store')
parser.add_argument('-b', action='store')
parser.add_argument('-c', action='store')
args = parser.parse_args()


def func_a(a, b, c):
    print(a)
    print(b)
    print(c)

func_a(args.a, args.b, args.c)
