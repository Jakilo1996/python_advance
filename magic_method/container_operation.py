# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     container_operation.py
# Author:      Jakiro
# Datetime:    2022/4/21 10:24
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# __setitem__
# __getitem__
# __delitem__
# __len__
# __iter__
# __contains__
# __reversed__
#
# Python 中常见的容器类型有：
#
# 字典
# 元组
# 列表
# 字符串
# 因为它们都是「可迭代」的。可迭代是因为，它们都实现了容器协议，也就是我们下面要介绍到的魔法方法。


class MyList():
    '''自定义list类'''

    def __init__(self, values=None):
        # 初始化自定义List
        self.values = values or []

    def __setitem__(self, key, value):
        # 添加元素
        self.values[key] = value

    def __getitem__(self, key):
        # 获取元素
        return self.values[key]

    def __delitem__(self, key):
        # 删除元素
        del self.values[key]

    def __len__(self):
        # 自定义list元素个数
        return len(self.values)

    def __iter__(self):
        # 可迭代
        self._index = 0
        return self

    def __next__(self):
        # 迭代的具体细节
        if self._index >= len(self.values):
            raise StopIteration
        value = self.values[self._index]
        self._index += 1
        return value

    def __contains__(self, item):
        # 元素是否在列表中
        return item in self.values

    def __reversed__(self):
        # 反转
        # 如果不加list  reversed(self.values) output <list_reverseiterator object at 0x7fccdff12bd0>
        # return reversed(self.values)
        return list(reversed(self.values))


my_list = MyList([1, 2, 3, 4, 5])

# __getitem__  调用instance[]的时候会调用
print(my_list[0])
# output
# 1

# __setitem__ 调用 instance[] = 赋值的时候会调用
my_list[1] = 20
print(my_list[1])
# output
# 20

# __len__  len(instance) 时会调用
print(len(my_list))
# output
# 5

# __del__ del(instance) 时会调用 删除一个元素
del my_list[0]
print(my_list)

# 通过魔法属性 查看所有的自定义属性
print(my_list.__dict__)

# 通过 next 调用迭代器  要先调用 iter方法
a = my_list.__iter__()
for i in range(0, 4):
    print(a.__next__())
# output
# 1
# 2
# 3
# 4
# 5
print([i for i in my_list])
# output
# [1, 2, 3, 4, 5]

# __contains__  调用in的时候会调用
print(1 in my_list)
# output
# True

# # __reversed__  调用反转的时候会调用
print(reversed(my_list))
# output
# [5, 4, 3, 2, 1]

'''
在这个例子中，我们自己实现了一个 MyList 类，在这个类中，定义了很多容器类的魔法方法。这样一来，我们这个 MyList 类就可以像操作普通 list 一样，通过切片的方式添加、获取、删除、迭代元素了。

__setitem__
当我们执行 my_list[1] = 20 时，就会调用 __setitem__ 方法，这个方法主要用于向容器内添加元素。

__getitem__
当我们执行 my_list[0] 时，就会调用 __getitem__ 方法，这个方法主要用于从容器中读取元素。

__delitem__
当我们执行 del my_list[0] 时，就会调用 __delitem__ 方法，这个方法主要用于从容器中删除元素。

__len__
当我们执行 len(my_list) 时，就会调用 __len__ 方法，这个方法主要用于读取容器内元素的数量。

__iter__
这个方法我们需要重点关注，为什么我们可以执行 [i for i in my_list]？就是因为我们定义了 __iter__。

这个方法的返回值可以有两种：

返回 iter(obj)：代表使用 obj 对象的迭代协议，一般 obj 是内置的容器对象
返回 self：代表迭代的逻辑由本类来实现，此时需要重写 next 方法，实现自定义的迭代逻辑
在这个例子中，__iter__ 返回的是 self，所以我们需要定义 next 方法，实现自己的迭代细节。

next 方法使用一个索引变量，用于记录当前迭代的位置，这个方法每次被调用时，都会返回一个元素，当所有元素都迭代完成后，这个方法会返回 StopIteration 异常，此时 for 会停止迭代。

在 Python3 中，已不再使用 next 方法，取而代之的是 __next__。
__contains__
从名字也能看出来，这个方法是在执行 1 in my_list 时触发，用于判断某个元素是否存在于容器中。

__reversed__
这个方法在执行 reversed(my_list) 时触发，用于反转容器的元素，具体的反转逻辑我们也可以自己实现。
'''


# case 自定义字典

class MyDict():
    def __init__(self, items=None):

        self.items = items
        self.keys = list(self.items.keys())

    def __setitem__(self, key, value):
        if key not in self.keys:
            self.items[str(key)] = value
            self.keys.append(str(key))
        else:
            self.items[str(key)] = value

    def __getitem__(self, item):
        if item in self.keys:
            return self.items[str(item)]
        else:
            return self.__missing__(item)

    def __delitem__(self, key):
        del self.items[str(key)]
        self.keys.remove(key)

    def __len__(self):
        return len(self.items)

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(f'key:{key}')

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.keys):
            raise StopIteration
        value = self.items[self.keys[self._index]]
        self._index += 1
        return value

    def __contains__(self, item):
        return str(item) in self.keys

    def __reversed__(self):
        self.keys = list(reversed(self.keys))


dict1 = MyDict({'a': 1, 'b': 2, 'c': 3})
dict1['d'] = 2  # 执行_setitem__

print(dict1['d'])  # 执行_getitem__
# output
# 2

# dict1['e']  # __missing__ 执行
# output
# KeyError: 'key:e'

print(len(dict1))  # __len__

print(dict1.__dict__)  # 魔法属性
# output
# {'items': {'a': 1, 'b': 2, 'c': 3, 'd': 2}, 'keys': ['a', 'b', 'c', 'd']}

# 执行__iter__  __next__

d = dict1.__iter__()
for i in range(0,4):
    print(next(d))

# output
# 1
# 2
# 3
# 2

print([i for i in dict1])  # 执行__iter__  __next__
# output
# [1, 2, 3, 2]

print('c' in dict1)  # 执行__contain__
# output
# True

reversed(dict1)  # __reversed__
print([i for i in dict1])
# output
# [2, 3, 2, 1]
