# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     DriverWait.py
# Author:      Jakiro
# Datetime:    2022/2/28 14:35
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import threading
import time


def open1():
    print('人数够了，开门！\n', end='')


barrier = threading.Barrier(parties=3, action=open1)


# barrier = threading.Barrier(3, open1)


class Customer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = 3

    def run(self):
        while self.n > 0:
            self.n -= 1
            print(f'{self.name}在等着开门\n', end='')
            try:
                # 设置超时时间，如果2秒内，没有达到障碍线程数量，
                # 会进入断开状态，引发BrokenBarrierError错误
                barrier.wait(2)
                # print(barrier.n_waiting)
            except threading.BrokenBarrierError:
                continue
            else:
                print(f"{self.name}开门了\n", end='')


class Manager(threading.Thread):
    def run(self):
        print('前面几个不算，重来\n', end='')
        barrier.reset()


if __name__ == '__main__':
    t1 = Customer(name="a")
    t2 = Customer(name="b")
    t3 = Customer(name="c")
    tm = Manager()
    # print(barrier.parties)
    t1.start()
    t2.start()
    tm.start()
    t3.start()
