# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     05_await2.py
# Author:      Jakiro
# Datetime:    2023/3/1 15:20
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import time
import asyncio


async def add_clothes():
    print('往洗衣机添加衣服....')
    await asyncio.sleep(2)       # 模拟这个任务耗时2秒


async def washing1():
    print('洗衣机工作之前，需加衣服进去')
    await add_clothes()  # 等待这个事情完成
    print('衣服加进去，可以开始工作了。。。。')
    await asyncio.sleep(3)  # 模拟洗衣机工作的耗时
    print('washer1 finished')  # 洗完了

print('start washing:')
start_time = time.time()
coroutine_1 = washing1() # 协程是一个对象，不能直接运行
loop = asyncio.get_event_loop()  # 创建一个事件循环
result = loop.run_until_complete(coroutine_1)  # 将协程对象加入到事件循环中，并执行
end_time = time.time()
print('-----------end washing----------')
print('总共耗时:{}'.format(end_time-start_time))