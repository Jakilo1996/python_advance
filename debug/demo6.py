# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     demo6.py
# Author:      Jakiro
# Datetime:    2022/5/19 10:35
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


"""
属性管理 特殊方法：__getattr__ 、__getattribute__、__setattr__、__delattr__、__dir__、

"""

# __getattr__  访问对象属性到底 发生了什么？

class A:
    def __init__(self) -> None:
        self.test = "test"
        self.age = 12

p = A()
print(p.test)
print(p.tt)

# 如何解决 AttributeError
class NewA:
    def __init__(self) -> None:
        self.test = "test"
        self.age = 12

    def __getattr__(self, name):
        self.__dict__[name] = "nothing"
        return self.__dict__[name]


p = NewA()
print(p.test)
print(p.tt)


# __get attribute__ 其实每次在访问Getattr之前先访问的__getattribute__ 函数调用类的属性，每次都会执行 __getattribute__ 函数
from typing import Any

class A:
    def __init__(self) -> None:
        self.name ='bzy'
        self.ido = '12121'
    def __getattribute__(self, item: str)-> Any:
        """all id parames can't use"""
        if item.startswith('id'):
            return 'erro use'
        return object.__getattribute__(self, item)
    def __getattr__(self, item):
        self.__dict__[item]= "don't known"
        return "don't known"


p = A()
p.name
p.ido
p.tt

# 属性被保护后，如何在内部使用呢？
# 先来一个错误例子
class ErroA:
    count = 0
    def __new__(cls: type[Self]) -> Self:
        pass

    def __init__(self) -> None:
        self.name ='bzy'
        self.ido = '12121'
    def __getattribute__(self, item: str)-> Any:
        """all id parames can't use"""
        if item.startswith('id'):
            return 'erro use'
        return object.__getattribute__(self, item)
    def __getattr__(self, item):
        self.__dict__[item]= "don't known"
        return "don't known"

    def get_id(self):
        print(self.ido)

p = ErroA()
p.get_id()

# 即使在 类内部调用 属性名也是走的 __getattribute__ 函数
class NewA:
    def __init__(self) -> None:
        self.name ='bzy'
        self.ido = '12121'
    def __getattribute__(self, item: str)-> Any:
        """all id parames can't use"""
        if item.startswith('id'):
            # return 'erro use'
            return self.name
        return object.__getattribute__(self, item)
    def __getattr__(self, item):
        self.__dict__[item]= "don't known"
        return "don't known"

    def get_id(self):
         print(object.__getattribute__(self, "ido"))

p = NewA()
p.get_id()
"""
注意事项：
__getattribute__(self, name): name 是属性名，而不是属性值， 得到结果是属性值

不可在__getattribute__ 中 继续调用 类对象实例化的名字，否则会 递归
"""

class A:
    def __init__(self) -> None:
        self.name ='bzy'
        self.ido = '12121'
    def __getattribute__(self, item: str)-> Any:
        """all id parames can't use"""
        if item.startswith('id'):
            # return 'erro use'
            return object.__getattribute__(self, item)
        else:
            return self.name

p = A()
p.tt

""" __setattr__:     
__setattr__(self,key,value) 当一个属性被设置时的行为 
在类实例的每个属性进行赋值时，都会首先调用__setattr__()方法，
并在__setattr__()方法中将属性名和属性值添加到类实例的__dict__属性中。
"""

class A:
    def __init__(self, name, age) -> None:
        print(self.__dict__)
        self.name = name
        print(self.__dict__)
        self.age = age
        print(self.__dict__)

p = A("bzy", 25)


class A:
    count = 0
    __private = 11
    def __init__(self, name, age) -> None:
        print(self.__dict__)
        self.name = name
        print(self.__dict__)
        self.age = age
        self.__tt = "test"
        print(self.__dict__)


    def __setattr__(self, key: str, vaule: Any) -> None:
        print('-'*30)
        print('setting:{},with:{}'.format(key,vaule))
        print("current __dict__: {}".format(self.__dict__))
        self.__dict__[key] = vaule
p = A("bzy", 25)
print(A.__dict__)
print(p.__dict__)
print(A.__weakref__)



#  __delattr__ 方法
class A:
    def __init__(self, name, age) -> None:
        # print(self.__dict__)
        self.name = name
        # print(self.__dict__)
        self.age = age

    def __delattr__(self, item):
        print("执行了删除方法",item)
        super().__delattr__(item)

p = A("test", 12)
p.name

del p.age
p.age



# __dir__ 与 dir


class C:
    """cest"""
    def __init__ (self,):
        self.name = "C"
        self.add = "http://www.baidu.com"
    def say():
        pass


c = C()
print(dir(c))
print(c.__dir__())
# __doc__ 打印注释
print(c.__doc__)


# 顺序是不一样的

