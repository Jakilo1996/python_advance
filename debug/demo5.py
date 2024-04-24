# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     demo5.py
# Author:      Jakiro
# Datetime:    2022/5/12 10:02
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


class Person():
    def __init__(self, a):
        self.a = a
        self.b = 2
        print(a)

    def __call__(self, func, *args, fun=3, **kwargs):
        # 缺省的位置参数作为形参    *args
        # 将没有变量名接收的位置参数 打包为一个元祖 传递给 args
        # 缺省的关键字参数    **kwargs   将没有变量名接收的关键字参数 的 参数名作为key 参数值作为value 打包为一个字典，传递给kwargs
        print(*args)
        print(args)
        print(kwargs)
        # print(**kwargs)
        # *参数   解包一个元祖
        # **参数  解包一个字典   key=value的形式
        print(func(**kwargs))  # func(a=2,b=3)
        # print(*args,**kwargs)

    def sing(self):
        print('sing')


def hello(a=2, b=1):
    return a, b


p1 = Person(2)
p1(hello, 3, 4, 4, 5,fun=2, a=2, b=3)
# p1.sing()
#
