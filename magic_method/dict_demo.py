# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     dict_demo.py
# Author:      Jakiro
# Datetime:    2022/12/13 12:08
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

c = {
    'a': {
        'a1': 2,
        'a2': {
            'a21': 3
        }
    },
    'b': 2,
    'c': 3
}


class DotDict(dict):
    '''
    字典支持.key递归出所有value
    '''
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        value = self[key]
        if isinstance(value, dict):
            value = DotDict(value)
        return value


dict1 = DotDict(c)
print(dict1.a.a2.a21)


class MyDict(dict):
    # 处理两层嵌套
    def __init__(self, *args, **kwargs):
        super(MyDict, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        super(MyDict, self).__setitem__(key, value)
        for k in self.keys():
            # print(k, self[k])
            if isinstance(self[k], dict):
                # print(self[k])
                self[k][key] = value


a = {
    'a': 1,
    'b': 2,
    'c': {
        'a': 1
    }
}


# b = MyDict(a)
# b['a'] = 2
# print(b)


class MyDict2(dict):
    # 处理多层嵌套
    def __init__(self, *args, **kwargs):
        super(MyDict2, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        super(MyDict2, self).__setitem__(key, value)
        for k in self.keys():

            if isinstance(self[k], dict):
                dict2 = MyDict2(self[k])

                dict2.__setitem__(key, value)

                super(MyDict2, self).__setitem__(k, dict2)


a = {
    'a': 1,
    'b': 2,
    'c': {
        'a': 1,
        'b': {
            'a': 1,
            'd': {
                'a': 1
            }
        }
    }
}
c = MyDict2(a)
c['a'] = 2
print(c)
