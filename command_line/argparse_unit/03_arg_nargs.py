# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     03_arg_nargs.py
# Author:      Jakiro
# Datetime:    2022/5/24 16:06
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# nargs  一组参数可以接收多个 或是满足一种类型的默认值
# ArgumentParser对象通常关联一个单独的命令行参数到一个单独的被执行的动作。
# nargs 命名参数关联不同数目的命令行参数到单一动作。可以思考一下和action中append的区别。支持的值有：
#
# N 一个整数  根绝整数的数量来设定命令行参数
# '?' 表示有或者没有选项的值。
# '*' 表示0个或者大于0个。
# '+' 表示大于等于一个。其实'?'、'*'、'+'和正则表达式意义差不多

import  argparse
parser = argparse.ArgumentParser(description='nargs test')
# 一个
parser.add_argument('--foo_1',nargs=1)
parser.add_argument('--foo_2',nargs=2)

# 有或没有  没有None  有 只能接收一个
parser.add_argument('--foo_3',nargs='?')
# '*' 表示0个或者大于0个。不管传入几个都用列表来接收
parser.add_argument('--foo_4',nargs='*')
# '+' 表示大于等于一个  不管传入几个，都用列表来接收   不足一个  # 报错 expected at least one argument
parser.add_argument('--foo_5',nargs="+")

args = parser.parse_args()
print(f'"N"--foo_1:{args.foo_1}')
print(f'"N"--foo_2:{args.foo_2}')

print(f'"?"--foo_3:{args.foo_3}')
print(f'"*"--foo_4:{args.foo_4}')

print(f'"+"--foo_3:{args.foo_5}')

# cmd_line
# python 03_arg_nargs.py --foo_1 2 --foo_2 a b --foo_3 a --foo_4  --foo_5 s

# ouput
# "N"--foo_1:['2']
# "N"--foo_2:['a', 'b']
# "?"--foo_3:a
# "*"--foo_4:[]
# "+"--foo_3:['s']

# cmd_line
#  python 03_arg_nargs.py

# output   都没有值时  都为空
# "N"--foo_1:None
# "N"--foo_2:None
# "?"--foo_3:None
# "*"--foo_4:None
# "+"--foo_3:None
# "*"--foo_4:None
# "+"--foo_3:None

# cmd_line
# python 03_arg_nargs.py --foo_3  --foo_4

# output
# "N"--foo_1:None
# "N"--foo_2:None
# "?"--foo_3:None
# "*"--foo_4:[]
# "+"--foo_3:None
