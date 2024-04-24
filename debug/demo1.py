# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     argparse_desc.py
# Author:      Jakiro
# Datetime:    2022/4/21 13:18
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


# import  requests
#
# see = requests.session()
# proxies = {
#     "http": "http://127.0.0.1:8888",
#     'https': "https://127.0.0.1:8888"
#     # "https": "http://12.34.56.79:9527",
# }
# see.get('https://www.baidu.com',proxies=proxies,cert='/Users/qiujie/study/my_code/python_adv'
#                                                      'ance_code/debug/Charles Proxy CA (24 Mar 2022, ZZ-B154deMacBook-Pro.local).cer')

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        monthdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        date2_days = 0;
        date1_days = 0
        date1_yaer = int(date1[0:4])
        date1_month = int(date1[5:7])
        date1_day = int(date1[8:])
        date2_yaer = int(date2[0:4])
        date2_month = int(date2[5:7])
        date2_day = int(date2[8:])
        # 处理月份
        for i in range(date2_month):
            date2_days += monthdays[i]
        # 处理月
        date2_days += date2_day
        # 当前闰年补差
        if (date2_yaer % 4 == 0 and i % 100 != 0) or (date2_yaer % 400 == 0):
            if date2_month > 2:
                date2_days += 1
        # 处理年
        if date2_yaer >= 1972:
            date2_days += 364
            for i in range(1972, date2_days):
                date2_days += 365
                if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                    date2_days += 1

        # 处理月份
        for i in range(date1_month):
            date1_days += monthdays[i]
        # 处理月
        date1_days += date1_day
        # 当前闰年补差
        if (date1_yaer % 4 == 0 and i % 100 != 0) or (date1_yaer % 400 == 0):
            if date1_month > 2:
                date1_days += 1
        # 处理年
        if date1_yaer >= 1972:
            date1_days += 364
            for i in range(1972, date1_days):
                date1_days += 365
                if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                    date1_days += 1
        return (date1_days - date2_days) if date1_days > date2_days else date2_days - date1_days



Solution.daysBetweenDates("2020-01-15","2019-12-31")