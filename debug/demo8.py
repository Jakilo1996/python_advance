# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo8.py
# Author:      Jakiro
# Datetime:    2022/6/2 10:32
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'person name:{self.name},age:{self.age}'

    def __repr__(self):
        return f'Person("{self.name}",{self.age})'

p1 = Person('a',18)
print(p1)
print(repr(p1))
print(eval(repr(p1)))
