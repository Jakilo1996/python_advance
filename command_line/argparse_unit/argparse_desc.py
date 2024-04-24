# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     argparse_desc.py
# Author:      Jakiro
# Datetime:    2022/5/24 13:57
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# argparse
# argparse模块是标准库中最大的模块之一，拥有大量的配置选项，这里只说明最常用、最基本的用法。
# argparse自带说明文档，用python filename.py -h或者python filename.py --help就可以查看使用说明，非常方便，不像getopt一样要自己写说明。
# 推荐使用argparse模块解析命令行参数。


# metavar
import argparse
parser = argparse.ArgumentParser(description='Simple argparse test')
parser.add_argument('-t', dest='test', metavar='test', action='store', help='test option')
parser.add_argument('-r', dest='r', metavar='test', action='store', help='test option')
args = parser.parse_args()
print(args.test,args.r)

