# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_advance_code
# FileName:     fork_d.py
# Author:      Jakiro
# Datetime:    2022/8/10 11:22
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup as be

md_url = "https://ys.mihoyo.com/content/ysCn/getContentList?pageSize=20&pageNum=1&order=asc&channelId=150"
ly_url = "https://ys.mihoyo.com/content/ysCn/getContentList?pageSize=20&pageNum=1&order=asc&channelId=151"
dq_url = "https://ys.mihoyo.com/content/ysCn/getContentList?pageSize=20&pageNum=1&order=asc&channelId=324"


def get_json(_url_):
    req = requests.get(url=_url_)
    if req.status_code == 200:
        return req.json()['data']
    else:
        return None


def clean_data(_data_):
    _return_ = []
    for key in _data_['list']:
        ext = key["ext"]
        data = {key['title']: {
            "角色ICON": ext[0]["value"][0]["url"],
            "电脑端立绘": ext[1]["value"][0]["url"],
            "手机端立绘": ext[15]["value"][0]["url"],
            "角色名字": key['title'],
            "角色属性": ext[3]["value"][0]["url"],
            "角色语言": ext[4]["value"],
            "声优1": ext[5]["value"],
            "声优2": ext[6]["value"],
            "简介": be(ext[7]["value"], "lxml").p.text.strip(),
            "台词": ext[8]["value"][0]["url"],
            "音频": {
                ext[9]["value"][0]["name"]: ext[9]["value"][0]["url"],
                ext[10]["value"][0]["name"]: ext[10]["value"][0]["url"],
                ext[11]["value"][0]["name"]: ext[11]["value"][0]["url"],
                ext[12]["value"][0]["name"]: ext[12]["value"][0]["url"],
                ext[13]["value"][0]["name"]: ext[13]["value"][0]["url"],
                ext[14]["value"][0]["name"]: ext[14]["value"][0]["url"],
            },
        }
        }
        _return_.append(data[key['title']])
    return _return_


def data():
    _json_ = {}
    for url in [md_url, ly_url, dq_url]:
        jsonlist = clean_data(get_json(url))
        for json in jsonlist:
            _json_[json['角色名字']] = json
    return _json_


def lookup(name):
    json = data()[name]
    print("查找角色：", name)
    for key, value in json.items():
        if key == "音频":
            for keys, values in json[key].items():
                print(f"{keys}：{values}")
        else:
            print(f"{key}：{value}")

lookup('胡桃')