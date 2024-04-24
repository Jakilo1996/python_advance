# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     serializanle_object.py
# Author:      Jakiro
# Datetime:    2022/4/21 19:18
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 序列化对象

# 有时候一个对象，想要保存在硬盘中。这时候我们就需要使用到对象持久化的技术了。
# 在Python中，如果要将一个对象存储到硬盘中，需要使用pickle模块，其中dump方法可以将一个对象存到硬盘中，
# load方法可以从硬盘中加载一个对象。Python许多内置的数据结构是可以直接序列化的，比如：字典、列表、元组、字符串等。以下举几个例子来介绍下序列化的大体步骤：

# 写入对象到磁盘中
import pickle

data = {
    'foo': [1, 2, 3],
    'bar': ('hello', 'world'),
    'baz': True
}

jar = open('data.pkl', 'wb')
pickle.dump(data, jar)
jar.close()

# 从硬盘中加载对象
pkl_file = open('data.pkl', 'rb')
data2 = pickle.load(pkl_file)
print(data2)
pkl_file.close()


# 自己定义可持续化的对象：
#
#
# 自己定义的类的对象，默认情况下是不能持续化的。
# 如果想要让自定义的对象可持续化，那么应该实现两个魔术方法：第一个是__getstate__，
# 这个魔术方法在把对象存储到硬盘中的时候会调用的，会将这个方法的返回值存储进去，返回值应该是可以持续化的数据类型，比如字典、列表、字符串等；
# 第二个是__setstate__，这个魔术方法是从硬盘中加载对象的时候，会调用，会将你之前存储进去的值，通过参数的形式传递进来。以下举个例子来说明下：

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getstate__(self):
        return {'name': self.name, 'age': self.age}

    def __setstate__(self, state):
        self.name = state['name']
        self.age = state['age']

    def __str__(self):
        return f'<name:{self.name},age:{self.age}>'


def dump_obj():
    p1 = Person('zhiliao', 18)
    with open('data2.pkl', 'wb') as fp:
        pickle.dump(p1,fp)
        fp.close()


def load_obj():
    with open('data2.pkl', 'rb') as fp:
        p1 = pickle.load(fp)
        print(p1)
        fp.close()

dump_obj()
load_obj()

# output
# {'foo': [1, 2, 3], 'bar': ('hello', 'world'), 'baz': True}
# <name:zhiliao,age:18>
