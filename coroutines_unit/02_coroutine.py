# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     02_coroutine.py
# Author:      Jakiro
# Datetime:    2023/3/1 14:43
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import time
import asyncio


async def fun():
    time.sleep(3)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


coroutine_1 = fun()  # 协程是一个对象，不能直接运行
loop = asyncio.get_event_loop()  # 创建一个事件循环
result = loop.run_until_complete(coroutine_1)  # 将协程对象加入到事件循环中，并执行
