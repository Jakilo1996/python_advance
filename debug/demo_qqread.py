# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo_qqread.py
# Author:      Jakiro
# Datetime:    2022/12/7 11:35
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import os.path

import requests
import re

a = 'LONG21'

a_path = f'data/{a}.txt'
if not os.path.exists(a_path):
    host = f'https://book.qq.com/book-read/44964278/19'

    resp_a = requests.get(host)
    print(resp_a.text)
    print(len(resp_a.text))
    pattern = re.compile('id="content"(.*?)</div>')
    b = re.findall(pattern, resp_a.text)[0]
    list2 = b.split('\r<br />\r<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
    # print(list2)

    with open(a_path, mode='w') as fp:
        for i in list2:
            fp.write(i + '\n')
else:
    with open(a_path, mode='r') as fp:

        c = iter(fp.readlines())
        # i = 0

        while 1:
            a = input('ss:')
            print('*' * 20, next(c), '&nbsp' * 30, '\n', '&nbsp;' * 20, end='')
