# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Jakiro_pro
# FileName:     requests_post.py
# Author:      Jakiro
# Datetime:    2022/3/24 15:37
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import requests

see = requests.session()

# 根据协议类型，选择不同的代理
proxies = {
    "http": "http://127.0.0.1:8888",
    # "https": "http://12.34.56.79:9527",
}
post_params = {
    'id': 1
}

get_res = see.get(url='http://127.0.0.1:5000/login/?id-1', proxies=proxies)
print(get_res.text)

# get_res = see.get(url='http://127.0.0.1:5000/login/',params=post_params, proxies=proxies)
# print(get_res.text)

# get_res = see.post(url='http://127.0.0.1:5000/login/?id=1', proxies=proxies)
# print(get_res.text)

# 1）请求正文是application/x-www-form-urlencoded
# 形式：
# 1requests.post(url=’’,data={‘key1’:‘value1’,‘key2’:‘value2’},headers={‘Content-Type’:‘application/x-www-form-urlencoded’})
# Reqeusts支持以form表单形式发送post请求，只需要将请求的参数构造成一个字典，然后传给requests.post()的data参数即可。

# post_params = {
#     'id': 1
# }
# headers = {
#     "Content-Type" : 'application/x-www-form-urlencoded'
# }
# headers = {'Content-Type': 'multipart/form-data'}
# post_res = see.post('http://127.0.0.1:5000/login/',headers=headers, data=post_params, proxies=proxies)
# print(post_res.text)
# headers = {'Content-Type': 'multipart/form-data'}
# files = {'file': open('/Users/qiujie/pythonProject/python_study/Jakiro_pro/debug/aaa.txt', 'rb')}
# post_res = see.post('http://127.0.0.1:5000/login/', data=post_params, proxies=proxies)
# print(post_res.text)


# 请求正文是multipart/form-data   传输文件对象的时候需要额外处理
# 除了传统的application/x-www-form-urlencoded表单，我们另一个经常用到的是上传文件用的表单，这种表单的类型为multipart/form-data。
# 形式：1 requests.post(url='',data={'key1':'value1','key2':'value2'},headers={'Content-Type':'multipart/form-data'})
# headers = {'Content-Type': 'multipart/form-data'}
# post_params = {
#     'id': 1
# }
# #
# files = {'file': open('/Users/qiujie/pythonProject/python_study/Jakiro_pro/debug/aaa.txt', 'rb')}
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, proxies=proxies, )
# print(post_res.text)

# from requests_toolbelt import MultipartEncoder
# # #
# m = MultipartEncoder(
#     fields={
#
#             'field2': (
#                 'filename', open('/Users/qiujie/pythonProject/python_study/Jakiro_pro/debug/aaa.txt', 'rb'),
#                 'text/plain')}
# )
# headers = {'Content-Type': m.content_type}
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, data=m, proxies=proxies, )

# headers = {'Content-Type': 'multipart/form-data'}
# 不需要文件  request.from 可以拿到表单的前两个，暂不知道怎么取文件
# m2 = MultipartEncoder(fields={'a': '2', 'b': '3'})
# headers = {'Content-Type': m2.content_type}
#
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, data=m2, proxies=proxies, )
# print(post_res.text)
# fp.close()
# print(post_res.text)
# print(post_res.json_unit())

# （3）请求正文是raw 传入xml格式文本
# headers = {'Content-Type': 'text/xml'}
# data2 = '<?xml ?>'
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, data=data2, proxies=proxies, )
# print(post_res.text)

# （3）请求正文是raw 传入html格式文本
# headers = {'Content-Type': 'text/html'}
# data2 = '<html>sdajk0</html>'
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, data=data2, proxies=proxies, )
# print(post_res.text)

# （3）请求正文是raw 传入text格式文本
# headers = {'Content-Type': 'text/text'}
# data2 = '<html>sdajk0</html>'
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, data=data2, proxies=proxies, )
# print(post_res.text)

# （3）请求正文是raw 传入文本格式
# headers = {'Content-Type': 'text/plain'}
# data2 = '<html>sdajk0</html>'
# post_res = see.post('http://127.0.0.1:5000/login/', headers=headers, data=data2, proxies=proxies, )
# print(post_res.text)

# （3）请求正文是raw 传入json格式文本
import json_unit

# 通过post传参
# post_res = see.post(url='http://127.0.0.1:5000/login/',data=json_unit.dumps(post_params ),headers={'Content-Type':'application/json_unit'},proxies=proxies)
# print(post_res.text)

# 通过json传参
# post_res = requests.post(url='http://127.0.0.1:5000/login/',json_unit=json_unit.dumps({'key1':'value1','key2':'value2'}),headers={'Content-Type':'application/json_unit'},proxies=proxies,)
# print(post_res.text)


# （4）请求正文是binary 可以通过该方式传递文件对象

# files = {'file': open('/Users/qiujie/pythonProject/python_study/Jakiro_pro/debug/aaa.txt', 'rb')}
# headers = {'Content-Type': 'binary'}
# post_res = see.post(url='http://127.0.0.1:5000/login/', files=files, headers=headers, proxies=proxies)
# print(post_res.text)
res = see.get(url='http://127.0.0.1:5000/redirect/', proxies=proxies)
print(res.text)