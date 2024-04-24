# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     class_expression.py
# Author:      Jakiro
# Datetime:    2022/4/18 15:29
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 类的表示
# 类的表示相关的魔法方法，主要包括以下几种：
# __str__ / __repr__


class Person():
    def __init__(self):
        self.name = 1

# __str__/__repr__
# 关于 __str__ 和 __repr__ 这 2 个魔法方法，非常类似，很多人区分不出它们有什么不同，我们来看几个例子，就能理解这 2 个方法的效果
a = 'hello'
# print(str(a))
#
# #  output
# # hello
# print('%s'%a) # 调用__str__
#  output
# hello

# print(repr(a)) # 对象a的标准表示  也就是a是如何创建的
# output
# 'hello'

d = Person()
# print(repr(d))
#
# # output
# # <__main__.Person object at 0x7fa2ea7d3b50>
#
# print(d)  #  打印一个对象的时候，打印出来是 类名+地址
# output
# <__main__.Person object at 0x7fa2ea7d3b50>

import datetime
b= datetime.datetime.now()
# str(b)
# print(b.__str__())
# print(b.__str__)
# # output
# # 2022-04-18 16:18:53.678087
#
# print(b.__repr__) # 直接调用方法名  打印一个方法以及类
# output
# <method-wrapper '__repr__' of datetime.datetime object at 0x7fe0fd5df570>

# print(repr(b))
# print(b.__repr__())  # 打印这个方法的返回值，方法的返回值为这个对象的标准创建方式
# print(repr(b))  # 打印这个方法的返回值，方法的返回值为这个对象的标准创建方式  与上一行相同
# # output
# # datetime.datetime(2022, 4, 18, 16, 31, 26, 409115)
#
#
# c = eval(b.__repr__()) # __repr__ 返回的结果是可执行的，通过 eval(repr(obj)) 可以正确运行
# print(c)   # 直接返回运行结果
# output
# 2022-04-18 16:31:26.409115

# 在pycharm中，如果将一个对象创建完成后，放到一个列表中，然后再打印这个列表，那么会打印这个列表中所有的对象，这时候会调用__repr__魔术方法，
f  = Person()
g = [d,f]
# print(g)
# output
# [<__main__.Person object at 0x7fdcdbf853d0>, <__main__.Person object at 0x7fdcdf212b50>]


'''  __str__/__repr__总结
__str__ 强调可读性，而 __repr__ 强调准确性 / 标准性
__str__ 的目标人群是用户，而 __repr__ 的目标人群是机器，__repr__ 返回的结果是可执行的，通过 eval(repr(obj)) 可以正确运行
占位符 %s 调用的是 __str__，而 %r 调用的是 __repr__ 方法
 __str__强调可以理解展示，__repr__强调创建过程
在pycharm中，如果将一个对象创建完成后，放到一个列表中，然后再打印这个列表，那么会打印这个列表中所有的对象，这时候会调用__repr__魔术方法，
'''


# case1  同时定义__str__和__repr__

class Person2():
    #  举例__str__\__repr__的常用方法
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def __str__(self):
        # 格式化 友好对用户人类展示
        return f'姓名：{self.name} 年龄：{self.age}'

    def __repr__(self):
        # 标准化  机器展示
        return f'Person2(name="{self.name}", age={self.age})'


person1 = Person2(name='qiujie', age=26)

# 强调对用户友好
# print(str(person1))
# print(person1.__str__())
# print('%s' % person1)

# output
# 姓名：qiujie 年龄：26

# 强调对机器友好 结果 eval 可执行
# print(repr(person1))
# print(person1.__repr__())
# print('%r' % person1)

# output
# Person(name=qiujie, age=26)

# print(eval(person1.__repr__()))  # 执行Person(name='qiujie',age=26)的结果
# output
# 姓名：qiujie 年龄：26


# case2  只定义 __str__，但没有定义 __repr__：


class Person3():
    #  举例__str__\__repr__的常用方法
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def __str__(self):
        # 格式化 友好对用户人类展示
        return f'姓名：{self.name} 年龄：{self.age}'


person2 = Person3(name='qiujie', age=26)

# 强调对用户友好
# print(str(person2))
# print(person2.__str__())
# print('%s' % person2)
#
# # output
# # 姓名：qiujie 年龄：26
#
# # 强调对机器友好 结果 eval 可执行
# print(repr(person2))
# print(person2.__repr__())
# print('%r' % person2)

# output
# <__main__.Person3 object at 0x7fa0c39f70d0>


print(eval(person2.__repr__()))  # 执行Person(name='qiujie',age=26)的 因为没有定义repr 不可执行
# # output
# #报错 invalid syntax


# case3 只定义 __repr__，但没有定义 __str__：


class Person4():
    #  举例__str__\__repr__的常用方法
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def __repr__(self):
        # 标准化  机器展示
        return f'Person4(name="{self.name}", age={self.age})'


person3 = Person4(name='qiujie', age=26)

# 强调对用户友好
# print(str(person3))
# print(person3.__str__())
# print('%s' % person3)
#
# # output
# # Person(name="qiujie", age=26)
#
# # 强调对机器友好 结果 eval 可执行
# print(repr(person3))
# print(person3.__repr__())
# print('%r' % person3)

# output
# Person(name=qiujie, age=26)

# print(eval(person3.__repr__()))  # 执行Person(name='qiujie',age=26)的结果
# output
# 姓名：qiujie 年龄：26

'''  __str__/__repr__总结
__str__ 强调可读性，而 __repr__ 强调准确性 / 标准性
__str__ 的目标人群是用户，而 __repr__ 的目标人群是机器，__repr__ 返回的结果是可执行的，通过 eval(repr(obj)) 可以正确运行
占位符 %s 调用的是 __str__，而 %r 调用的是 __repr__ 方法
 __str__强调可以理解展示，__repr__强调创建过程
在pycharm中，如果将一个对象创建完成后，放到一个列表中，然后再打印这个列表，那么会打印这个列表中所有的对象，这时候会调用__repr__魔术方法，

通过case2 和 case3 可以看出
如果只定义了__str__, repr(person) 输出<__main__.Person3 object at 0x7fa0c39f70d0>
如果只定义 __repr__, str(person)和repr(person)的输出结果相同
也就是说，__repr__在表示类的时候 是第一级的，如果不定义__str__，那么__str__= __repr__.
而 __str__展示类时是次级的，如果没有定义__repr__，那么repr(person)将会展示缺省的定义  <__main__.Person3 object at 0x7fa0c39f70d0>
'''
