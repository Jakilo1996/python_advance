# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     zip_demo.py
# Author:      Jakiro
# Datetime:    2022/1/13 20:56
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # 打包为元组的列表
for g, i in zipped:
    print(g, i)
# d = zip(a, c)  # 元素个数与最短的列表一致
# for k, l in d:
#     print(k, l)
# e = zip(*zipped)  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# # print(e[0], e[1])
f = 1.1**6
print(f)