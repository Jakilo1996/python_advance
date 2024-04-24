# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     contextlib_desc.py
# Author:      Jakiro
# Datetime:    2022/5/9 15:17
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# contextlib模块
# 对于需要上下文管理的场景，除了自己实现 __enter__ 和 __exit__ 之外，还有更简单的方式来做吗？
#
# 答案是肯定的。我们可以使用 Python 标准库提供的 contextlib 模块，来简化我们的代码。
#
# 使用 contextlib 模块，我们可以把上下文管理器当成一个「装饰器」来使用。
#
# 其中，contextlib 模块提供了 contextmanager 装饰器和 closing 方法。

# contextmanager装饰器


from contextlib import contextmanager


@contextmanager
def hello_test():
    print('before')
    yield 'hello'
    print('after')


# with hello_test() as t:
#     print(t)


# Output:
# before
# hello
# after

# 理器相同的功能，它的执行流程如下：
#
# 执行 test() 方法，先打印出 before
# 执行 yield 'hello'，test 方法返回，hello 返回值会赋值给 with 语句块的 t 变量
# 执行 with 语句块内的逻辑，打印出 t 的值 hello
# 又回到 test 方法中，执行 yield 后面的逻辑，打印出 after
# 这样一来，当我们使用这个 contextmanager 装饰器后，就不用再写一个类来实现上下文管理协议，只需要用一个方法装饰对应的方法，就可以实现相同的功能

# 不过有一点需要我们注意：在使用 contextmanager 装饰器时，如果被装饰的方法内发生了异常，那么我们需要在自己的方法中进行异常处理，否则将不会执行 yield 之后的逻辑。

@contextmanager
def b_test():
    print('before')
    try:
        yield 'hello'
        # 这里发生异常 必须自己处理异常逻辑 否则不会向下执行
        a = 1 / 0
        print('error')
    finally:
        print('after')


# with b_test() as t:
#     print(t)

# closing方法
# 我们再来看 contextlib 提供的 closing 方法如何使用。
#
# closing 主要用在已经实现 close 方法的资源对象上：

from contextlib import closing


class Test():

    # 定义了close 方法才可以使用 closing 装饰器
    def close(self):
        # 此处也是相同 必须得处理异常
        try:
            1 / 0
        finally:
            print('closed')


# with closing(Test()):
#     print('do something')

# Output:
# do something
# closed

# 从执行结果我们可以看到，with 语句块执行结束后，会自动调用 Test 实例的 close 方法。
#
# 所以，对于需要自定义关闭资源的场景，我们可以使用这个方法配合 with 来完成。


@contextmanager
def open2(file_path, mode):
    fp = open(file_path, mode=mode)

    yield fp
    fp.close()
    print(fp.read())


with open2(file_path='file.txt', mode='r') as fp:
    print(fp.read())

from contextlib import contextmanager

