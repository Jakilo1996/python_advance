# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     generator.py
# Author:      Jakiro
# Datetime:    2022/4/28 17:35
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 生成器

# 为什么需要生成器：
# 假如现在有一个需求，我要打印从1-1亿的整形。如果我们采用普通的方式，直接调用range函数，那么程序肯定会崩溃，因为range(1,100000000)函数直接产生一个从1-1亿的列表，
# 这个列表中的所有数据都是存放在内存中的，会导致内存爆满。这时候我们可以采用生成器来解决这个问题，生成器不会一次性把所有数据都加载到内存中，而是在循环的时候临时生成的
# ，循环一次生成一个，所以在程序运行期间永远都只会生成一个数据，从而大大节省内存。

# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
#
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
#
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
#
# 调用一个生成器函数，返回的是一个迭代器对象。
#
# 以下实例使用 yield 实现斐波那契数列：


# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while 1:
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# #
# #
# from collections.abc import Iterable,Iterator
# f_100 = fibonacci(5)
# # print(f_100.__dir__)
# print(isinstance(f_100,Iterator))
# #
# while 1:
#     try:
#         print(next(f_100), end='\t')
#     except StopIteration:
#         break

# 解决打印1-1亿的问题：
# 用range函数配合圆括号可以产生一个生成器
# 普通的列表.

from decorator.time_fuc_dec import timeit
@timeit('s')
def a():
    num_list = [x for x in range(1, 100000000)]
    print(type(num_list))

#
@timeit('s')
def b():
    num_gen = (x for x in range(1, 100000000))
    print(type(num_gen))
    print(next(num_gen))

# a()
# b()
# next函数和__next__方法：
# next函数可以迭代生成器的返回值

# 自己写生成器：
# 生成器可以通过函数产生。如果在一个函数中出现了yield表达式，那么这个函数将不再是一个普通的函数，而是一个生成器函数。yield一次返回一个结果，并且会冻结当前函数的状态。以下是一个非常简单的生成器：

# def my_gen():
#     yield 1
#     yield 2
#     yield 3
#
# # 那么想要获取里面的值，可以通过以下方式获取：
# ret = my_gen()
# print(next(ret))
# print(next(ret))
# print(next(ret))


# send方法：
# send方法和next方法类似，可以用来触发生成器的下一个yield，但是send不仅可以触发下一个yield，还可以发送数据过去，作为yield表达式的值。
# send(arg)  将参数
def my_gen(start):
    while start < 10:
        temp = yield start
        print(temp)
        start += 1
#
ret = my_gen(2)
print(type(ret))
# # # next(ret)返回1
# # # 以下结果会打印1
print(next(ret))
# # # send("Hello World")返回2
# # # 但是会将"Hello World"赋值给yield start
# # # 因此temp = "Hello World"
# # # 那么会打印"Hello World"
# # # 并且打印2
print(ret.send('hello'))


# 生成器中的return语句会触发StopIterator异常：

# def my_gen(start):
#     while start < 3:
#         temp = yield start
#         print(temp)
#         start +=1
#         # 触发StopIterator异常，会导致不能继续遍历
#         return 'nihao'
#
# ret =my_gen(1)
# for x in ret:
#     print(x)

# 生成器的使用案例：
# 用yield实现斐波拉契数列： 斐波拉契数列的算法：除第一个和第二个数以外，任意一个数都可由前两个数相加得到：1,1,2,3,5,8,13,21,34,55...

# def fibonacci(n):
#     a, b, count = 0, 1, 0
#     while 1:
#         if count > n:
#             return
#         else:
#             yield a
#             a, b = b, a + b
#             count += 1


# 通过生成器对象的 throw方法 抛出一个错误 可以向生成器发信号，让其必须处理一个错误
# 语法 throw(type,message)
# type 必须为BaseException的基类
# print(fibonacci(100).throw(ValueError, 'bad value'))
# for x in fibonacci(100):
#     print(x, end='\t')
