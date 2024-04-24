# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     lock.py
# Author:      Jakiro
# Datetime:    2022/2/18 15:15
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 原始锁 （Python Lock对象）
# 方法：
#
# acquire(blocking=True,timeout=-1)：默认阻塞，阻塞可以设置超时时间。非阻塞时，timeout禁止设置。成功获取锁，返回True，否则返回False
#
# release( )：释放锁。可以从任何线程释放。已上锁的锁，会抛出RuntimeError异常。
#
# 总结：原始锁是一个处于两个状态的变量：解锁和加锁，只需要一个二进制位表示，原始锁和前面信号量和event都是可以被线程之间共享的，这里原始锁对象始终只让一个线程进入临界区，如果该锁在进入临界区之前加锁，则其他线程在进入此临界区时都会被阻塞，等待临界区的线程完成解锁操作。其他线程才有机会进入此临界区（随机选择一个线程允许它获得锁）。
#
# 原始锁适用于访问和修改同一个资源的时候，引起资源争用的情况下。使用锁的注意事项：锁的使用场景：
#
# 1.少用锁，除非有必要。多线程访问加锁的资源时，由于锁的存在，实际就变成了串行。
#
# 2.加锁时间越短越好，不需要就立即释放锁。
#
# 3.一定要避免死锁，使用with或者try...finally。
#
# 我们修改了最开始的例子，使用原始锁保证了线程安全：

import threading

num = 0
lock = threading.Lock()


def add_number():
    global num
    try:
        lock.acquire()
        for i in range(1000):
            num += 1
    finally:
        lock.release()


if __name__ == '__main__':
    threads = []
    for i in range(0, 10):
        current_thread = threading.Thread(target=add_number)
        current_thread.start()
        threads.append(current_thread)
    for thread in threads:
        thread.join()
    print(num)
