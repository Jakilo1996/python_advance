# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     demo99.py
# Author:      Jakiro
# Datetime:    2023/5/10 18:09
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
import unittest
# from lib2to3.pgen2 import browser  #这个导入进来的好像也是个驱动
from selenium import webdriver
import time
# from selenium.webdriver.common.by import By
#
# class tst(unittest.TestCase):
#     def test_something(self, ):
#         browser = webdriver.Chrome()  # 这一步的意思就是实例化驱动
#         time.sleep(3)
#         URL = browser.get("http://192.168.12.1/cgi-bin/luci")
# #        browser.get(url)
#         time.sleep(5)
#         # 登录管理页面¡
#         browser.find_element(By.NAME, '//*[@id="focus_password"]').send_keys('admin')
#         browser.find_element(By.XPATH, '//*[@id="login_form"]/div[2]/input').click()
#         browser.find_element_by_xpath()


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://192.168.12.1/cgi-bin/luci/')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="login_form"]/div[1]/input[2]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/input').click()