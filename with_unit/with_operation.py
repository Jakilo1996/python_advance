# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     with_operation.py
# Author:      Jakiro
# Datetime:    2022/5/7 13:32
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 上下文管理器
# 语法格式
# with context_expression [as target(s)]:
#     with-body

# with 语法非常简单，我们只需要 with 一个表达式，然后就可以执行自定义的业务逻辑。
#
# 但是，with 后面的表达式是可以任意写的吗？
#
# 答案是否定的。要想使用 with 语法块，with 后面的的对象需要实现「上下文管理器协议」。
# __enter__：在进入 with 语法块之前调用，返回值会赋值给 with 的 target
# __exit__：在退出 with 语法块时调用，一般用作异常处理

# 举例
class TestContext():

    def __enter__(self):
        print('__enter__')
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exc_type: %s' % exc_type)
        print('exc_value: %s' % exc_val)
        print('exc_tb: %s' % exc_tb)


# with TestContext() as t:
#     print(f't:{t}')
#     print('a')
# print()


# Output:
# __enter__
# t: 1
# exc_type: None
# exc_value: None
# exc_tb: None

# 在这个例子中，我们定义了 TestContext 类，它分别实现了 __enter__ 和 __exit__ 方法。
#
# 这样依赖，我们就可以把 TestContext 当做一个「上下文管理器」来使用，也就是通过 with TestContext() as t 方式来执行。
#
# 从输出结果我们可以看到，具体的执行流程如下：

# __enter__ 在进入 with 语句块之前被调用，这个方法的返回值赋给了 with 后的 t 变量
# __exit__ 在执行完 with 语句块之后被调用
# 如果在 with 语句块内发生了异常，那么 __exit__ 方法可以拿到关于异常的详细信息：
#
# exc_type：异常类型
# exc_value：异常对象
# exc_tb：异常堆栈信息
# 我们来看一个发生异常的例子，观察 __exit__ 方法拿到的异常信息是怎样的：

# with TestContext() as t:
#     # 这里会发生异常
#     print('b')
#     a = 1 / 0
#     print('t: %s' % t)


# Output:
# __enter__
# exc_type: <type 'exceptions.ZeroDivisionError'>
# exc_value: integer division or modulo by zero
# exc_tb: <traceback object at 0x10d66dd88>
# Traceback (most recent call last):
#   File "base.py", line 16, in <module>
#     a = 1 / 0
# ZeroDivisionError: division by zero


# 回到最开始我们讲的，使用 with 读取文件的例子。之所以 with 能够自动关闭文件资源，
# 就是因为内置的文件对象实现了「上下文管理器协议」，这个文件对象的 __enter__ 方法返回了文件句柄，
# 并且在 __exit__ 中实现了文件资源的关闭，另外，当 with 语法块内有异常发生时，会抛出异常给调用者

# 伪代码可以这么写：
# class File:
#     def __init__(self, file_path, mode):
#         self.file_obj = open(file_path, mode)
#
#     def __enter__(self):
#         print('__enter__')
#         return self.file_obj
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print('__exit__')
#         # with 退出时释放文件资源
#         self.file_obj.close()
#         # 如果 with 内有异常发生 抛出异常
#         if exc_type is not None:
#             print(exc_type)
#             raise exc_type
# #
# #
# with File('file.txt', 'r') as fp:
#     for line in fp:
#         print(line)
#     1 / 0

# 这里我们小结一下，通过对 with 的学习，我们了解到，with 非常适合用需要对于上下文处理的场景，
# 例如操作文件、Socket，这些场景都需要在执行完业务逻辑后，释放资源。

