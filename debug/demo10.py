# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo10.py
# Author:      Jakiro
# Datetime:    2022/6/15 20:15
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import openpyxl


def sheet_data_to_python(file_path: str, sheet: str) -> list:
    '''
    将sheet页中的数据转换为列表
    :param sheet:
    :return:根据sheet名，将当前sheet页的数据转换为[[first_cell,second],second_row]
    '''
    # 忽略全空的行
    wb = openpyxl.load_workbook(file_path, data_only=True)
    all_lists = []
    one_line_data_list = []
    current_sheet_count = 0
    current_ignore_first_row = True
    try:
        ws = wb[sheet]
    except:
        raise ValueError('Wrong Sheet Name')

    for row_tuple in ws:
        if current_ignore_first_row:
            current_ignore_first_row = False
            continue
        # 认为前几列数据需要打印，否则会打印一堆None
        for cell in list(row_tuple):
            # 拼接 value

            one_line_data_list.append(cell.value)
            # 转化成元组
            one_line_data_tuple = tuple(one_line_data_list)
        if row_tuple[0].value:
            current_sheet_count += 1
        # 清空临时列表
        one_line_data_list.clear()
        # 将临时元组添加到总列表中
        all_lists.append(one_line_data_tuple)
    print(f'当前sheet页行数:{current_sheet_count}')

    return all_lists
