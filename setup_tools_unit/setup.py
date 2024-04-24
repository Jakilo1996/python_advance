# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   setup_tools_unit
# FileName:     setup.py
# Author:      Jakiro
# Datetime:    2022/5/26 14:52
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import setuptools

"""
打包成一个 可执行模块
"""
# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()


setuptools.setup(
    # 关于项目的介绍 - 随便写都可以
    # 描述信息
    # 部分参数提供了更多当前应用的细节信息，对打包安装并无任何影响，比如：
    # 应用名
    name="test_setup",
    # 版本号
    version="0.0.1",
    # 作者
    author="hctestedu.com",
    # 作者邮箱
    author_email="zhangfeng0103@live.com",
    # 工具介绍
    description="api 接口自动化测试工具",
    # 证书
    license="GPLv3",
    # 长介绍
    # long_description=long_description,
    # 长介绍类型
    long_description_content_type="text/markdown",
    # 网址
    url="http://www.hctestedu.com",
    # 项目地址
    project_urls={
        "Bug Tracker": "https://github.com/crazyFeng/api-runner/issues",
        "Contact Us": "http://www.hctestedu.com",
    },
    # 分级
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],

    # 需要安装的第三方依赖 -- 工具依赖
    # 们的应用会依赖于第三方的Python包，虽然可以在说明文件中要求用户提前安装依赖包，但毕竟很麻烦，用户还有可能装错版本。其实我们可以在”setup.py”文件中指定依赖包，
    # 然后在使用setuptools安装应用时，依赖包的相应版本就会被自动安装。让我们来修改上例中的”setup.py”文件，加入install_requires参数：
    install_requires=[
        # "pytest",
        # "pytest-html",
        # "jsonpath",
        # "PyYAML",
        # "pyyaml-include",
        "requests"
    ],
    # 上面声明的包会被自动下载安装，如果本地没有 会PyPI安装一个最新版

    # dependency_links=['https://mirrors.aliyun.com/pypi/simple/'],

    # 自动打包当前项目内的所有包 ，参数可以指定路径 比如使用find_packages('src')就表明只在”src”子目录下搜索所有的Python包。
    packages=setuptools.find_packages(),
    # python 版本
    python_requires=">=3.6",
    # 生成一个 可执行文件 例如 windows下面 .exe  指向主函数
    entry_points={
        'console_scripts': [
            # 可执行文件的名称=执行的具体代码方法
            'test_run=src.main:mian'
        ]
    },
    # 决定应用是否作为一个zip压缩后的”egg”文件安装在当前Python环境中，还是作为一个以”.egg”结尾的目录安装在当前环境中。
    # 因为有些工具不支持zip压缩文件，而且压缩后的包也不方便调试，所以建议将其设为False：zip_safe=False。
    zip_safe=False,
    # 是否导入MANIFEST.in目录中的文件
    # include_package_data=False
)
