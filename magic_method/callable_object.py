# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     callable_object.py
# Author:      Jakiro
# Datetime:    2022/4/21 17:58
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 可调用的对象  _call__

# 在Python中，一个特殊的魔术方法可以让类的实例的行为表现的像函数一样，你可以调用他们，将一个函数当做一个参数传到另外一个函数中等等。
# 这是一个非常强大的特性让Python编程更加舒适甜美。__call__(self, [args...])
#
# 允许一个类的实例像函数一样被调用。实质上说，这意味着x()与 x.__call__()是相同的。
# 注意__call__参数可变。这意味着你可以定义__call__为其他你想要的函数，无论有多少个参数。


class CallableObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        if kwargs:
            self.x, self.y = kwargs['x'], kwargs['y']
        elif args:
            self.x, self.y = args[0], args[1]

    def __str__(self):
        return f'({self.x},{self.y})'


c2 = CallableObject(1, 2)
print(c2)  # (1,2)
c2(3, 4)  # __call__  修改x=3 y=4
print(c2) # (3,4)
