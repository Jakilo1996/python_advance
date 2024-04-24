# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     command_line_getopt.py
# Author:      Jakiro
# Datetime:    2022/5/24 11:40
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import sys, getopt

# getopt
#  getopt是我们经常使用的函数，下面我们来看看它的函数说明吧。
#
# getopt(args, shortopts, longopts=[]) -> opts, args
#
#
# args: 指的是当前脚本需要解析的参数列表，通常是sys.argv[1:]
#
# shortopts: 短参数，类似于 python test.py -h。短参数是一个字符串，如果带有冒号:表示这个选项后面必须要有一个参数。比如'-h-v-i:-o:'表示-i和-o的后面需要接参数。
#
# longopts: 长参数，类似于 python test.py --help。长参数是一个可选参数，它是一个list列表。如果选项后面必须接参数，则需要加个=。比如['help', 'version', 'input=', 'output=']表示input和output后面需要接参数。
#
# 调用方式：
#
#  短参数：-参数名[空格]参数值
#
#  长参数：--参数名=参数值
#
# getopt函数的返回值是一个包含两个列表的元组
#
# opts
#
# args
#
# opts是一个列表，列表每个值是(option, value)对。比如("-o", "outputname")
#
# args其他参数列表，它包含不属于格式信息的剩余的命令行参数。



# case1
# try:
#     opts,args = getopt.getopt(sys.argv[1:],'-h-v-i:-o:',['help','version','input=','output='])
# finally:
#     print(opts)
#     print(args)

    # ***** 如果命令行传入的参数错误，比如有空格，之后的所有参数都将被识别为不属于格式信息的剩余命令行参数
    # output
    # python command_line_getopt.py -h -v -i:输入 -o:输出 --help --version --input=输入2 --output=输出2 other_arg1 other_arg2=2
    # [('-h', ''), ('-v', ''), ('-i', ':输入'), ('-o', ':输出'), ('--help', ''), ('--version', ''), ('--input', '输入2'), ('--output', '输出2')]
    # ['other_arg1', 'other_arg2=2']


# case2
try:
    # opts: 包含选项和值  args: 不属于格式信息的剩余的命令行参数
    # :和=表示后面必须要接参数
    opts, args = getopt.getopt(sys.argv[1:], '-h-v-i:-o:', ['help', 'version', 'input=', 'output='])
except getopt.GetoptError as e:
    print(e)
    print('usage: python %s -i <inputfile> -o <outputfile>' % __file__)
    print('   or: python %s --input=<inputfile> --output=<outputfile>' % __file__)
#
print(opts)

# for option, value in opts:
#     if option in ('-h', '--help'):
#         print('usage: python %s -i <inputfile> -o <outputfile>' % __file__)
#         print('   or: python %s --input=<inputfile> --output=<outputfile>' % __file__)
#     elif option in ('-v', '--version'):
#         print('Version is 0.01')
#     elif option in ('-i', '--input'):
#         print('input file is: %s' % value)
#     elif option in ('-o', '--output'):
#         print('output file is: %s' % value)
print('args = %s' % args)
for index, arg in enumerate(args):
    print('Other argument_%s: %s' % (index+1, arg))