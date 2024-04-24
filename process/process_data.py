# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     process_data.py
# Author:      Jakiro
# Datetime:    2022/4/24 11:45
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 进程间数据不共享：

# 在一个程序中，如果创建了一个子进程，那么这个子进程会拷贝一份当前进程所有的资源作为子进程的运行环境。
# 也就是说，子进程中的变量可能跟父进程一样，但其实是另外一个块内存区域了。
# 他们之间的数据是不共享的。以下代码演示一下：


from multiprocessing import Process
import os

AGE = 1


def child_func(names):
    global AGE
    AGE += 1
    names.append('ketang')
    print('=' * 8, '子进程', '=' * 8)
    print(f'AGE:{AGE}，id:{id(AGE)}')
    print(f'names:{names}')
    print(f'pid:{os.getpid()}')
    print('=' * 8, '子进程', '=' * 8)


if __name__ == '__main__':
    names = ['qiujie', ]
    p = Process(target=child_func,args=(names,))
    p.start()
    p.join()
    print('=' * 8, '父进程', '=' * 8)
    print(f'AGE:{AGE}，id:{id(AGE)}')
    print(f'names:{names}')
    print(f'pid:{os.getpid()}')
    print('=' * 8, '父进程', '=' * 8)
    # output
    # ======== 子进程 ========
    # AGE:2，id:4381551424
    # names:['qiujie', 'ketang']
    # pid:69484
    # ======== 子进程 ========
    # ======== 父进程 ========
    # AGE:1，id:4381551392  与子进程不同
    # names:['qiujie']      与子进程不同
    # pid:69483             与子进程不同
    # ======== 父进程 ========
