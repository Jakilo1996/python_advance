# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     condition.py
# Author:      Jakiro
# Datetime:    2022/2/22 15:01
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 作用: 在保护互斥资源的基础上，增加了条件判断的机制
# 即为使用wait() 函数 判断不满足当前条件的基础上，让当前线程的阻塞。
# 其他线程如果生成了满足了条件的资源 使用notify（） notifyALl（） 函数将刮起线程唤醒。
# 使用了 threading 的Condition 类
# acquire() : 锁住当前资源
# relarse() ：释放当前锁住的资源
# wait：挂起当前线程， 等待唤起 。
# • notify：唤起被 wait 函数挂起的线程 。
# • notif计All：唤起所有线程，防止线程永远处于沉默状态


from threading import Thread
from threading import Condition
import random
import time

flag = 0  # 控制标志
goods = 0  # 事务表示
lock = Condition()


def consumer(x):
    global flag
    global goods
    lock.acquire()  # 获得锁
    while flag == 0:
        print(f'consumer{x} 进入等待')
        lock.wait()
    print(f'consumer{x} 消费了{goods}')
    flag -= 1
    lock.release()


def product(x):
    global flag
    global goods
    time.sleep(3)
    lock.acquire()
    goods = random.randint(1, 100)
    print(f'product{x} 产生了{goods}')
    flag += 1
    lock.notifyAll()
    lock.release()


threads = []
for i in range(0, 2):
    tc = Thread(target=consumer, args=(i,))
    tp = Thread(target=product, args=(i,))
    tc.start()
    tp.start()
    threads.append(tc)
    threads.append(tp)

for x in threads:
    x.join()
