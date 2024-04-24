# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     04_arg_choices.py
# Author:      Jakiro
# Datetime:    2022/5/24 16:52
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# choices
# 从choices选项中指定参数的值。指定当前选项的取值范围 未传入 取值为None
# 传入超过一个值 报错 unrecognized arguments
#  传入非取值范围  报错  invalid choice
# ，结合default 使用默认值，未传入 取默认值

import argparse

parser = argparse.ArgumentParser(description='choices test')
parser.add_argument('--foo', choices=['arg1', 'arg2', 'arg3'], default='arg1')
args = parser.parse_args()
print(f'current foo arg: {args.foo}')

# command line
#  python 04_arg_choices.py

# output
# current foo arg: arg1

# command line    python 04_arg_choices.py --foo arg2
# output
# current foo arg: arg2

# python 04_arg_choices.py --foo arg4
# usage: 04_arg_choices.py [-h] [--foo {arg1,arg2,arg3}]
# 04_arg_choices.py: error: argument --foo: invalid choice: 'arg4' (choose from 'arg1', 'arg2', 'arg3')


# python 04_arg_choices.py --foo arg2 arg3
# usage: 04_arg_choices.py [-h] [--foo {arg1,arg2,arg3}]
# 04_arg_choices.py: error: unrecognized arguments: arg3
