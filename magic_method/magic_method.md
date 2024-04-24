#### 魔法方法概览 首先，我们先对 Python 中的魔法方法进行归类，常见的魔法方法大致可分为以下几类：

构造与初始化 类的表示 访问控制 比较操作 容器类操作 可调用对象 序列化

构造与初始化 首先，我们来看关于构造与初始化相关的魔法方法，主要包括以下几种：

__init__
__new__
__del__
__init__

__init__
关于构造与初始化的魔法方法，我们使用最频繁的一个就是 __init__ 了。 我们在定义类的时候，通常都会去定义构造方法，它的作用就是在初始化一个对象时，定义这个对象的初始值。

我们在定义类的时候，通常都会去定义构造方法，它的作用就是在初始化一个对象时，定义这个对象的初始值。

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('张三', 25)
p2 = Person('李四', 30)
```

##### __new__
在初始化一个类的属性时，除了使用 __init__ 之外，还可以使用 __new__ 这个方法。

我们在平时开发中使用的虽然不多，但是经常能够在开源框架中看到它的身影。实际上，这才是「真正的构造方法」。

单列类  无论实例化几次 返回都是同一个实例

由于 __new__ 优先于 __init__ 调用，而且它返回的是一个实例，所以我们可以利用这个特性，在 __new__ 方法中，每次返回同一个实例来实现一个单例类：
```python
class Singleton():
    '''
    单例
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MySingleton(Singleton):
    pass


a = Singleton()
b = MySingleton()
print(a is b)
print(repr(a))
```

另外一个使用场景是，当我们需要继承内置类时，例如想要继承 int、str、tuple，就无法使用 __init__ 来初始化了，只能通过 __new__ 来初始化数据：
```python
class g(float):
    '''千克转克'''

    def __new__(cls, *args, **kwargs):
        return float.__new__(cls, args[0] * 1000)


c = g(5)
print(c)
print(c + 1000)  # 200 由于继承了float，所以可以直接运算，非常方便！
```

##### __str__ / __repr__

__str__ 强调可读性，而 __repr__ 强调准确性 / 标准性

__str__ 的目标人群是用户，而 __repr__ 的目标人群是机器，__repr__ 返回的结果是可执行的，通过 eval(repr(obj)) 可以正确运行

占位符 %s 调用的是 __str__，而 %r 调用的是 __repr__ 方法

 __str__强调可以理解展示，__repr__强调创建过程

在pycharm中，如果将一个对象创建完成后，放到一个列表中，然后再打印这个列表，那么会打印这个列表中所有的对象，这时候会调用__repr__魔术方法，

通过case2 和 case3 可以看出

如果只定义了__str__, repr(person) 输出<__main__.Person3 object at 0x7fa0c39f70d0>

如果只定义 __repr__, str(person)和repr(person)的输出结果相同

也就是说，__repr__在表示类的时候 是第一级的，如果不定义__str__，那么__str__= __repr__.

而 __str__展示类时是次级的，如果没有定义__repr__，那么repr(person)将会展示缺省的定义  <__main__.Person3 object at 0x7fa0c39f70d0>

'%s' 调用__str__方法   '%r' 调用__repr__方法

```python
class Person2():
    #  举例__str__\__repr__的常用方法
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def __str__(self):
        # 格式化 友好对用户人类展示
        return f'姓名：{self.name} 年龄：{self.age}'

    def __repr__(self):
        # 标准化  机器展示
        return f'Person2(name="{self.name}", age={self.age})'


person1 = Person2(name='qiujie', age=26)

# 强调对用户友好
print(str(person1))
print(person1.__str__())
print('%s' % person1)

# output
# 姓名：qiujie 年龄：26

# 强调对机器友好 结果 eval 可执行
print(repr(person1))
print(person1.__repr__())
print('%r' % person1)


```

##### __hash__
__hash__ 方法返回一个整数，用来表示实例对象的唯一标识，配合 __eq__ 方法，可以判断两个对象是否相等：

__eq__ 用于通过对比唯一标识符，返回 一个布尔值

如果我们需要判断两个对象是否相等，只需要我们重写 __hash__ 和 __eq__ 方法就可以了。

标识符相同 == 视为同一个对象

标识符相同 is判断的时候  不为同一个对象

此外，当我们使用 set 时，在 set 中存放这些对象，也会根据这两个方法进行去重操作。

##### __bool__
当调用 bool(obj) 时，会调用 __bool__ 方法，返回 True 或 False

```python
class Person2():
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return f'Person({self.uid})'

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid

    def __bool__(self):
        return self.uid > 10


person4 = Person2(5)
person5 = Person2(15)
print(bool(person4))
print(person4.__bool__())
# output
# False
print(bool(person5))
print(person5.__bool__())
# output
# True
```

#### 访问控制
__setattr__：通过「.」设置属性或 setattr(key, value) 设置属性时调用

__getattr__：访问不存在的属性时调用

__delattr__：删除某个属性时调用

__getattribute__：访问任意属性或方法时调用

__dict__  魔术属性 这个属性装的是所有用户自定义的属性。

__class__  魔术属性  用来返回这个对象所属的类。如果一个类调用这个属性，那么得到的是这个类的元类。

__doc__  魔术属性，描述该对象的作用，一般为``````` 中描述的内容

```python
class Person1():
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
'''
先来说 __setattr__，当我们在给一个对象进行属性赋值时，都会经过这个方法，在这个例子中，我们只允许对 name 和 age 这 2 个属性进行赋值，忽略了 gender 属性，除此之外，我们还对 age 赋值进行了校验。

