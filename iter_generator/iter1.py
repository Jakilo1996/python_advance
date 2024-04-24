# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     iter1.py
# Author:      Jakiro
# Datetime:    2022/1/18 13:53
# Description:  迭代器和生成器
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 迭代器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器可以让我们访问集合的时候变得非常方便。之前我们通过for...in...的方式访问一个集合的时候，就是使用迭代器完成的。
# 如果没有迭代器，那么我们只能通过while循环，每次循环的时候通过下标访问了。

# 迭代器是一个可以记住遍历的位置的对象。
#
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
#
# 迭代器有两个基本的方法：iter() 和 next()。
#
# 字符串，列表或元组对象都可用于创建迭代器： 可以直接使用for循环遍历的对象，成为可迭代的对象，常见的可迭代的对象有：list、tuple、dict、set、str以及生成器。
# 更加专业的判断一个对象是否是可迭代的对象是：这个对象有一个__iter__方法，并且这个方法会返回一个迭代器对象，这种对象就叫做可迭代的对象。
list1 = [1, 2, 3, 4]
it1 = iter(list1)

for i in range(0,10):
    print(next(it1))


for i in it1:

    print(i, end='\t')

# next方法
# while 1:
#     try:
#         print(next(it1))
#     except StopIteration:
#         break

# 通过类实现一个迭代器功能
class IterationClass():
    def __init__(self,b):
        self.b = b

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.b:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
# #
# #
# it = IterationClass(15)
# it_instance = iter(it)
#
# for i in range(0,21):
#     print(next(it_instance))

# 使用iter()方法获取可迭代对象的迭代器：
# 有时候我们拥有了一个可迭代的对象，我们想要获取这个迭代器，那么可以通过iter(x)方法获取这个可迭代对象的迭代器。
# a = it_instance.__iter__()
# while 1:
#     try:
#         print(a.__next__())
#     except StopIteration:
#         break


class MyRangeIterator():
    '''
    迭代器
    '''

    def __init__(self, start, end,step):
        self.index = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            index = self.index
            self.index += self.step
            return index
        else:
            raise StopIteration
# #
# #
# myrange = MyRangeIterator(0,20,2)
# my_range_it = iter(myrange)
# for i in range(0,10):
#     print(next(my_range_it))





class MyRange():
    '''
    可迭代对象
    '''
    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.index, self.end,1)
# #
# # # 迭代器实例
a = MyRangeIterator(1, 10,2)
# #
# print(a.__class__)
#
# # 迭代器只能通过 next调用
#
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
#
# # 可迭代对象实例
b = MyRange(1,10)
# # 可迭代对象可以直接遍历
# for x in b:
#     print(x)
#
#
from collections.abc import Iterable,Iterator
# 可以使用isinstance()判断一个对象是否是Iterable的对象：
it_instance = IterationClass(2)
# # 迭代器必须有 __iter__  __next_两个方法



# print(isinstance(b,Iterator))
# print(isinstance(b,Iterable))
#
# print(isinstance(a,Iterator))
# print(isinstance(a,Iterable))
# # 通过 iter  将可迭代对象转化为迭代器
# c = iter(b)
# print(c.__next__())