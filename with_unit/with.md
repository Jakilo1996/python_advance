## Python进阶——什么是上下文管理器？
在 Python 开发中，我们经常会使用到 with 语法块，例如在读写文件时，保证文件描述符的正确关闭，避免资源泄露问题。

你有没有思考过， with 背后是如何实现的？我们常常听到的上下文管理器究竟是什么？

这篇文章我们就来学习一下 Python 上下文管理器，以及 with 的运行原理。

with语法块
在讲解 with 语法之前，我们先来看一下不使用 with 的代码如何写？

我们在操作一个文件时，代码可以这么写：

# 打开文件
f = open('file.txt')
for line in f:
    # 读取文件内容 执行其他操作
    # do_something...
# 关闭文件
f.close()
这个例子非常简单，就是打开一个文件，然后读取文件中的内容，最后关闭文件释放资源。

但是，代码这么写会有一个问题：在打开文件后，如果要对读取到的内容进行其他操作，如果操作期间发生了异常，这就会导致文件句柄无法被释放，进而导致资源的泄露。

如何解决这个问题？

也很简单，我们使用 try ... finally 来优化代码：

# 打开文件
f = open('file.txt')
try:
    for line in f:
        # 读取文件内容 执行其他操作
        # do_something...
finally:
    # 保证关闭文件
    f.close()
这么写的好处是，在读取文件内容和操作期间，无论是否发生异常，都可以保证最后能释放文件资源。

但这么优化，代码结构会变得很繁琐，每次都要给代码逻辑增加 try ... finally 才可以，可读性变得很差。

针对这种情况，我们就可以使用 with 语法块来解决这个问题：

with open('file.txt') as f:
    for line in f:
        # do_something...
使用 with 语法块可以完成之前相同的功能，而且这么写的好处是，代码结构变得非常清晰，可读性也很好。

明白了 with 的作用，那么 with 究竟是如何运行的呢？

上下文管理器
首先，我们来看一下 with 的语法格式：

with context_expression [as target(s)]:
    with-body
with 语法非常简单，我们只需要 with 一个表达式，然后就可以执行自定义的业务逻辑。

但是，with 后面的表达式是可以任意写的吗？

答案是否定的。要想使用 with 语法块，with 后面的的对象需要实现「上下文管理器协议」。

什么是「上下文管理器协议」？

一个类在 Python 中，只要实现以下方法，就实现了「上下文管理器协议」：

__enter__：在进入 with 语法块之前调用，返回值会赋值给 with 的 target
__exit__：在退出 with 语法块时调用，一般用作异常处理
我们来看实现了这 2 个方法的例子：
```python

class TestContext:

    def __enter__(self):
        print('__enter__')
        return 1

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exc_type: %s' % exc_type)
        print('exc_value: %s' % exc_value)
        print('exc_tb: %s' % exc_tb)

with TestContext() as t:
    print('t: %s' % t)
    
# Output:
# __enter__
# t: 1
# exc_type: None
# exc_value: None
# exc_tb: None

```
在这个例子中，我们定义了 TestContext 类，它分别实现了 __enter__ 和 __exit__ 方法。

这样依赖，我们就可以把 TestContext 当做一个「上下文管理器」来使用，也就是通过 with TestContext() as t 方式来执行。

从输出结果我们可以看到，具体的执行流程如下：

__enter__ 在进入 with 语句块之前被调用，这个方法的返回值赋给了 with 后的 t 变量
__exit__ 在执行完 with 语句块之后被调用
如果在 with 语句块内发生了异常，那么 __exit__ 方法可以拿到关于异常的详细信息：

exc_type：异常类型
exc_value：异常对象
exc_tb：异常堆栈信息
我们来看一个发生异常的例子，观察 __exit__ 方法拿到的异常信息是怎样的：
```python


with TestContext() as t:
    # 这里会发生异常
    a = 1 / 0 
    print('t: %s' % t)

# Output:
# __enter__
# exc_type: <type 'exceptions.ZeroDivisionError'>
# exc_value: integer division or modulo by zero
# exc_tb: <traceback object at 0x10d66dd88>
# Traceback (most recent call last):
#   File "base.py", line 16, in <module>
#     a = 1 / 0
# ZeroDivisionError: integer division or modulo by zero

```
从输出结果我们可以看到，当 with 语法块内发生异常后，__exit__ 输出了这个异常的详细信息，其中包括异常类型、异常对象、异常堆栈。

如果我们需要对异常做特殊处理，就可以在这个方法中实现自定义逻辑。

回到最开始我们讲的，使用 with 读取文件的例子。之所以 with 能够自动关闭文件资源，就是因为内置的文件对象实现了「上下文管理器协议」，这个文件对象的 __enter__ 方法返回了文件句柄，并且在 __exit__ 中实现了文件资源的关闭，另外，当 with 语法块内有异常发生时，会抛出异常给调用者。

