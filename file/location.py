# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     location.py
# Author:      Jakiro
# Datetime:    2021/9/10 18:20
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------



# 文件的定位读写操作

# tell函数:获取当前文件指针所在的区域
# fp = open('xxx.txt','r+',encoding='utf-8')
# text = fp.read(5)
# position = fp.tell()
# print(position)
# fp.close()

# seek方法 定位到某个位置，
# offset偏移量，
# from 参照物 0代表开头  1代表结尾 2 代表文件结尾

# 文件指针往后面移动5个字节
fp = open('PorthideSDP_Client.txt', 'r+', encoding='utf-8', errors='ignore')
text = fp.read()
print(text)
fp.close()