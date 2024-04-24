# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     class_expression1.py
# Author:      Jakiro
# Datetime:    2022/4/18 18:24
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# __hash__ / __eq__
# __bool__


# __hash__
# __hash__ 方法返回一个整数，用来表示实例对象的唯一标识，配合 __eq__ 方法，可以判断两个对象是否相等：
# 如果我们需要判断两个对象是否相等，只需要我们重写 __hash__ 和 __eq__ 方法就可以了。

class Person1():
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return f'Person({self.uid})'

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid


person1 = Person1(2)
person2 = Person1(2)
# 标识符相同 == 视为同一个对象
print(person2 == person2)

# output
# Ture

# is判断的时候  不为同一个对象
print(person1 is person2)

# output
# False

# 此外，当我们使用 set 时，在 set 中存放这些对象，也会根据这两个方法进行去重操作。
person3 = Person1(3)
print(set([person1, person2, person3]))


# __bool__
# 当调用 bool(obj) 时，会调用 __bool__ 方法，返回 True 或 Fals

class Person2():
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return f'Person({self.uid})'

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid

    def __bool__(self):
        return self.uid > 10


person4 = Person2(5)
person5 = Person2(15)
print(bool(person4))
print(person4.__bool__())
# output
# False
print(bool(person5))
print(person5.__bool__())
# output
# Ture

'''
# __hash__
# __hash__ 方法返回一个整数，用来表示实例对象的唯一标识，配合 __eq__ 方法，可以判断两个对象是否相等：
# __eq__ 用于通过对比唯一标识符，返回 一个布尔值
# 如果我们需要判断两个对象是否相等，只需要我们重写 __hash__ 和 __eq__ 方法就可以了。
# 标识符相同 == 视为同一个对象
# 标识符相同 is判断的时候  不为同一个对象
# 此外，当我们使用 set 时，在 set 中存放这些对象，也会根据这两个方法进行去重操作。
# __bool__
# 当调用 bool(obj) 时，会调用 __bool__ 方法，返回 True 或 False
'''