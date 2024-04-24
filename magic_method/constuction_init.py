# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     constuction_init.py
# Author:      Jakiro
# Datetime:    2022/4/15 16:42
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# __init__
# __new__
# __del__

class Person(object):
    __person = 1

    def __new__(cls, *args, **kwargs):
        print('call __new__')
        return object.__new__(cls)

    # __init__
    # 关于构造与初始化的魔法方法，我们使用最频繁的一个就是 __init__ 了。
    #
    # 我们在定义类的时候，通常都会去定义构造方法，它的作用就是在初始化一个对象时，定义这个对象的初始值。
    def __init__(self, name, age):
        print('call __init__')
        self.name = name
        self.age = age


p = Person('张三', 20)
# 通过歪方法调用私有属性
print(p._Person__person)
print(Person.__dict__)
print(p.__dict__)


# print(Person.__)

# Output:
# call __new__
# call __init__

# 在初始化一个类的属性时，除了使用 __init__ 之外，还可以使用 __new__ 这个方法。
# __new__
# 我们在平时开发中使用的虽然不多，但是经常能够在开源框架中看到它的身影。实际上，这才是「真正的构造方法」。
### 单列类  无论实例化几次 返回都是同一个实例
#  由于 __new__ 优先于 __init__ 调用，而且它返回的是一个实例，所以我们可以利用这个特性，在 __new__ 方法中，每次返回同一个实例来实现一个单例类：
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


class MySingleton(Singleton):
    pass


a = Singleton()
c = Singleton()
# b = MySingleton()
# print(a is b)
print(repr(a))

#  另外一个使用场景是，当我们需要继承内置类时，例如想要继承 int、str、tuple，就无法使用 __init__ 来初始化了，只能通过 __new__ 来初始化数据：

# class g(float):
#     '''千克转克'''
#
#     def __new__(cls, *args, **kwargs):
#         return float.__new__(cls, args[0] * 1000)
#
#
# c = g(5)
# print(c)
# print(c + 1000)  # 200 由于继承了float，所以可以直接运算，非常方便！


#  除此之外，__new__ 比较多的应用场景是配合「元类」使用


# __del__ 这个方法就是我们经常说的「析构方法」，也就是在对象被垃圾回收时被调用。
#
# 但是请注意，当我们执行 del obj 时，这个方法不一定会执行。
#
# 由于 Python 是通过引用计数来进行垃圾回收的，如果这个实例在执行 del 时，还被其他对象引用，那么就不会触发执行 __del__ 方法。

# class Person2():
#     def __del__(self):
#         pass
# print('__del__')


# 由于我们没有对实例进行任何引用操作时，所以 __del__ 在程序退出时被调用。
# p2 = Person2()
# print('code_exit')


# # Output:
# # exit
# # __del__


# 同样地，由于实例没有被其他对象所引用，当我们手动销毁这个实例时，__del__ 被调用后程序正常退出。
# p3 = Person2()
# del p3
# print("code_exit")

# Output:
# __del__
# exit


# p4 = Person2()
# p5 = p4
# del p4
# print("code_exit")

# Output:
# exit
# __del__

# 可以看到，如果这个实例有被其他对象引用，尽管我们手动销毁这个实例，但不会触发 __del__ 方法，而是在程序正常退出时被调用执行。

# 通常来说，__del__ 这个方法我们很少会使用到，除非需要在显示执行 del 执行特殊清理逻辑的场景中才会使用到。

# 但另一方面，也给我们一个提醒，当我们在对文件、Socket 进行操作时，如果要想安全地关闭和销毁这些对象，最好是在 try 异常块后的 finally 中进行关闭和释放操作，从而避免资源的泄露。

'''
# __init__
    # 关于构造与初始化的魔法方法，我们使用最频繁的一个就是 __init__ 了。
    #
    # 我们在定义类的时候，通常都会去定义构造方法，它的作用就是在初始化一个对象时，定义这个对象的初始值。

# 在初始化一个类的属性时，除了使用 __init__ 之外，还可以使用 __new__ 这个方法。
# __new__
# 我们在平时开发中使用的虽然不多，但是经常能够在开源框架中看到它的身影。实际上，这才是「真正的构造方法」。
### 单列类  无论实例化几次 返回都是同一个实例
#  由于 __new__ 优先于 __init__ 调用，而且它返回的是一个实例，所以我们可以利用这个特性，在 __new__ 方法中，每次返回同一个实例来实现一个单例类：

#  另外一个使用场景是，当我们需要继承内置类时，例如想要继承 int、str、tuple，就无法使用 __init__ 来初始化了，只能通过 __new__ 来初始化数据：

'''

# 超级管理员登录 拿cookie
# 创建角色   # 所有角色对应params value
# 创建并关联角色 # 关联的时候要怎么传
# 管理员登录验证 过第一次登录 更新cookie


# 普通用户，一个url在多个key下的情况，普通的所有