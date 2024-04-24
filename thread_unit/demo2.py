# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo2.py
# Author:      Jakiro
# Datetime:    2022/9/22 10:26
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import threading

# current_data_list = []

# write_event = threading.Event()
# read_event = threading.Event()

n = 0


class AddThread(threading.Thread):
    def run(self):
        global n
        for i in range(0,100000):
            n += i



if __name__ == '__main__':
    ths = []
    for i in range(0,400):
        add_t = AddThread()
        ths.append(add_t)

    for i in ths:
        i.start()

    for i in ths:
        i.join()
    print(n)
