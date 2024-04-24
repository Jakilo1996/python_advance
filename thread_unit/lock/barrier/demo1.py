# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     function_demo.py
# Author:      Jakiro
# Datetime:    2022/2/22 15:45
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import threading

def open1():
    print('人数够了，开门！\n',end='')


barrier = threading.Barrier(parties=3, action=open1)
# barrier = threading.Barrier(3, open1)


class Customer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = 3

    def run(self):
        while self.n > 0:
            self.n -= 1
            print(f'{self.name}在等着开门\n',end='')
            try:
                barrier.wait(2)
            except threading.BrokenBarrierError:
                pass
            print(f"{self.name}开门了\n",end='')


if __name__ == '__main__':
    t1 = Customer(name="a")
    t2 = Customer(name="b")
    t3 = Customer(name="c")
    t1.start()
    t2.start()
    t3.start()
