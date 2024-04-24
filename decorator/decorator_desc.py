# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     decorator_desc.py
# Author:      Jakiro
# Datetime:    2022/4/28 20:44
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 装饰器
# 什么是装饰器：
# 装饰器利用了函数也可以作为参数传递和闭包的特性，可以让我们的函数在执行之前或者执行之后方便的添加一些代码。
# 这样就可以做很多事情了，比如@classmethod装饰器可以将一个普通的方法设置为类方法，@staticmethod装饰器可以将一个普通的方法设置为静态方法等。
# 所以明白了装饰器的原理以后，我们就可以自定义装饰器，从而实现我们自己的需求。

# 理解：
# 拿网站开发的例子来说。网站开发中，经常会碰到一些页面是需要登录后才能访问的。
# 那么如果每次都在访问的视图函数中判断，很麻烦，而且代码很难维护，示例如下：
#
user = {
    "is_login": False
}
# user = {
#     "is_login": True
# }


#
# def edit_user():
#     if user['is_login'] == True:
#         print('用户名修改成功')
#     else:
#         print('跳转到登录页面')
#
# def add_article():
#     if user['is_login'] == True:
#         print('添加文章成功')
#     else:
#         print('跳转到登录页面')

# edit_user()
# add_article()

# 以上现在是只有两个函数，如果以后网站越来越大，需要做判断的地方越来越大，
# 那么这种判断将显得非常低效并且难以维护，因此这时候我们可以采用装饰器来解决：


#
#
def edit_user():
    print('用户名修改成功')

#
def add_article():
    print('添加文章成功')
#
#
def login_required(func):
    def inner():
        if user['is_login'] == True:
            func()
        else:
            print('跳转到登录页面')
    return inner
#
#  inner()
login_required(edit_user)  #  login_required(edit_user) = inner
login_required(add_article)()

@login_required # login_required(edit)
def eidt():
    pass
eidt()  # inner()
#
# 这样我们把这个判断用户是否登录的逻辑就已经单独抽出放到login_required这个装饰器中了，以后如果某个函数想要做登录限制，那么就先传给login_required这个装饰器就可以了。
# 但是以上方式写法很别扭，每次调用一个函数的时候要记得先传给login_required，容易忘记每次都要写，因此我们采用另外一种写法：

# def login_required(func):
#     def inner():
#         if user['is_login'] == True:
#             func()
#         else:
#             print('跳转到登录页面')
#
#     return inner
#
# @login_required   #  inner func = edit_user
# def edit_user():
#     print('用户名修改成功')
#
# @login_required   # = inner
# def add_article():
#     print('添加文章成功')
#
# def edit_user1():
#     print('用户名修改成功')
#
#
# def add_article1():
#     print('添加文章成功')
#
# # 以上这种写法是装饰器中正确的写法，在函数定义开头的地方，通过@装饰器名就可以了，
# # 这样在调用edit_user和add_article的时候，就不需要手动的传给login_required了。
#
# login_required(edit_user1)()
# login_required(add_article1)()
# edit_user()  # inner()  func =edit
# add_article() # inner()  func =edit

# 被装饰的函数带有参数：
# 被装饰的函数有参数是非常普遍的一种情况，这时候我们只需要在里面的函数中传递参数就可以了：
# def login_required(func):
#
#     def wrapper(*args,**kwargs):
#         if user['is_login'] == True:
#             func(*args,**kwargs)
#         else:
#             print('跳转到登录页面')
#
#     return wrapper
#
# @login_required  # wrapper
# def edit_user(username):
#     print('用户名修改成功：%s'%username)
#
# edit_user(3)

# 带参数的装饰器：
# 装饰器也可以传递参数。只不过如果给装饰器传递参数了，那么就要在这个装饰器中写两个方法了，示例代码如下：
# def login_required(a=2):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             # print(args)
#             if user['is_login'] == True:
#                 func(*args, **kwargs)
#             else:
#                 print(f'跳转到登录页面{a}')
#
#         return wrapper
#
#     return inner
# #
# #
# @login_required(a=4) # inner  func edit   wrapper()  func edit
# def edit_user(a):
#     print(f'用户名修改成功{a}')
# #
# edit_user(3) # wrapper(3)


# wraps装饰器：
# 采用之前的装饰器，会让我们的函数失去一些属性，比如__name__，这样在一些代码中会产生错误，比如Flask开发中。
# 如果我们想要用装饰器，并且仍想保留函数的一些属性，比如__name__，那么可以使用wraps装饰器，以下是没有使用wraps装饰器的代码：
#
from functools import wraps
def login_required(a=2):

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # print(args)
            if user['is_login'] == True:
                func(*args, **kwargs)
            else:
                print(f'跳转到登录页面{a}')

        return wrapper

    return inner


@login_required(a=4) # inner  # wrapper
def edit_user(a):
    print(f'用户名修改成功{a}')

edit_user(3)
print(edit_user.__name__)