通过 __setattr__ 方法，我们可以非常方便地对属性赋值进行控制。


__getattr__
再来看 __getattr__，由于我们在 __setattr__ 中忽略了对 gender 属性的赋值，所以当访问这个不存在的属性时，会调用 __getattr__ 方法，在这个方法中返回了默认值 unknown。

很多同学以为这个方法与 __setattr__ 方法对等的，一个是赋值，一个是获取。其实不然，__getattr__ 只有在访问「不存在的属性」时才会被调用，这里我们需要注意。

__getattribute__
了解了 __getattr__ 后，还有一个和它非常类似的方法：__getattribute__。

很多人经常把这个方法和 __getattr__ 混淆，通过例子我们可以看出，它与前者的区别在于：

__getattr__ 只有在访问不存在的属性时被调用，而 __getattribute__ 在访问任意属性时都会被调用
__getattr__ 只针对属性访问，而__getattribute__ 不仅针对所有属性访问，还包括方法调用，优先级 先执行__getattribute__
在上面的例子，虽然我们没有定义 money 属性和 hello 方法，但是在 __getattribute__ 里拦截到了这个属性和方法，就可以对其执行不同的逻辑。

__delattr__
最后，我们来看 __delattr__，它比较简单，当删除对象的某个属性时，这个方法会被调用，所以它一般会用在删除属性前的校验场景中使用。

__dict__  魔术属性 这个属性装的是所有用户自定义的属性。
__class__  魔术属性  用来返回这个对象所属的类。如果一个类调用这个属性，那么得到的是这个类的元类。
'''
```

#### 比较操作
```python

# __cmp__
# __eq__
# __ne__
# __lt__
# __gt__


# __cmp__
# 从名字我们就能看出来这个魔法方法的作用，当我们需要比较两个对象时，我们可以定义 __cmp__ 来实现比较操作。

class Person1():
    def __init__(self, uid, name, salary):
        self.uid = uid
        self.name = name
        self.salary = salary

    def __cmp__(self, other):
        if self.uid == other.uid:
            return 0
        if self.uid > other.uid:
            return 1
        if self.uid < other.uid:
            return -1
        raise ValueError

    def __eq__(self, other):
        """对象 == 判断"""
        return self.uid == other.uid

    def __ne__(self, other):
        """对象 != 判断"""
        return self.uid != other.uid

    def __lt__(self, other):
        """对象 < 判断 根据len(name)"""
        return len(self.name) < len(other.name)

    def __gt__(self, other):
        """对象 > 判断 根据alary"""
        return self.salary > other.salary


p1 = Person1(1, 'zhangsan', 1000)
p2 = Person1(1, 'list', 2000)
p3 = Person1(2, 'wangwu', 3000)
print(p1.__cmp__(p2))
print(p1 == p2)
print(p1!=p2)
print(p1<p2)
print(p1>p2)
# output
# 0
# True
# False
# False
# False

# __eq__
# __eq__ 我们在上一篇文章已经介绍过，它配合 __hash__ 方法，可以判断两个对象是否相等。
#
# 但在这个例子中，当判断两个对象是否相等时，实际上我们比较的是 uid 这个属性。
#
# __ne__
# 同样地，当需要判断两个对象不相等时，会调用 __ne__ 方法，在这个例子中，我们也是根据 uid 来判断的。
#
# __lt__
# 当判断一个对象是否小于另一个对象时，会调用 __lt__ 方法，在这个例子中，我们根据 name 的长度来做的比较。
#
# __gt__
# 同样地，在判断一个对象是否大于另一个对象时，会调用 __gt__ 方法，在这个例子中，我们根据 salary 属性判断。
```

####  容器类操作
__setitem__
__getitem__
__delitem__
__len__
__iter__
__contains__
__reversed__

Python 中常见的容器类型有：

字典
元组
列表
字符串
因为它们都是「可迭代」的。可迭代是因为，它们都实现了容器协议，也就是我们下面要介绍到的魔法方法。

case1
```python
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

```
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

可变容器可以对容器中的元素进行更改，比如删除一个元素，添加一个容器。而不可变容器不能做这些操作。因此如果你向定义一个不可变容器，那么不应该实现__setitem__、__delitem__方法。
'''

