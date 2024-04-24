# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     datarace.py
# Author:      Jakiro
# Datetime:    2022/3/10 13:23
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# * 使用 Golang 开发一个 HTTP Web 服务器/客户端
# 	* 服务端维护一个内存数据结构，所有数据进程重启丢失，不做数据持久化，不考虑内存容量问题
# 	* 服务端实现一个网络 API 接口，客户端向该 API 发送一个网络请求，请求数据是一个 string 的信息
# 	* 服务端该 API 收到请求后响应一个 []string 的信息，返回之前发送过的所有string，当次请求发送的string一定在最后，不关心是否重复
# 	  	* 示例：
# 	  		* 第一次请求发送："a"，响应: []string{"a"}
# 	  		* 第二次请求发送："b"，响应: []string{"a", "b"}
# 	  		* 第三次请求发送："a"，响应: []string{"a", "b", "a"}
# 		* 注意服务端代码部分，任何情况下均不能退出进程。
# 	* 必须写一个 Golang 的客户端函数（该函数后面简称 BcjClient ），调用该服务端的 API 接口
# 		* 该客户端函数输入参数为：string，输出参数为： []string，和 error
# 		* 客户端函数是个function/函数，不是method/方法
# 		* 注意客户端函数业务代码执行过程中，任何情况下均不能退出进程。
# 		* 客户端函数的类型必须严格匹配。

import threading

current_data_list = []

write_event = threading.Event()
read_event = threading.Event()


class WriteTh(threading.Thread):
    def __init__(self, wt, rt, current_data):
        global current_data_list
        self.current_data = current_data
        self.wt = wt
        self.rt = rt

    def run(self):
        current_data_list.append(self.current_data)
        self.rt.set()
        self.wt.wait()
        self.wt.clear()


class ReadTh(threading.Thread):
    def __init__(self, wt, rt, current_data):
        self.current_data = current_data
        self.wt = wt
        self.rt = rt

    def run(self):
        self.rt.wait()
        print(current_data_list)
        self.wt.set()
        self.wt.clear()



