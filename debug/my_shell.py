# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   acnsdp_autotest
# FileName:     my_shell.py
# Author:      czx
# Datetime:    2021/6/15 11:09 上午
# Description:ssh相关
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# --------------------------------------
import subprocess
import time

import paramiko
import pymysql


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o

class ConLinux:
    def __init__(self, hostname, username, password=''):
        self.shell = paramiko.SSHClient()
        # 取消安全认证
        self.shell.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接linux
        self.shell.connect(hostname=hostname, username=username, password=password)

        self.channel = self.shell.invoke_shell()

    def con_linux(self, command):
        # 执行命令
        stdin, stdout, stderr = self.shell.exec_command(command)
        # 读取执行结果
        result = stdout.read()
        # 返回执行结果
        return result

    def invoke(self, command):
        self.channel.send(command + '\n')
        buff = ""
        while not buff.strip(" ").endswith('2004h'):
            time.sleep(1)
            resp = self.channel.recv(9999).decode("ISO-8859-1")
            buff += resp
            print(resp)

    def __del__(self):
        self.shell.close()

class MySql():
    def __init__(self, hostname, user, database):
        self.db = pymysql.connect(host=hostname, user=user, db=database, password="123456")
        self.cursor = self.db.cursor()

    def drop_databse(self, database):
        self.cursor.execute(f"drop database {database};")

    def execute(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res