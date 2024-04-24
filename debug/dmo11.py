# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     dmo11.py
# Author:      Jakiro
# Datetime:    2022/12/13 11:39
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import pytest

dict_1 = {
    'a': 1,
    'b': 2
}


class SingleClass():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingleClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.a = dict_1

    def update(self, k, v):
        self.a[k] = v


def call(param):
    if param['a'] == 0:
        return param['b'] + 1
    elif param['b'] == 1:
        return param['b'] + 2


@pytest.fixture()
def first_fix():
    param_instance = SingleClass()
    param_instance.update('a', 0)
    call(param_instance.a)


@pytest.fixture()
def second_fix():
    param_instance = SingleClass()
    param_instance.update('a', 1)
    call(param_instance.a)


def test_1(first_fix, second_fix):
    assert 1 == 1
