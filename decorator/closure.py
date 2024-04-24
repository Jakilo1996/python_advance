# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     closure.py
# Author:      Jakiro
# Datetime:    2022/4/28 20:12
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 闭包：
# 闭包是什么东西：
# 如果在一个函数中，定义了另外一个函数，并且那个函数使用了外面函数的变量，并且外面那个函数返回了里面这个函数的引用，那么称为里面的这个函数为闭包。例如：

# def greet(name):
#     def say_hello():
#         print(f'hello my name is {name}')
#
#     return say_hello
#
#
# greet('a')()


# 用闭包完成一个计算器：
def calculator(option):
    operator = None
    if option == 1:
        def add(x, y):
            return x + y

        operator = add
    elif option == 2:
        def minus(x, y):
            return x - y

        operator = minus
    elif option == 3:
        def multiply(x, y):
            return x * y

        operator = multiply
    elif option == 4:
        def divide(x, y):
            return x / y

        operator = divide
    else:
        operator = operator
    return operator


print(calculator(2)(1, 2))

# nonlocal关键字：
# 如果想要在闭包中修改外面函数的变量，这时候应该使用nonlocal关键字，来把这个变量标识为外面函数的变量：
# 以下代码修改了name，但没有使用nonlocal关键字，会报错：


# def greet(name):
#     def say_hello():
#         name += 'hello'
#         print('hello my name is %s' % name)
#     return say_hello

def greet(name):
    def say_hello():
        nonlocal name
        name += 'hello'
        print('hello my name is %s' % name)
    return say_hello

greet('a')()