# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     04_await.py
# Author:      Jakiro
# Datetime:    2023/3/1 14:58
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import time
import asyncio


async def washing1():
    await asyncio.sleep(3)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


async def washing2():
    await asyncio.sleep(8)
    print('washer2 finished')


async def washing3():
    await asyncio.sleep(5)
    print('washer3 finished')

if __name__ == '__main__':
    print('start main:')
    start_time = time.time()
    # step1 创建一个事件循环
    loop = asyncio.get_event_loop()
    # step2 将异步函数（协程）加入事件队列
    tasks = [
        washing1(),
        washing2(),
        washing3()
    ]
    # step3 执行事件队列 直到最晚的一个事件被处理完毕后结束
    loop.run_until_complete(asyncio.wait(tasks))
    end_time = time.time()
    print('-----------end main----------')
    print('总共耗时:{}'.format(end_time-start_time))