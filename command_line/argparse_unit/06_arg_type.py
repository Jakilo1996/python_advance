# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     06_arg_type.py
# Author:      Jakiro
# Datetime:    2022/5/24 17:01
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# type
#
# 默认情况下，解析器会将命令行参数当作简单字符串读入。
# type默认是str，也可以指定为int、float等
# 传入错误的type 报错invalid int value: 'b'
#
# 如果指定格式为list  会将字符串参数的每个元素拆分列表的每一个元素存储
# 如果指定格式为tuple  会将字符串参数的每个元素拆分元祖的每一个元素存储
# 如果指定格式为set  会将字符串参数的每个元素拆分集合的每一个元素存储

# 尝试后认为不支持字典

import argparse

parser = argparse.ArgumentParser(description='type test')

parser.add_argument('--foo_1', type=int)
parser.add_argument('--foo_2', type=float)
parser.add_argument('--foo_3', type=list)
parser.add_argument('--foo_4', type=tuple)
parser.add_argument('--foo_5', type=set)
# parser.add_argument('--foo_6', type=dict)
args = parser.parse_args()
print(f"int foo_1:{args.foo_1}")
print(f"float foo_2:{args.foo_2}")
print(f"list foo_3:{args.foo_3}")
print(f"tuple foo_4:{args.foo_4}")
print(f"set foo_5:{args.foo_5}")
# 不支持字典
# print(f"dict foo_6:{args.foo_6}")
# int foo_1:2
# float foo_2:3.0
# list foo_3:['1', 'a', 'b']
# tuple foo_4:('b', '2', '3', '4', 's')
# set foo_5:{'a', 'b', 's', 'd'}


# command_line  python 06_arg_type.py --foo_1 2 --foo_2 3 --foo_3 1ab --foo_4 b234s --foo_5 bsadad
# output
#