伪代码可以这么写：
```python
class File:
    def __init__(self, file_path, mode):
        self.file_obj = open(file_path, mode)

    def __enter__(self):
        print('__enter__')
        return self.file_obj

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('__exit__')
        # with 退出时释放文件资源
        self.file_obj.close()
        # 如果 with 内有异常发生 抛出异常
        if exc_type is not None:
            print(exc_type)
            raise exc_type


with File('file.txt', 'r') as fp:
    for line in fp:
        print(line)
    1 / 0
```
```python
# case2
# 将一个方法转化为 可以通过上下文调用
class WithClass():
    '''
    params : enter_func  传入 传入一个方法或类的字符串（可以是内置方法），这个类或者方法的返回值必须是一个对象
    params : exit_func 传入一个字符串，这个方法必须为 enter_func返回对象的方法，（如果字符串含有，），则将依次使用enter_func返回对象执行这些方法
    params : enter_params 以列表形式传入 enter_func 需要传入的参数
    params : exit_params 以列表形式传入 enter_func 需要传入的参数  如果 exit_func 不为1  需要以列表套列表形式传入 并且与传入exit_func 一一对应
    '''

    def __init__(self, enter_func, exit_func, enter_params=None, exit_params=None,):
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
                    if isinstance(self.exit_params[i],Iterable):
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


```
这里我们小结一下，通过对 with 的学习，我们了解到，with 非常适合用需要对于上下文处理的场景，例如操作文件、Socket，这些场景都需要在执行完业务逻辑后，释放资源。

---
contextlib模块
对于需要上下文管理的场景，除了自己实现 __enter__ 和 __exit__ 之外，还有更简单的方式来做吗？

答案是肯定的。我们可以使用 Python 标准库提供的 contextlib 模块，来简化我们的代码。

使用 contextlib 模块，我们可以把上下文管理器当成一个「装饰器」来使用。

其中，contextlib 模块提供了 contextmanager 装饰器和 closing 方法。

下面我们通过例子来看一下它们是如何使用的。

contextmanager装饰器
我们先来看 contextmanager 装饰器的使用：
```python
from contextlib import contextmanager

@contextmanager
def test():
    print('before')
    yield 'hello'
    print('after')

with test() as t:
    print(t)

# Output:
# before
# hello
# after
```
在这个例子中，我们使用 contextmanager 装饰器和 yield配合，实现了和前面上下文管理器相同的功能，它的执行流程如下：

执行 test() 方法，先打印出 before
执行 yield 'hello'，test 方法返回，hello 返回值会赋值给 with 语句块的 t 变量
执行 with 语句块内的逻辑，打印出 t 的值 hello
又回到 test 方法中，执行 yield 后面的逻辑，打印出 after
这样一来，当我们使用这个 contextmanager 装饰器后，就不用再写一个类来实现上下文管理协议，只需要用一个方法装饰对应的方法，就可以实现相同的功能。

不过有一点需要我们注意：在使用 contextmanager 装饰器时，如果被装饰的方法内发生了异常，那么我们需要在自己的方法中进行异常处理，否则将不会执行 yield 之后的逻辑。
```python


@contextmanager
def test():
    print('before')
    try:
        yield 'hello'
        # 这里发生异常 必须自己处理异常逻辑 否则不会向下执行
        a = 1 / 0 
    finally:
        print('after')

with test() as t:
    print(t)
```
closing方法
我们再来看 contextlib 提供的 closing 方法如何使用。

closing 主要用在已经实现 close 方法的资源对象上：
```python

from contextlib import closing

class Test():

    # 定义了 close 方法才可以使用 closing 装饰器
    def close(self):
        print('closed')

# with 块执行结束后 自动执行 close 方法
with closing(Test()):
    print('do something')
    
# Output:
# do something
# closed
```
从执行结果我们可以看到，with 语句块执行结束后，会自动调用 Test 实例的 close 方法。

所以，对于需要自定义关闭资源的场景，我们可以使用这个方法配合 with 来完成。

contextlib的实现
学习完了 contextlib 模块的使用，最后我们来看一下 contextlib 模块是究竟是如何实现的？

contextlib 模块相关的源码如下：