# 将一个方法转化为 可以通过上下文调用
# class WithClass():
#     '''
#     params : enter_func  传入 传入一个方法或类的字符串（可以是内置方法），这个类或者方法的返回值必须是一个对象
#     params : exit_func 传入一个字符串，这个方法必须为 enter_func返回对象的方法，（如果字符串含有，），则将依次使用enter_func返回对象执行这些方法
#     params : enter_params 以列表形式传入 enter_func 需要传入的参数
#     params : exit_params 以列表形式传入 enter_func 需要传入的参数  如果 exit_func 不为1  需要以列表套列表形式传入 并且与传入exit_func 一一对应
#     '''
#
#     def __init__(self, enter_func, exit_func, enter_params=None, exit_params=None,):
#         try:
#             self.enter_func_obj = eval(f'{enter_func}(*{enter_params})')
#         except Exception:
#             raise ValueError('with_enter error wrong enter_params')
#         # self.enter_func_obj = eval(f'{enter_func}(*{args}, **{kwargs})')
#         if not ',' in exit_func:
#             self.exit_func = exit_func
#         else:
#             self.exit_func = exit_func.split(',')
#         self.exit_params = exit_params
#         print(self.__doc__)
#         # print(exit_params)
#
#     def __enter__(self):
#         print('__enter__')
#         return self.enter_func_obj
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__')
#
#         # 通过给实例添加方法  不可行
#         # def exit_func(obj):
#         #     obj.self.exit_func()
#         # import types
#         # self.enter_func_obj.close = types.MethodType(exit_func,self.enter_func_obj)
#
#         # 直接运行  不可行
#         # self.exit_func()
#         # 通过eval  不可行
#         # eval(f'{self.enter_func_obj}.{self.exit_func}()')
#
#         # 方法八：使用 attrgetter 获取执行
#         # 在 operator 这个内置库中，有一个获取属性的方法，叫 attrgetter ，获取到函数后再执行。
#         # from operator import attrgetter
#         # caller = attrgetter(self.exit_func)
#         # caller(self.enter_func_obj)
#
#         # 方法九：使用 methodcaller 执行
#         # 同样还是 operator 这个内置库，有一个 methodcaller 方法，使用它，也可以做到动态调用实例方法的效果。
#         from operator import methodcaller
#         from collections.abc import Iterable
#         if isinstance(self.exit_func, str):
#             # 需要参数的 单exit方法
#             if self.exit_params:
#                 caller = methodcaller(self.exit_func, *self.exit_params)
#             else:
#                 caller = methodcaller(self.exit_func)
#             try:
#                 caller(self.enter_func_obj)
#             except:
#                 raise ValueError('with_exit error')
#         elif isinstance(self.exit_func, list):
#             for i, cur_exit_func in enumerate(self.exit_func):
#                 if self.exit_params[i]:
#                     # print(self.exit_params[i])
#                     if isinstance(self.exit_params[i],Iterable):
#                         caller = methodcaller(cur_exit_func, *self.exit_params[i])
#                     else:
#                         caller = methodcaller(cur_exit_func, self.exit_params[i])
#                 else:
#                     caller = methodcaller(cur_exit_func)
#                 try:
#                     caller(self.enter_func_obj)
#                 except:
#                     raise ValueError('with_exit error wrong exit_params')
#         # 下面语句 如果报错 代表成功关闭文件
#         # self.enter_func_obj.read()
#
#         # print(self.enter_func_obj.show())
#         # 如果 with 内有异常发生 抛出异常
#         if exc_type is not None:
#             # print(exc_type)
#             raise exc_type('with_context run error')
#         print('end_exit')



# case 1

# with WithClass('open', 'close', 'file.txt', 'r') as fp:
#     for line in fp:
#         print(line)

# case2
class Person():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('init', self.a, self.b)

    def clear(self):
        self.a = 0
        self.b = 0
        print('clear', self.a, self.b)

    def change(self, c):
        self.a = c
        self.b = c
        print('change', self.a, self.b)

    def change1(self, c, d):
        self.a = c
        self.b = d
        print('change1', self.a, self.b)

    def show(self):
        print('show', self.a, self.b)
#
#
# with WithClass('Person', 'change,change1', (1, 2), (1, (2, 3))) as p1:
#     p1.clear()
