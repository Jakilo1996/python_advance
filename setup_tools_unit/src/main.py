# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   setup_tools_unit
# FileName:     main.py
# Author:      Jakiro
# Datetime:    2022/5/26 14:51
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

# 执行安装文件
# 有了上面的”setup.py”文件，我们就可以打各种包，也可以将应用安装在本地Python环境中。


# 创建egg包
#
# $ python setup.py bdist_egg
# 该命令会在当前目录下的”dist”目录内创建一个”egg”文件，名为”MyApp-1.0-py2.7.egg”。
# 文件名格式就是”应用名-版本号-Python版本.egg”，我本地Python版本是2.7。同时你会注意到，当前目录多了”build”和”MyApp.egg-info”子目录来存放打包的中间结果。
#
# 创建tar.gz包
#
# $ python setup.py sdist --formats=gztar
# 同上例类似，只不过创建的文件类型是”tar.gz”，文件名为”MyApp-1.0.tar.gz”。
#
# 安装应用
#
# $ python setup.py install
# 该命令会将当前的Python应用安装到当前Python环境的”site-packages”目录下，这样其他程序就可以像导入标准库一样导入该应用的代码了。
#
# 开发方式安装
#
# $ python setup.py develop
# 如果应用在开发过程中会频繁变更，每次安装还需要先将原来的版本卸掉，很麻烦。使用”develop”开发方式安装的话，
# 应用代码不会真的被拷贝到本地Python环境的”site-packages”目录下，而是在”site-packages”目录里创建一个指向当前应用位置的链接。这样如果当前位置的源码被改动，就会马上反映到”site-packages”里。

def mian():
    print('hello1')