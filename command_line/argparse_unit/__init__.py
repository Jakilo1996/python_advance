# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     __init__.py.py
# Author:      Jakiro
# Datetime:    2022/5/24 13:53
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 参数	说明
# name or flags	一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
# dest	解析结果被指派给属性的名字，即调用时候的名字。如果不指定，则会用第一个参数name or flags的名称。
# metavar	生成帮助信息，比如以上的[-t test]和-t test中的test。如果没有metavar，会使用大写的dest参数。
# action	指定跟属性对应的处理逻辑， 通常的值为 store，存储参数的值，这个是默认的动作。
# nargs	nargs 命名参数关联不同数目的命令行参数到单一动作。
# default	默认值，如果一个选项需要默认值，可以用default设置
# type	默认情况下，解析器会将命令行参数当作简单字符串读入。type默认是str，也可以指定为int、float等
# choices	表示受限制的参数值。可以是一个list对象、set对象等。
# required	默认required=False，可以用required=True表示必选参数
# help	参数简短描述的字符串

# name or flags   /dest   有- 开头 需要用

