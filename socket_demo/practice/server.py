# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     server.py
# Author:      Jakiro
# Datetime:    2022/3/10 13:48
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词`
# -----------------------------------------------------------------------------------


# ss = socket_demo() # 创建服务器套接字
# ss.bind() # 套接字与地址绑定
# ss.listen() # 监听连接
# inf_loop: # 服务器无限循环
# cs = ss.accept() # 接受客户端连接
# comm_loop: # 通信循环
# cs.recv()/cs.send() # 对话（接收/发送）
# cs.close() # 关闭客户端套接字
# ss.close() # 关闭服务器套接字#（可选）

import socket_demo
import threading

# 1.socket_demo(socket_family, socket_type, protocol=0)
# 其中，socket_family 是 AF_UNIX 或 AF_INET,ocket_type 是 SOCK_STREAM或 SOCK_DGRAM, protocol 通常省略，默认为 0。
# 为了创建 TCP/IP 套接字，可以用下面的方式调用 socket_demo.socket_demo()。
# tcpSock = socket_demo.socket_demo(socket_demo.AF_INET, socket_demo.SOCK_STREAM)
# 同样，为了创建 UDP/IP 套接字，需要执行以下语句。
# udpSock = socket_demo.socket_demo(socket_demo.AF_INET, socket_demo.SOCK_DGRAM)
ServerSocket = socket_demo.socket(socket_demo.AF_INET, socket_demo.SOCK_STREAM)

# 获取本地机器名
host = socket_demo.gethostname()

# 设置端口
port = 9999

# 2.s.bind绑定本地地址到socket对象
ServerSocket.bind((host, port))
# 3.s.listen监听地址端口，连接几个客户端
ServerSocket.listen(2)

current_data_list = []
write_event = threading.Event()
read_event = threading.Event()


class WriteTh(threading.Thread):
    def __init__(self, wt, rt, current_data):
        super().__init__()
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
        super().__init__()
        self.current_data = current_data
        self.wt = wt
        self.rt = rt
        self.current_data_list = current_data_list

    def run(self):
        self.rt.wait()
        self.current_data_list = current_data_list
        self.wt.set()
        self.wt.clear()


while True:
    # 4.s.accept阻塞接受链接请求，被动接受 TCP 客户端连接，一直等待直到连接到达（阻塞）
    # accept()方法会返回一个含有两个元素的元组（fd,addr）。
    # 第一个元素是新的socket对象，服务器通过它与客户端通信。
    # 第二个元素也是元组，是客户端的地址及端口信息。
    clientsocket, addr = ServerSocket.accept()
    print("连接地址:%s" % str(addr))
    msg = "welcomt to my demo"
    # send()和recv()的数据格式都是bytes。
    # (str和bytes的相互转化，用encode()和decode(),或者用bytes()和str())
    # s.recv()	接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
    # s.send()	发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
    clientsocket.send(msg.encode("utf-8"))
    data = clientsocket.recv(1024)
    print(data.decode())
    wt = WriteTh(wt=write_event, rt=read_event,current_data=data.decode())
    rt = ReadTh(wt=write_event, rt=read_event,current_data=data.decode())
    wt.start()
    rt.start()
    data1 = str(rt.current_data_list)
    print(data1)
    clientsocket.send(data1.encode('utf-8'))
    clientsocket.close()
ServerSocket.close()