case2
```python
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

```
#### 运算符
运算符魔术方法
一元操作符和函数：

__pos__(self)魔术方法：在这个对象前面使用正号的时候执行的方法。
__neg__(self)魔术方法：在这个对象前面使用负号的时候执行的方法。
__abs__(self)魔术方法：在这个对象上使用abs函数的时候执行的方法。
__invert__(self)魔术方法：在这个对象前面使用~的时候执行的方法。
```python
class Coornidate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __pos__(self)魔术方法：在这个对象前面使用正号的时候执行的方法。
    def __pos__(self):
        return self

    def __neg__(self):
        return Coornidate(-self.x, -self.y)

    def __abs__(self):
        return Coornidate(abs(self.x), abs(self.y))

    def __invert__(self):
        return Coornidate(255 - self.x, 255 - self.y)

    def __str__(self):
        return f'({self.x},{self.y})'


c1 = Coornidate(-1, 2)
c2 = +c1  # __pos__  x = -1 y =2
c3 = -c1  # __neg__ x =1 y =-2
c4 = abs(c1)  # __abs__  x =1 y=2
c5 = ~c1  # __invert__ x= 256 y= 253
print(c5)

```

普通算数操作符：
__add__(self,other)魔术方法：在两个对象相加的时候执行的方法。
__sub__(self,other)魔术方法：在两个对象相减的时候执行的方法。
__mul__(self,other)魔术方法：在两个对象相乘的时候执行的方法。
__floordiv__(self,other)魔术方法：在两个对象使用//运算的时候执行的方法。
__div__(self,other)魔术方法：在两个对象使用/运算的时候执行的方法。
__truediv__(self,other)魔术方法：在两个对象之间使用真除的时候执行的方法。在Python3中使用/运算的时候会执行这个方法。在Python2中，默认使用__div__方法，如果from __future__ import division，那么将会使用__truediv__方法。
__mod__(self,other)魔术方法：在使用%取模运算的时候执行的方法。
```python
class GeneralOperator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return GeneralOperator(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return GeneralOperator(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return GeneralOperator(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other):
        print('__floordiv__')
        return GeneralOperator(self.x // other.x, self.y // other.y)

    def __divmod__(self, other):
        print('__divmod__')
        return GeneralOperator(self.x / other.x, self.y / other.y)

    def __truediv__(self, other):
        print('__truediv__')
        return GeneralOperator(self.x / other.x, self.y / other.y)

    def __mod__(self, other):
        return GeneralOperator(self.x % other.x, self.y % other.y)

    def __str__(self):
        return f'({self.x},{self.y})'


g7 = GeneralOperator(4, 6)
g8 = GeneralOperator(3, 4)
print(g7 + g8)  # __add__   (7,10)
print(g7 - g8)  # __sub__   (1,2)
print(g7 * g8)  # __mul__    (12,24)
print(g7 / g8)  # __truediv__  (1.3333333333333333,1.5)
print(g7 % g8)  # __mod__  (1,2)
```