```python
class _GeneratorContextManagerBase:

    def __init__(self, func, args, kwds):
        # 接收一个生成器对象 (方法内包含 yield 的方法就是一个生成器)
        self.gen = func(*args, **kwds)
        self.func, self.args, self.kwds = func, args, kwds
        doc = getattr(func, "__doc__", None)
        if doc is None:
            doc = type(self).__doc__
        self.__doc__ = doc


class _GeneratorContextManager(_GeneratorContextManagerBase,
                               AbstractContextManager,
                               ContextDecorator):

    def __enter__(self):
        try:
            # 执行生成器 代码会运行生成器方法的 yield 处
            return next(self.gen)
        except StopIteration:
            raise RuntimeError("generator didn't yield") from None

    def __exit__(self, type, value, traceback):
        # with 内没有异常发生
        if type is None:
            try:
                # 继续执行生成器
                next(self.gen)
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")
        # with 内发生了异常
        else:
            if value is None:
                value = type()
            try:
                # 抛出异常
                self.gen.throw(type, value, traceback)
            except StopIteration as exc:
                return exc is not value
            except RuntimeError as exc:
                if exc is value:
                    return False
                if type is StopIteration and exc.__cause__ is value:
                    return False
                raise
            except:
                if sys.exc_info()[1] is value:
                    return False
                raise
            raise RuntimeError("generator didn't stop after throw()")

def contextmanager(func):
    @wraps(func)
    def helper(*args, **kwds):
        return _GeneratorContextManager(func, args, kwds)
    return helper

class closing(AbstractContextManager):
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()
```
源码中我已经添加好了注释，你可以详细看一下。

contextlib 源码中逻辑其实比较简单，其中 contextmanager 装饰器实现逻辑如下：

初始化一个 _GeneratorContextManager 类，构造方法接受了一个生成器 gen
这个类实现了上下文管理器协议 __enter__ 和 __exit__
执行 with 时会进入到 __enter__ 方法，然后执行这个生成器，执行时会运行到 with 语法块内的 yield 处
__enter__ 返回 yield 的结果
如果 with 语法块没有发生异常，with 执行结束后，会进入到 __exit__ 方法，再次执行生成器，这时会运行 yield 之后的代码逻辑
如果 with 语法块发生了异常，__exit__ 会把这个异常通过生成器，传入到 with 语法块内，也就是把异常抛给调用者
再来看 closing 的实现，closing 方法就是在 __exit__ 方法中调用了自定义对象的 close，这样当 with 结束后就会执行我们定义的 close 方法。

使用场景
学习完了上下文管理器，那么它们具体会用在什么场景呢？

下面我举几个常用的例子来演示下，你可以参考一下结合自己的场景使用。

---
Redis分布式锁
```python

from contextlib import contextmanager

@contextmanager
def lock(redis, lock_key, expire):
    try:
        locked = redis.set(lock_key, 'locked', expire)
        yield locked
    finally:
        redis.delete(lock_key)

# 业务调用 with 代码块执行结束后 自动释放锁资源
with lock(redis, 'locked', 3) as locked:
    if not locked:
        return
    # do something ...

```
在这个例子中，我们实现了 lock 方法，用于在 Redis 上申请一个分布式锁，然后使用 contextmanager 装饰器装饰了这个方法。

之后我们业务在调用 lock 方法时，就可以使用 with 语法块了。

with 语法块的第一步，首先判断是否申请到了分布式锁，如果申请失败，则业务逻辑直接返回。如果申请成功，则执行具体的业务逻辑，当业务逻辑执行完成后，with 退出时会自动释放分布式锁，就不需要我们每次都手动释放锁了。

Redis事物和管道
```python

from contextlib import contextmanager

@contextmanager
def pipeline(redis):
    pipe = redis.pipeline()
    try:
        yield pipe
        pipe.execute()
    except Exception as exc:
        pipe.reset()
            
# 业务调用 with 代码块执行结束后 自动执行 execute 方法
with pipeline(redis) as pipe:
    pipe.set('key1', 'a', 30)
    pipe.zadd('key2', 'a', 1)
    pipe.sadd('key3', 'a')

```
在这个例子中，我们定义了 pipeline 方法，并使用装饰器 contextmanager 让它变成了一个上下文管理器。

之后在调用 with pipeline(redis) as pipe 时，就可以开启一个事物和管道，然后在 with 语法块内向这个管道中添加命令，最后 with 退出时会自动执行 pipeline 的 execute 方法，把这些命令批量发送给 Redis 服务端。

如果在执行命令时发生了异常，则会自动调用 pipeline 的 reset 方法，放弃这个事物的执行。

---

总结
总结一下，这篇文章我们主要介绍了 Python 上下文管理器的使用及实现。

首先我们介绍了不使用 with 和使用 with 操作文件的代码差异，然后了解到使用 with 可以让我们的代码结构更加简洁。之后我们探究了 with 的实现原理，只要实现 __enter__ 和 __exit__ 方法的实例，就可以配合 with 语法块来使用。

之后我们介绍了 Python 标准库的 contextlib 模块，它提供了实现上下文管理更好的使用方式，我们可以使用 contextmanager 装饰器和 closing 方法来操作我们的资源。

最后我举了两个例子，来演示上下文管理器的具体使用场景，例如在 Redis 中使用分布式锁和事物管道，用上下文管理器帮我们管理资源，执行前置和后置逻辑。

所以，如果我们在开发中把操作资源的前置和后置逻辑，通过上下文管理器来实现，那么我们的代码结构和可维护性也会有所提高，推荐使用起来。