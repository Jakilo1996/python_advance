# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     session_manager.py
# Author:      Jakiro
# Datetime:    2022/4/21 18:13
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 会话管理

# 在Python2.5中，为了代码利用定义了一个新的关键词with语句。之前在讲文件操作的时候，用过以下代码来打开一个文件以及关闭一个文件：
'''
with open('xxx.txt','r') as fp:
    print(fp.read())
    那么这种代码底层的原理是什么呢？
    这种代码专业术语叫做会话控制器，
    他通过控制两个魔术方法：__enter__(self)以及__exit__(self,exception_type,exception_value,traceback)来定义一个代码块被执行或者终止后会话管理器应该做什么。
    他可以被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作。如果代码执行成功，没有任何异常，那么exception_type、exception_value以及traceback将会是None。
    否则的话你可以选择处理这个异常或者是直接交给用户处理。如果你想处理这个异常的话，那么必须在__exit__在所有结束之后返回True。
'''


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