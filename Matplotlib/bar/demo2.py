# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     DriverWait.py
# Author:      Jakiro
# Datetime:    2021/12/20 20:57
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


from study.common.excel_handle import Excel
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

# 参数	接收值	说明	默认值
# left	array	x 轴；	无
# height	array	柱形图的高度，也就是y轴的数值；	无
# alpha	数值	柱形图的颜色透明度 ；	1
# width	数值	柱形图的宽度； 	0.8
# color（facecolor）	string	柱形图填充的颜色； 	随机色
# edgecolor	string	图形边缘颜色 	None
# label	string	解释每个图像代表的含义 	无
# linewidth（linewidths / lw)	数值	边缘or线的宽度	1


exl = Excel(r'/Users/qiujie/pythonProject/python_study/Jakiro_pro/study/xlsx/data/python_demo.xlsx')
my_font = fm.FontProperties(fname="/System/Library/Fonts/Supplemental/Songti.ttc")
all_data = exl.get_all_data_dict()
sheet1 = all_data['工作表1']
sheet_data = pd.read_excel(r'/Users/qiujie/pythonProject/python_study/Jakiro_pro/study/xlsx/data/python_demo.xlsx')
print(sheet_data['姓名'])
sheet1_data = all_data['工作表1']
# plt.bar()
col_0 = []
col_1 = []
col_2 = []
col_3 = []
for data_tuple in sheet1_data:
    col_0.append(data_tuple[0])
    col_1.append(data_tuple[1])
    col_2.append(data_tuple[2])
    col_3.append(data_tuple[3])
print(col_0, col_1, col_2, col_3)

# 读取数据

plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('12月工作量', fontsize=20, fontproperties=my_font)  # 标题，并设定字号大小
plt.xlabel(u'姓名', fontsize=14, fontproperties=my_font)  # 设置x轴，并设定字号大小
plt.ylabel(u'工作量', fontsize=14, fontproperties=my_font)  # 设置y轴，并设定字号大小

# alpha：透明度；width：柱子的宽度；facecolor：柱子填充色；edgecolor：柱子轮廓色；lw：柱子轮廓的宽度；label：图例；
plt.bar(sheet_data['姓名'], sheet_data['0.19版本实际完成工作量 11月'], alpha=0.6, width=0.8, facecolor='deeppink',
        edgecolor='darkblue', lw=1,
        label='Jay income', )
plt.xticks(fontproperties=my_font)
plt.legend(loc=2)  # 图例展示位置，数字代表第几象限
plt.show()  # 显示图像
plt.savefig(r'/Users/qiujie/pythonProject/python_study/Jakiro_pro/study/Matplotlib/picture/b.png')
