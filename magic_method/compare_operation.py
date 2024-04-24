# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     compare_operation.py
# Author:      Jakiro
# Datetime:    2022/4/20 15:58
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# __cmp__
# __eq__
# __ne__
# __lt__
# __gt__


# __cmp__
# 从名字我们就能看出来这个魔法方法的作用，当我们需要比较两个对象时，我们可以定义 __cmp__ 来实现比较操作。

class Person1():
    def __init__(self, uid, name, salary):
        self.uid = uid
        self.name = name
        self.salary = salary

    def __cmp__(self, other):
        if self.uid == other.uid:
            return 0
        if self.uid > other.uid:
            return 1
        if self.uid < other.uid:
            return -1
        raise ValueError

    def __eq__(self, other):
        """对象 == 判断"""
        return self.uid == other.uid

    def __ne__(self, other):
        """对象 != 判断"""
        return self.uid != other.uid

    def __lt__(self, other):
        """对象 < 判断 根据len(name)"""
        return len(self.name) < len(other.name)

    def __gt__(self, other):
        """对象 > 判断 根据alary"""
        return self.salary > other.salary


p1 = Person1(1, 'zhangsan', 1000)
p2 = Person1(1, 'list', 2000)
p3 = Person1(2, 'wangwu', 3000)
print(p1.__cmp__(p2))
print(p1 == p2)
print(p1!=p2)
print(p1<p2)
print(p1>p2)
# output
# 0
# True
# False
# False
# False

# __eq__
# __eq__ 我们在上一篇文章已经介绍过，它配合 __hash__ 方法，可以判断两个对象是否相等。
#
# 但在这个例子中，当判断两个对象是否相等时，实际上我们比较的是 uid 这个属性。
#
# __ne__
# 同样地，当需要判断两个对象不相等时，会调用 __ne__ 方法，在这个例子中，我们也是根据 uid 来判断的。
#
# __lt__
# 当判断一个对象是否小于另一个对象时，会调用 __lt__ 方法，在这个例子中，我们根据 name 的长度来做的比较。
#
# __gt__
# 同样地，在判断一个对象是否大于另一个对象时，会调用 __gt__ 方法，在这个例子中，我们根据 salary 属性判断。