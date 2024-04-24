# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     05_arg_required.py
# Author:      Jakiro
# Datetime:    2022/5/24 17:01
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# required
# 默认required=False， 表示非必选参数
# 可以用required=True   表示必选参数  不能和default 否则不会报错


import argparse

parser = argparse.ArgumentParser(description='choices test')
parser.add_argument('--foo',choices=['arg1','arg2','arg3'],required=True)
args = parser.parse_args()
print(f'current foo arg: {args.foo}')


# command_line
# python 05_arg_required.py

# output
# error: the following arguments are required: --foo