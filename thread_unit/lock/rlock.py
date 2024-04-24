# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     rlock.py
# Author:      Jakiro
# Datetime:    2022/2/18 15:30
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# 重入锁  （Python RLock对象）
# 　　为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。
#
# threading.Rlock() 允许多次锁资源，acquire() 和 release() 必须成对出现，也就是说加了几把锁就得释放几把锁。
#
# 方法：
#
# acquire(blocking=True,timeout = -1)：内部counter变量加1
#
# release():内部counter变量减1

import threading

# 原始锁lock会死锁
# lock = threading.Lock()
# # 死锁
# lock.acquire()
# lock.acquire()
# print('...')
# lock.release()
# lock.release()


# 重入锁不会死锁
rlock = threading.RLock()
# 同一线程内不会阻塞线程，可以多次acquire
rlock.acquire()
rlock.acquire()
print('...')
rlock.release()
rlock.release()
