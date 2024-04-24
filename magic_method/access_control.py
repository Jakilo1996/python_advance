# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     access_control.py
# Author:      Jakiro
# Datetime:    2022/4/19 14:33
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# __setattr__：通过「.」设置属性或 setattr(key, value) 设置属性时调用
# __getattr__：访问不存在的属性时调用
# __delattr__：删除某个属性时调用
# __getattribute__：访问任意属性或方法时调用
# __dict__  魔术属性 这个属性装的是所有用户自定义的属性。
# __class__  魔术属性  用来返回这个对象所属的类。如果一个类调用这个属性，那么得到的是这个类的元类。
# dir()  和 __dir__ 打印子类和父类的所有方法和属性  顺序不同 和dict不同是  不会详细描述属性和方法的所属类型  dict只会打印类中定义的
# __doc__ 打印出所有类的注释

class Person1(object):
    def __setattr__(self, key, value):
        ''' 赋值属性'''
        if key not in ('name', 'age'):
            return

        if key == 'age' and value < 0:
            raise ValueError

        super(Person1, self).__setattr__(key, value)

    def __getattr__(self, item):
        '''访问某个不存在的属性 会调用这个方法
        '''
        return 'unknown attr'

    def __delattr__(self, key):
        if key == 'name':
            raise AttributeError
        super(Person1, self).__delattr__(key)

    def __getattribute__(self, item):
        """所有属性/方法调用都经过这里"""
        if item == 'money':
            return 100
        if item == 'hello':
            return self.say
        return super(Person1, self).__getattribute__(item)

    def say(self):
        return 'hello'




p1 = Person1()
p1.name = 'zhangsan'

print(p1.name)
# output
# zhangsan
print(p1.__dict__)  # __dict__  魔术属性 这个属性装的是所有用户自定义的属性。
# output
# {'name': 'zhangsan'}
print(p1.__class__)  # __class__  魔术属性  用来返回这个对象所属的类。如果一个类调用这个属性，那么得到的是这个类的元类。
print(Person1.__class__)
# output
# <class '__main__.Person1'>
print(p1.age)  # __delattr__  访问不存在的属性时调用
# output
# unknown attr



print(p1.money)
# output
# 100
print(p1.say())  # hello
print(p1.hello())  # hello  hello 调用__getattribute__ 间接调用say方法

# del p1.name
# output
# AttributeError'

'''
__setattr__
先来说 __setattr__，当我们在给一个对象进行属性赋值时，都会经过这个方法，在这个例子中，我们只允许对 name 和 age 这 2 个属性进行赋值，忽略了 gender 属性，除此之外，我们还对 age 赋值进行了校验。

通过 __setattr__ 方法，我们可以非常方便地对属性赋值进行控制。


__getattr__
再来看 __getattr__，由于我们在 __setattr__ 中忽略了对 gender 属性的赋值，所以当访问这个不存在的属性时，会调用 __getattr__ 方法，在这个方法中返回了默认值 unknown。

很多同学以为这个方法与 __setattr__ 方法对等的，一个是赋值，一个是获取。其实不然，__getattr__ 只有在访问「不存在的属性」时才会被调用，这里我们需要注意。

__getattribute__
了解了 __getattr__ 后，还有一个和它非常类似的方法：__getattribute__。

很多人经常把这个方法和 __getattr__ 混淆，通过例子我们可以看出，它与前者的区别在于：

__getattr__ 只有在访问不存在的属性时被调用，而 __getattribute__ 在访问任意属性时都会被调用
__getattr__ 只针对属性访问，而__getattribute__ 不仅针对所有属性访问，还包括方法调用
在上面的例子，虽然我们没有定义 money 属性和 hello 方法，但是在 __getattribute__ 里拦截到了这个属性和方法，就可以对其执行不同的逻辑。
即使在类的

__delattr__
最后，我们来看 __delattr__，它比较简单，当删除对象的某个属性时，这个方法会被调用，所以它一般会用在删除属性前的校验场景中使用。del 的时候的时候会调用

__dict__  魔术属性 这个属性装的是所有用户自定义的属性。
__class__  魔术属性  用来返回这个对象所属的类。如果一个类调用这个属性，那么得到的是这个类的元类。
'''
# 属性被保护后，如何在内部使用呢？
# 先来一个错误例子
from typing import Any
class ErroA:
    count = 0
    def __new__(cls, *args, **kwargs):
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

# p = ErroA()
# p.get_id()

# 即使在 类内部调用 属性名也是走的 __getattribute__ 函数，所以类中自己的getattribute 被重写 是无法绕过的
class NewA:
    def __init__(self) -> None:
        self.name ='bzy'
        self.ido = '12121'
    def __getattribute__(self, item: str)-> Any:
        """all id parames can't use"""
        if item.startswith('id'):
            # return 'erro use'
            return self.name
        # 通过父类的方法，调用实例的属性 可以绕过子类的调用限制
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
print('*'*20,A.count)
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
    def say(self):
        pass


c = C()
print(dir(c))
print(c.__dir__())
# __doc__ 打印注释
print(c.__doc__)


# 顺序是不一样的

