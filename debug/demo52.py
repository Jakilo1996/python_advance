# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo52.py
# Author:      Jakiro
# Datetime:    2023/1/12 16:44
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import requests
class Singleton():
    '''
    单例
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        print(type(cls._instance))
        return cls._instance

    def __init__(self, a):
        self.a = a


class MySingleton(Singleton):
    pass


a = Singleton(requests.session())
print(id(a.a))
# c = Singleton()
b = MySingleton(requests.session())
print(id(a.a))
print(a is b)

