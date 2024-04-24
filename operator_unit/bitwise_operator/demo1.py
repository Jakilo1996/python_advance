# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     argparse_desc.py
# Author:      Jakiro
# Datetime:    2022/4/28 11:46
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

#  不用 + 完成加运算
class Solution():
    def add(self, num1, num2):
        xorNum = num1 ^ num2
        addNum = num1 & num2 << 1
        while addNum:
            tmp1 = xorNum ^ addNum
            tmp2 = (xorNum & addNum) << 1
            tmp1 = tmp1 & 0xFFFFFFFF  # 32个1
            xorNum = tmp1
            addNum = tmp2
        return xorNum if xorNum <= 0x7FFFFFFFF else ~(xorNum ^ 0x100000000)
    # 0x7FFFFFFFF 32位最大带符号整数

s = Solution()
print(s.add(1,2))


