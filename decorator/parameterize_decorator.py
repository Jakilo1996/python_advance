# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     parameterize_decorator.py
# Author:      Jakiro
# Datetime:    2022/5/12 10:51
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 用装饰器试实现pytest的参数化装饰器
def param(params_names, data_lists):
    '''
    params_names 接收被装饰函数的变量名  多个变量名用 ， 分割
    datalists 接收被装饰函数的多组参数 列表套列表  每一组列表对应一组参数
    '''
    params_names = params_names.split(',')

    def wrapper(func):

        def inner():
            kwargs = {}
            for data_list in data_lists:
                # print( list(zip(params_names, data_list)))
                for param_name, data in zip(params_names, data_list):
                    kwargs[param_name] = data
                # print(kwargs)
                func(**kwargs)
                reason = func(**kwargs)
                return reason
        return inner

    return wrapper


list1 = [(1, 2), (3, 4), (5, 6)]


@param('a,b', list1)
def hello(a, b):
    print(a, b)


hello()
