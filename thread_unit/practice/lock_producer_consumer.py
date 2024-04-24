# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     lock_producer_consumer.py
# Author:      Jakiro
# Datetime:    2022/4/25 17:38
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
# 记录生产者生产的次数，达到10次就不再生产
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gLock
        global gTimes
        global gMoney
        while 1:
            gLock.acquire()
            if gTimes <= 10:
                money = random.randint(100, 1000)

                gMoney += money
                print(f'{threading.current_thread()}_produce_money:{money},current_money:{gMoney}')
                time.sleep(1)
                gTimes += 1
                gLock.release()
            else:
                gLock.release()
                print('10次生产完成')
                break


class Consumer(threading.Thread):
    def run(self):
        global gLock
        global gTimes
        global gMoney
        while 1:
            money = random.randint(100,1000)
            gLock.acquire()
            if money <= gMoney:

                gMoney -= money
                print(f'{threading.current_thread()}_consumer_money:{money},current_money:{gMoney}')
                time.sleep(1)
            else:
                if gTimes >= 10:
                    gLock.release()
                    print(f'全部消费,剩余{gMoney},想花费{money}')
                    break
            gLock.release()

def main():
    for x in range(5):
        Consumer(name='消费者线程').start()

    for x in range(5):
        Producer(name='生产者线程').start()


if __name__ == '__main__':
    main()