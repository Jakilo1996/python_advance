# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     02_arg_action.py
# Author:      Jakiro
# Datetime:    2022/5/24 15:20
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# action 提供命令行参数默认值
# ArgumentParser对象将命令行参数与动作相关联。这些动作可以做与它们相关联的命令行参数的任何事，
# 尽管大多数动作只是简单的向parse_args()返回的对象上添加属性。action命名参数指定了这个命令行参数应当如何处理。相应的动作有：
#
# 'store'
#  存储参数的值，这个是默认动作。
#
# 'store_const'
#  存储被const命名参数指定的值。选项的值会变成一个固定值。   传入store_const时 需要传入参数 const 用来指定选项的默认值 是否可以是一个列表
# 如果指定了默认值，在使用选项进行传参，就会报错
#
# 'store_true' and 'store_false'
# 这些是'store_const'分别用作存储True和False值的特殊用例。它们的默认值对应的是False和True。比如一个选项--foo，action是'store_true'，
# 如果运行时命令行没有指定--foo，则存储的值是False；
# 如果运行时指定了--foo，则存储的值是True。
#
#
# 'append'
#  存储一个列表，并且将每个参数值追加到列表中。在允许多次使用选项时很有用。

import argparse
parser = argparse.ArgumentParser(description='store const args')
# action default_value store
parser.add_argument('--foo_1',action='store')
# action set_default_value store_const 默认值
parser.add_argument('--foo_2',action='store_const',const=42)
# action store_ture
parser.add_argument('--foo_3',action='store_true')
# action store_false
parser.add_argument('--foo_4',action='store_false')
# action append
parser.add_argument('--foo_5',action='append')

# 获得命令行输入的参数
args= parser.parse_args()
print(f'store --foo_1:{args.foo_1}')
print(f'store_const --foo_2:{args.foo_2}')
print(f'store_true --foo_3:{args.foo_3}')
print(f'store_false --foo_4:{args.foo_4}')
print(f'store_false --foo_5:{args.foo_5}')

# cmd line    python 02_arg_action.py --foo_1 2 --foo_2 --foo_3 --foo_4 --foo_5 5 --foo_5 4
# output
# store --foo_1:2
# store_const --foo_2:42
# store_true --foo_3:True
# store_false --foo_4:False
# store_false --foo_5:['5', '4']

# cmd_line   p
# python 02_arg_action.py --foo_2 3
# output
# 02_arg_action.py: error: unrecognized arguments: 3


# cmd_line
# python 02_arg_action.py
# output   未传入参数时， 存储的值 与false true 默认值刚好相反 没有这个选项时存储的是False；有这个选项时存储的是True。
# store --foo_1:None
# store_const --foo_2:None
# store_true --foo_3:False
# store_false --foo_4:True