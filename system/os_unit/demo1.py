# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo1.py
# Author:      Jakiro
# Datetime:    2022/5/26 19:07
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import os
# 2.1、os.name
# 获取当前的操作系统名称，其中Windows 是 NT 内核，所以会得到nt，而 Linux/Unix 用户则会得到posix


# 2.2、os.getcwd()
# 获取当前的工作目录


# 2.3、os.listdir()
# 获取当前工作目录的文件及文件夹
#
#
# 2.4、os. mkdir()
# 创建文件夹
#
#
# os.makedirs()创建多级目录
# 2.5、os.chdir()
# 切换目录


# 2.6、os.remove()
# 删除文件


# 2.7、os.system(command)
# 用来运行shell命令。python调用Shell脚本，有两种方法：os.system(cmd)或os.popen(cmd),前者返回值是脚本的退出状态码，后者的返回值是脚本执行过程中的输出内容。
# 2.8、os.rename()
# 将文件或路径重命名


# 2.9、os.path.split()
# 将路径和文件名分开


# 2.10、os.path.exists()
# 判断路径是否存在
#
#
# 2.11、os.path.isfile()
# 判断路径是不是文件
# import os print(os.path.isfile('E:/tmp.txt'))
os.path.isdir()
# 判断 path 是否为目录


os.path.abspath()
# 获取绝对路径


os.path.getsize()
# 获取文件的大小，单位：字节


os.path.join()
# 连接目录和文件名


os.path.basename()
# 获取路径中的文件名


os.path.dirname(path)
# 获取路径中的目录名

