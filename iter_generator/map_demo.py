# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     map_demo.py
# Author:      Jakiro
# Datetime:    2022/4/24 16:48
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# map() 会根据提供的函数对指定序列做映射。
#
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
# map(function, iterable, ...)
# function -- 函数
# iterable -- 一个或多个序列
# Python 3.x 返回迭代器。
def square(x):
    return x ** 2


# 返回一个迭代器
print(map(square, [1, 2, 3, 4]).__next__())
