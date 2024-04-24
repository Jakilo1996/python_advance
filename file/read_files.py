# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     read_files.py
# Author:      Jakiro
# Datetime:    2021/9/10 16:59
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 1.已指定的方式，打开文件
# 2.做相关的操作
# 3.关闭文件

# 写的方式打开文件
# fp = open('xxx.txt', 'w')
# # 写入文件
# fp.write('hello')
# # 关闭文件
# fp.close()

# read方法
# fp = open('xxx.txt','r')
# string_a = fp.read()
# print(string_a)
# fp.close()

# write方法

# python2 和 python3 默认打开打开文件的编码
# python2使用utf-8
# python3使用系统自带的编码
# fp = open('xxx.txt','r',encoding='utf-8')
# string_b = fp.read()
# print(string_b)
# fp.close()


# 打开文件的几种方式

# 读的方式打开文件，不能用于写入

# w写方式打开文件，不能用于读，并且会覆盖掉原来的数据

# # a追加的方式打开文件，不能用于读，不会覆盖原来的数据
# fp = open('xxx.txt','a',encoding='utf-8')
# fp.write('aaa')
# fp.close()

# r+读写的方式打开文件，r的基因,文件的指针在最开始的地方

# w+读写的方式打开文件，w的基因，文件的指针在文件结束的地方

# 文件读取的三种方式

# read函数
# fp = open('xxx.txt', 'r', encoding='utf-8')
# # 读取文件内的指定字节
# a_string = fp.read(5)
# print(a_string)
# fp.close()

# readline函数
# fp = open('xxx.txt', 'r', encoding='utf-8')
# # 读取文件中的一行  \n
# line_1 = fp.readline()
# print(line_1)
# line_2 = fp.readline()
# print(line_2)
# fp.close()

# 使用readline函数遍历文件中的所有的行
# fp = open('xxx.txt','r+',encoding='utf-8')
# while True:
#     line = fp.readline()
#     if not line:
#         break
#     print(line)
# fp.close()

# readlines函数
# fp = open('xxx.txt','r+',encoding='utf-8')
# lines = fp.readlines()
# for line in lines:
#     print(line)
# fp.close()

# 遍历文件指针对象，不会返回所有的数据
fp = open('PorthideSDP_Client.txt', 'r+', encoding='utf-8')
for line in fp:
    print(line)
fp.close()

