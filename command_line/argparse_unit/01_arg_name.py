# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     01_arg_name.py
# Author:      Jakiro
# Datetime:    2022/5/24 14:28
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# name or flags   dest    命令行参数的名字
# add_argument()方法必须知道它是否是一个选项，例如 -f 或 --foo，或是一个位置参数，例如一组文件名。 -f认为是选项参数  位置参数也可以直接接收
# 第一个传递给 add_argument() 的参数必须是一系列 flags 或者是一个简单的参数名。如果是位置参数，指定的属性就是它本身，不能再用dest指定。


import argparse

parser = argparse.ArgumentParser(description='Name or flags test')
# 加-的认为是 一个选项  调用时 -f f_arg 认为是f的参数 并复制给--foo
parser.add_argument('-f', dest='foo')
# 不能这样写 parser.add_argument('bar', dest='bar_arg')
parser.add_argument(dest='bar')
args = parser.parse_args()
print(dir(args))
print('='*20)
print('='*20)
print(args.foo)
print(args.bar)
# 其中的bar是位置参数，是必须要传入的参数。

# cmd line
#  python 01_arg_name.py -f f_arg bar_arg

# out_put
# ['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_get_args', '_get_kwargs', 'bar', 'foo']
# f_arg
# bar_arg
