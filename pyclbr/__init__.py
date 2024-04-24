# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     __init__.py.py
# Author:      Jakiro
# Datetime:    2022/7/12 11:04
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import os
import pkgutil  # 包扩展工具
import pyclbr   # pyclbr：Python类浏览支持




# 这段代码 -- 描述了 --- pytest 是如何找到 具体要执行的测试方法的
if __name__ == '__main__':
    cur_dir = os.path.dirname(__file__)
    # 读取路径下 所有的模块
    for module in pkgutil.iter_modules([cur_dir]):
        # 读取模块内的类
        m = pyclbr.readmodule(module.name, [cur_dir])
        for classname in m.keys():
            print("搜寻到类：",m[classname].name)
            # 如果是test开头的方法，就执行它
            if m[classname].name.startswith("Test"):
                for method in m[classname].methods:
                    print("搜寻到方法：", method)