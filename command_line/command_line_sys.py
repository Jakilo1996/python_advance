# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     command_line_sys.py
# Author:      Jakiro
# Datetime:    2022/5/24 11:31
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# python命令行参数
# python获取命令行参数的方式主要有三种：
#
# sys.argv
# getopt
# argparse

# sys.argv
# sys.argv是python中最基本、最简单的获取命令行参数的方式。sys.argv返回一个命令行参数列表。



import sys
# 命令行参数个数
print('命令行参数个数：%s' % len(sys.argv))
# 命令行参数
print('命令行参数：%s' % ' '.join(sys.argv))
# 第一个参数表示脚本名
print('脚本名称：%s' % sys.argv[0])

print(sys.argv)


# output
# python command_line_sys.py -v -s -s -4 -s
# 命令行参数个数：6
# 命令行参数：command_line_sys.py -v -s -s -4 -s
# 脚本名称：command_line_sys.py