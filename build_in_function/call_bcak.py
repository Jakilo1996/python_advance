# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     call_bcak.py
# Author:      Jakiro
# Datetime:    2023/2/9 15:43
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 简单来说就是定义一个函数，然后将这个函数的函数名传递给另一个函数做参数，以这个参数命名的函数就是回调函数。

def apply_ascyn(func, *args, callback):
    result = func(*args)
    callback(result)


def add(a, b):
    return a + b


def print_re(result):
    print(result)


# apply_ascyn(add, 1, 2, callback=print_re)


# output 3

class Result():
    def __init__(self, a):
        self.a = a

    def print_re(self, result):
        print(f'对象属性a{self.a}，打印{result}')


# apply_ascyn(add, 1, 2, callback=Result('ccc').print_re)


# output 对象属性accc，打印3

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print(f'对象属性{sequence}，打印{result}')


handle = make_handler()
next(handle)
apply_ascyn(add, 1, 2, callback=handle.send)

# output 对象属性1，打印3