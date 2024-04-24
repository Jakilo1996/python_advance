# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     operator_method.py
# Author:      Jakiro
# Datetime:    2022/4/21 15:36
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 运算符魔术方法
# 一元操作符和函数：
#
# __pos__(self)魔术方法：在这个对象前面使用正号的时候执行的方法。
# __neg__(self)魔术方法：在这个对象前面使用负号的时候执行的方法。
# __abs__(self)魔术方法：在这个对象上使用abs函数的时候执行的方法。
# __invert__(self)魔术方法：在这个对象前面使用~的时候执行的方法。

class Coornidate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __pos__(self)魔术方法：在这个对象前面使用正号的时候执行的方法。
    def __pos__(self):
        return self

    def __neg__(self):
        return Coornidate(-self.x, -self.y)

    def __abs__(self):
        return Coornidate(abs(self.x), abs(self.y))

    def __invert__(self):
        return Coornidate(255 - self.x, 255 - self.y)

    def __str__(self):
        return f'({self.x},{self.y})'


c1 = Coornidate(-1, 2)
c2 = +c1  # __pos__  x = -1 y =2
c3 = -c1  # __neg__ x =1 y =-2
c4 = abs(c1)  # __abs__  x =1 y=2
c5 = ~c1  # __invert__ x= 256 y= 253
print(c5)


# 普通算数操作符：
# __add__(self,other)魔术方法：在两个对象相加的时候执行的方法。
# __sub__(self,other)魔术方法：在两个对象相减的时候执行的方法。
# __mul__(self,other)魔术方法：在两个对象相乘的时候执行的方法。
# __floordiv__(self,other)魔术方法：在两个对象使用//运算的时候执行的方法。
# __div__(self,other)魔术方法：在两个对象使用/运算的时候执行的方法。
# __truediv__(self,other)魔术方法：在两个对象之间使用真除的时候执行的方法。在Python3中使用/运算的时候会执行这个方法。在Python2中，默认使用__div__方法，如果from __future__ import division，那么将会使用__truediv__方法。
# __mod__(self,other)魔术方法：在使用%取模运算的时候执行的方法。
# 相关示例代码如下：


class GeneralOperator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return GeneralOperator(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return GeneralOperator(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return GeneralOperator(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other):
        print('__floordiv__')
        return GeneralOperator(self.x // other.x, self.y // other.y)

    def __divmod__(self, other):
        print('__divmod__')
        return GeneralOperator(self.x / other.x, self.y / other.y)

    def __truediv__(self, other):
        print('__truediv__')
        return GeneralOperator(self.x / other.x, self.y / other.y)

    def __mod__(self, other):
        return GeneralOperator(self.x % other.x, self.y % other.y)

    def __str__(self):
        return f'({self.x},{self.y})'


g7 = GeneralOperator(4, 6)
g8 = GeneralOperator(3, 4)
print(g7 + g8)  # __add__   (7,10)
print(g7 - g8)  # __sub__   (1,2)
print(g7 * g8)  # __mul__    (12,24)
print(g7 / g8)  # __truediv__  (1.3333333333333333,1.5)
print(g7 % g8)  # __mod__  (1,2)


# 增量赋值：
# __iadd__(self,other)魔术方法：在给对象做+=运算的时候会执行的方法。
# __isub__(self,other)魔术方法：在给对象做-=运算的时候会执行的方法。
# __imul__(self,other)魔术方法：在给对象做*=运算的时候会执行的方法。
# __idiv__(self,other)魔术方法：在给对象做/=运算的时候会执行的方法。
# __itruediv__(self,other)魔术方法：在给对象做真/=运算的时候会执行的方法。


class AugmentedAssignment():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other
        self.y += other
        return self

    def __isub__(self, other):
        return AugmentedAssignment(self.x - other, self.y - other)

    def __imul__(self, other):
        return AugmentedAssignment(self.x * other, self.y * other)

    def __itruediv__(self, other):
        return AugmentedAssignment(self.x / other, self.y * other)

    def __str__(self):
        return f'({self.x},{self.y})'


a1 = AugmentedAssignment(4, 6)
a1 += 1
print(a1)  # __iadd__ (5,7)
a1 -= 1
print(a1)  # __isub__  (4,6)
a1 *= 1
print(a1)  # __mul__ (4,6)
a1 /= 2
print(a1)  # __itruediv__ (2.0,12)