增量赋值：
__iadd__(self,other)魔术方法：在给对象做+=运算的时候会执行的方法。
__isub__(self,other)魔术方法：在给对象做-=运算的时候会执行的方法。
__imul__(self,other)魔术方法：在给对象做*=运算的时候会执行的方法。
__idiv__(self,other)魔术方法：在给对象做/=运算的时候会执行的方法。
__itruediv__(self,other)魔术方法：在给对象做真/=运算的时候会执行的方法。

```python
class AugmentedAssignment():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other
        self.y += other
        return self

    def __isub__(self, other):
        return AugmentedAssignment(self.x - other, self.y - other)

    def __imul__(self, other):
        return AugmentedAssignment(self.x * other, self.y * other)

    def __itruediv__(self, other):
        return AugmentedAssignment(self.x / other, self.y * other)

    def __str__(self):
        return f'({self.x},{self.y})'


a1 = AugmentedAssignment(4, 6)
a1 += 1
print(a1)  # __iadd__ (5,7)
a1 -= 1
print(a1)  # __isub__  (4,6)
a1 *= 1
print(a1)  # __mul__ (4,6)
a1 /= 2
print(a1)  # __itruediv__ (2.0,12)
```

#### 可调用的对象
在Python中，一个特殊的魔术方法可以让类的实例的行为表现的像函数一样，你可以调用他们，将一个函数当做一个参数传到另外一个函数中等等。

这是一个非常强大的特性让Python编程更加舒适甜美。__call__(self, [args...])

允许一个类的实例像函数一样被调用。实质上说，这意味着x()与 x.__call__()是相同的。

注意__call__参数可变。这意味着你可以定义__call__为其他你想要的函数，无论有多少个参数。

```python

class CallableObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        if kwargs:
            self.x, self.y = kwargs['x'], kwargs['y']
        elif args:
            self.x, self.y = args[0], args[1]

    def __str__(self):
        return f'({self.x},{self.y})'


c2 = CallableObject(1, 2)
print(c2)  # (1,2)
c2(3, 4)  # __call__  修改x=3 y=4
print(c2) # (3,4)
```


####  会话管理
在Python2.5中，为了代码利用定义了一个新的关键词with语句。之前在讲文件操作的时候，用过以下代码来打开一个文件以及关闭一个文件：
'''
with open('xxx.txt','r') as fp:
    print(fp.read())
    那么这种代码底层的原理是什么呢？
    这种代码专业术语叫做会话控制器，
    他通过控制两个魔术方法：__enter__(self)以及__exit__(self,exception_type,exception_value,traceback)来定义一个代码块被执行或者终止后会话管理器应该做什么。
    他可以被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作。如果代码执行成功，没有任何异常，那么exception_type、exception_value以及traceback将会是None。
    否则的话你可以选择处理这个异常或者是直接交给用户处理。如果你想处理这个异常的话，那么必须在__exit__在所有结束之后返回True。
'''

```python

class FileOpener():
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.fp = open(*self.args,**self.kwargs)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        print(exc_type)
        # 报错
        # return True
        # 不报错
        return False

with FileOpener('test.txt','r') as fp:
    a = 1
    b = 0
    # c = a/b
    print(fp.read())
```

#### 序列化对象
有时候一个对象，想要保存在硬盘中。这时候我们就需要使用到对象持久化的技术了。

在Python中，如果要将一个对象存储到硬盘中，需要使用pickle模块，其中dump方法可以将一个对象存到硬盘中，

load方法可以从硬盘中加载一个对象。Python许多内置的数据结构是可以直接序列化的，比如：字典、列表、元组、字符串等。以下举几个例子来介绍下序列化的大体步骤

```python
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

```

自己定义可持续化的对象：

自己定义的类的对象，默认情况下是不能持续化的。

如果想要让自定义的对象可持续化，那么应该实现两个魔术方法：第一个是__getstate__，

这个魔术方法在把对象存储到硬盘中的时候会调用的，会将这个方法的返回值存储进去，返回值应该是可以持续化的数据类型，比如字典、列表、字符串等；

第二个是__setstate__，这个魔术方法是从硬盘中加载对象的时候，会调用，会将你之前存储进去的值，通过参数的形式传递进来。以下举个例子来说明下：
```python
import pickle
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
```