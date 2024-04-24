# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   auto_iframe
# FileName:     string_template.py
# Author:      Jakiro
# Datetime:    2022/5/30 17:52
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
from string import Template
import yaml
import json


class ParamsTemplate(Template):
    delimiter = '!'


with open(r'/Users/qiujie/study/auto_test/auto_iframe/debug/testLogin.yaml', mode='r') as yf:
    datacase = yaml.load(yf)

# print(datacase)
# print('=' * 20)
# print(datacase.get('steps', None))
context = datacase.get('context', None)
context.update({'accounts':'qiujie','pwd':1213})
# print(context)
for step in datacase.get('steps', None):
    # print(type(step))

    for key in step.keys():
        # print(key)
        if not key.startswith("_"):
            # 拿到符合条件的key的value
            target_obj = step.get(key)
            print(type(json.dumps(target_obj)))
            # 将需要替换的字符串实例化
            string = ParamsTemplate(json.dumps(target_obj))
            # 将需要替换的字段标记出来
            print(type(**context))
            value = string.substitute(**context)
            json_obj = json.loads(value)
            step.update({key: json_obj})
        print(step)

# datas = {'context': {'host': 'shop-xo.hctestedu.com', 'port': '80'}, 'steps': [{'assert_options': [
#     {'errorMsg': 'code不等于0', 'target': '$.code', 'type': 'equals', 'value': '0'},
#     {'errorMsg': 'token不存在', 'target': '$.data.token', 'type': 'exists', 'value': ''}],
#     'data': {'accounts': '!accounts',
#              'pwd': '!pwd',
#              'type': 'username'},
#     'extract_options': [
#         {'target': '$.data.token',
#          'varname': 'login_token'}],
#     'method': 'post',
#     'url': 'http://!host:!port/index.php?s=/api/user/login&application=app'}],
#          'ddts': [{'accounts': 'sanfeng', 'pwd': 'ttt', 'desc': '正确的用户名，错误的密码'},
#                   {'accounts': 'sanfen', 'pwd': 'sanfeng', 'desc': '错误的用户名，正确的密码'},
#                   {'accounts': 'sanfeng', 'pwd': 'sanfeng', 'desc': '正确的用户名，正确的密码'}]}

steps = [{'assert_options': [{'errorMsg': 'code不等于0', 'target': '$.code', 'type': 'equals', 'value': '0'},
                             {'errorMsg': 'token不存在', 'target': '$.data.token', 'type': 'exists', 'value': ''}],
          'data': {'accounts': '!accounts', 'pwd': '!pwd', 'type': 'username'},
          'extract_options': [{'target': '$.data.token', 'varname': 'login_token'}], 'method': 'post',
          'url': 'http://!host:!port/index.php?s=/api/user/login&application=app'}]
context = {'host': 'shop-xo.hctestedu.com', 'port': '80','accounts':'qiujie'}
