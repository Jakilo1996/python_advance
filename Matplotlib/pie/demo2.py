# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     DriverWait.py
# Author:      Jakiro
# Datetime:    2021/12/20 17:04
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

my_font = fm.FontProperties(fname="/System/Library/Fonts/Supplemental/Songti.ttc")
y = np.array([22, 23, 32, 23, 44])
plt.axes(aspect='equal')
plt.pie(y, labels=['a', 'b', 'c', 'd', 'e'],  # 设置饼图标签
        colors=['red', 'blue', 'green', 'pink', 'yellow'],  # 设置颜色
        explode=(0, 0, 0, 0, 0),  # 突出显示
        autopct='%.2f%%',
        )

plt.title('测试demo', fontproperties=my_font, color='black', fontsize='18')

plt.savefig('demo2.png')
plt.show()
