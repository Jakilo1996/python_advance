# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     dynamic_state.py
# Author:      Jakiro
# Datetime:    2022/4/29 15:33
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------





class Person():
    sing1 = 1
    def __init__(self, name):
        self.name = name


# 动态添加属性：
# 动态添加属性，就是这个属性不是在类定义的时候添加的，而是在程序运行过程中添加的，动态添加属性有两种方法，第一个是直接通过对象名.属性名，第二个是通过setattr添加：


p = Person(2)
# 第一种：使用对象名.属性名添加，示例如下
p.age = 3

# hasattr是用来判断一个对象是否有某个属性，而setattr是用来给某个对象添加属性，并且指定这个属性的值。
# getattr是用来访问这个对象的某个属性，并且如果这个属性不存在的时候，可以指定一个默认值。


# 第二种：使用setattr函数添加，示例如下：
if not hasattr(p, 'country'):
    setattr(p, 'country', 'china')
#  打印所有属性
print(p.__dict__)



# 动态添加方法


# 动态添加实例方法：
# 动态添加方法，意思是方法不是在类定义的时候添加的。而是创建完这个对象后，在运行的时候添加的。
# 如果想要在运行的时候添加方法，这时候就应该使用到types.MethodType这个方法了，示例代码如下：
import types


def run(self,b):
    print(f'{self.name}:{b}')

# 其中types.MethodType的第一个参数是这个函数本身，第二个参数是在调用run这个函数的时候，传给run方法的第一个参数。
p.run = types.MethodType(run,p)

p.run(2)

# 动态添加类方法：
# 添加类方法，是把这个方法添加给类。因此添加类方法的时候不是给对象添加，而是给类添加。
# 并且添加类方法的时候不需要使用types.MethodType，直接将这个函数赋值给类就可以了，
# 但是需要使用classmethod装饰器将这个方法设置为一个类方法。示例代码如下：

@classmethod
def sing(cls):
    print(f'csl{cls.sing1}')

Person.sing = sing
Person.sing()

# 动态添加静态方法：
# 添加静态方法，是把这个方法添加给类。因此也是直接给类添加的，并且使用staticmethod这个装饰器。示例方法如下：

@staticmethod
def jump():
    print(f'jump:')

Person.jmup = jump
Person.jmup()


# 动态删除属性和方法：
# del 对象.属性名
# delattr(对象,"属性名")


# __slots__魔术变量：
# 有时候我们想指定某个类的对象，只能使用我指定的这些属性，不能随便添加其他的属性，那么这时候就可以使用__slots__魔术变量。
# 这个魔术变量是一个列表或者一个元组，里面存放属性的名字，以后在对象外面，就只能添加这个魔术变量中指定的属性，不能添加其他属性，示例代码如下：

class Person2(object):
    __slots__ = ('name','age')
    def __init__(self,name):
        self.name = name

p = Person2('zhiliao')
setattr(p,'height',180)
# 报错 AttributeError: 'Person2' object has no attribute 'height'