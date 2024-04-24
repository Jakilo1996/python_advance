# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     with_context_manager.py
# Author:      Jakiro
# Datetime:    2022/5/9 17:13
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 将一个方法转化为 可以通过上下文调用  感觉很麻烦
class WithClass():
    '''
    params : enter_func  传入 传入一个方法或类的字符串（可以是内置方法），这个类或者方法的返回值必须是一个对象
    params : exit_func 传入一个字符串，这个方法必须为 enter_func返回对象的方法的字符串，（如果字符串含有，），则将依次使用enter_func返回对象执行这些方法
    params : enter_params 以列表形式传入 enter_func 需要传入的参数
    params : exit_params 以列表形式传入 enter_func 需要传入的参数  如果 exit_func 不为1  需要以列表套列表形式传入 并且与传入exit_func 一一对应
    '''

    def __init__(self, enter_func, exit_func, enter_params=None, exit_params=None, ):
        try:
            self.enter_func_obj = eval(f'{enter_func}(*{enter_params})')
        except Exception:
            raise ValueError('with_enter error wrong enter_params')
        # self.enter_func_obj = eval(f'{enter_func}(*{args}, **{kwargs})')
        if not ',' in exit_func:
            self.exit_func = exit_func
        else:
            self.exit_func = exit_func.split(',')
        self.exit_params = exit_params
        print(self.__doc__)
        # print(exit_params)

    def __enter__(self):
        print('__enter__')
        return self.enter_func_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

        # 通过给实例添加方法  不可行
        # def exit_func(obj):
        #     obj.self.exit_func()
        # import types
        # self.enter_func_obj.close = types.MethodType(exit_func,self.enter_func_obj)

        # 直接运行  不可行
        # self.exit_func()
        # 通过eval  不可行
        # eval(f'{self.enter_func_obj}.{self.exit_func}()')

        # 方法八：使用 attrgetter 获取执行
        # 在 operator 这个内置库中，有一个获取属性的方法，叫 attrgetter ，获取到函数后再执行。
        # from operator import attrgetter
        # caller = attrgetter(self.exit_func)
        # caller(self.enter_func_obj)

        # 方法九：使用 methodcaller 执行
        # 同样还是 operator 这个内置库，有一个 methodcaller 方法，使用它，也可以做到动态调用实例方法的效果。
        from operator import methodcaller
        from collections.abc import Iterable
        if isinstance(self.exit_func, str):
            # 需要参数的 单exit方法
            if self.exit_params:
                caller = methodcaller(self.exit_func, *self.exit_params)
            else:
                caller = methodcaller(self.exit_func)
            try:
                caller(self.enter_func_obj)
            except:
                raise ValueError('with_exit error')
        elif isinstance(self.exit_func, list):
            for i, cur_exit_func in enumerate(self.exit_func):
                if self.exit_params[i]:
                    # print(self.exit_params[i])
                    if isinstance(self.exit_params[i], Iterable):
                        caller = methodcaller(cur_exit_func, *self.exit_params[i])
                    else:
                        caller = methodcaller(cur_exit_func, self.exit_params[i])
                else:
                    caller = methodcaller(cur_exit_func)
                try:
                    caller(self.enter_func_obj)
                except:
                    raise ValueError('with_exit error wrong exit_params')
        # 下面语句 如果报错 代表成功关闭文件
        # self.enter_func_obj.read()

        # print(self.enter_func_obj.show())
        # 如果 with 内有异常发生 抛出异常
        if exc_type is not None:
            # print(exc_type)
            raise exc_type('with_context run error')
        print('end_exit')


# case2 自定义一个装饰器  可以将任意一个带参数的方法修饰为with上下文

from functools import wraps


class ContextMangerBase():
    def __init__(self, func, args, kwargs):
        # print(args)
        self.gene = func(*args, **kwargs)

    def __enter__(self):
        print('__enter__')
        try:
            return next(self.gene)
        except StopIteration:
            raise RuntimeError('generation did`t yield') from None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        if exc_type == None:
            try:
                print('__exit__try')
                next(self.gene)
            # 此处的作用是为了忽略 迭代对象 第二次next 的 StopIteration异常
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")

        else:
            try:
                self.gene.throw(exc_type, exc_val, exc_tb)
            except:
                raise
            raise RuntimeError("generator didn't stop after throw()")


def context_manager(func, ):
    '''
    params: func 被装饰的函数对象，必须是一个生成器函数，缺省参数为装饰器函数的实参
    '''

    @wraps(func)
    def inner(*args, **kwargs):
        return ContextMangerBase(func, args, kwargs)

    return inner


@context_manager
# 使用装饰器方法 需要自定义生成器函数  yield前 为with前执行 yield 必须返回需要在with中处理的对象， yield 后为 with 后处理
def file_open(file_path, mode):
    try:
        1 / 0
        fp = open(file_path, mode)
        yield fp
    finally:
        #
        fp.close()
        # 此处是为了 试验关闭是否执行成功
        # print(fp.read())
    # yield 0


# with file_open('aaa.txt','r') as fp:
#     # print(fp.__dict__)
#     print(fp.read())


with WithClass('open', 'close', ('aaa.txt', 'r')) as fp:
    print(fp.read())
