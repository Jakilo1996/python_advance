# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     condition_producer.py
# Author:      Jakiro
# Datetime:    2022/4/28 15:12
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# Condition版的生产者与消费者模式：
# Lock版本的生产者与消费者模式可以正常的运行。但是存在一个不足，在消费者中，总是通过while True死循环并且上锁的方式去判断钱够不够。
# 上锁是一个很耗费CPU资源的行为。因此这种方式不是最好的。还有一种更好的方式便是使用threading.Condition来实现。
# threading.Condition可以在没有数据的时候处于阻塞等待状态。一旦有合适的数据了，还可以使用notify相关的函数来通知其他处于等待状态的线程。
# 这样就可以不用做一些无用的上锁和解锁的操作。可以提高程序的性能。首先对threading.Condition相关的函数做个介绍，threading.Condition类似threading.Lock，
# 可以在修改全局数据的时候进行上锁，也可以在修改完毕后进行解锁。以下将一些常用的函数做个简单的介绍：

# acquire：上锁。
# release：解锁。
# wait：将当前线程处于等待状态，并且会释放锁。可以被其他线程使用notify和notify_all函数唤醒。被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
# notify：通知某个正在等待的线程，默认是第1个等待的线程。
# notify_all：通知所有正在等待的线程。notify和notify_all不会释放锁。并且需要在release之前调用

# case
import threading
import random
import time

gMoney = 1000
gCondition = threading.Condition()
gTimes = 0
gTotalTimes = 5


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                print('当前生产者总共生产了%s次' % gTimes)
                break
            gMoney += money
            print('%s当前存入%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            time.sleep(1)
            gCondition.notify_all()
            gCondition.release()


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        while True:
            money = random.randint(100, 500)
            gCondition.acquire(
            )
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    print('消费完成')
                    return
                print('%s准备取%s元钱，剩余%s元钱，不足！' % (threading.current_thread(), money, gMoney))
                gCondition.wait()
            gMoney -= money
            print('%s当前取出%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
            time.sleep(1)
            gCondition.release()


def main():
    for x in range(5):
        Consumer(name='消费者线程%d' % x).start()
    for x in range(5):
        Producer(name='生产者线程%d' % x).start()


if __name__ == '__main__':
    main()
