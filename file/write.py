# FileName:     read_files.py
# Author:      Jakiro
# Datetime:    2021/9/10 16:59
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import os

# write函数

# writelines函数
fp = open('xxx.txt', 'w+', encoding='utf-8')
a = ['a\n','b\n','c\n']
fp.writelines(a)
fp.close()

tmp_lines = os.popen(f'tail -10f xxx.txt')
for tmp_line in tmp_lines:
    print(tmp_line)

