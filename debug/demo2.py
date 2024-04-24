# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     fork_d.py
# Author:      Jakiro
# Datetime:    2022/5/7 14:29
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# a = eval('open("file1.txt",mode="w")')
# a.write('a')
# a.close()
# eval(f'{a}.close()')

# login_su = [tuple(login_succeed)]

# a = 'aaads'
# b = a.upper()
# print(a, b)
#
print(type(open))


# a = [1, 2]


def func_2():
    print('func_2')


print(type(func_2))
func_2()
# eval('func2()')
eval('func_2()')


class Person():
    def __init__(self, a, b):
        self.c = a


# 如果直接传 内置库函数或方法  或 自定义方法 通过eval 执行
# 如果传
p2 = eval('Person(1,2)')
print(p2.c)


