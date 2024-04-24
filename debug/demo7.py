# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   code
# FileName:     demo7.py
# Author:      Jakiro
# Datetime:    2022/5/19 16:41
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import requests
import re
import os
from bs4 import BeautifulSoup
import pymysql

data = {'Email': 'luhaotian1@zhuozhuo.io', 'Password': 'Aa111111+'}

session2 = requests.Session()

r = session2.post('https://101.132.38.80:25601/?n=acnSdp.httpApi.AdminSignInAction', data=data, verify=False)
session = re.findall("Session=(.*?); Path=/;", r.headers['Set-Cookie'])
cookies = r.cookies
cookie = requests.utils.dict_from_cookiejar(cookies)

twofa = os.popen('kmg 2fa KH2KFBHMKNKE2VQTNDEXVXALKKYLV6D7').read()
data = {'googleCode': twofa, 'clientTime': 'Wed May 18 2022 15:17:46 GMT+0800'}
r = session2.post('https://101.132.38.80:25601/?n=acnSdp.httpApi.CtUserSignInCheckGoogleAuthAction', data=data,
                  cookies=cookie, verify=False)


from functools import wraps


class ContextMangerBase():
    # 通用方法，用于将一个函数改变为上下文处理器
    def __init__(self, func, args, kwargs):
        # print(args)
        self.gene = func(*args, **kwargs)

    def __enter__(self):
        # print('__enter__')
        try:
            return next(self.gene)
        except StopIteration:
            raise RuntimeError('generation did`t yield') from None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('__exit__')
        if exc_type == None:
            try:
                # print('__exit__try')
                next(self.gene)
            # 此处的作用是为了忽略 迭代对象 第二次next 的 StopIteration异常
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")

        else:
            try:
                self.gene.throw(exc_type, exc_val, exc_tb)
            except:
                raise
            raise RuntimeError("generator didn't stop after throw()")


def context_manager(func, ):
    '''
    params: func 被装饰的函数对象，必须是一个生成器函数，缺省参数为装饰器函数的实参
    '''

    @wraps(func)
    def inner(*args, **kwargs):
        return ContextMangerBase(func, args, kwargs)

    return inner


class Mysql_Operation:

    def __init__(self, host=None, db=None, user=None, password=None, port=None):
        # 临时存放当前获取到的数据库表名的键值对
        self.mysql_dict = {}
        # 临时存放获取到dict.txt文件中数据库表名的键值对
        self.dict_1 = {}
        # 新增k1表
        self.del_list = []
        # 被删除的k1表
        self.add_list = []
        # 当前访问数据库的地址
        self.host = host
        # 当前访问的数据库名
        self.db = db
        # 当前访问的数据库的登录用户
        self.user = user
        # 当前访问数据库的密码
        self.password = password
        # 数据库服务器所在的端口
        self.port = port
        # 数据库的常用表数据位置信息
        self.common_table_info = {'user_id': {'table_name': 'k1NameToId', 'result_index': 1,'where_condition':'k' },
                                  'org_id': {'table_name': 'K1Org', 'result_index': 0,'where_condition':'v' },
                                  'group_id': []}

    def current_db_k1_dict(self):
        """
        把数据库的k1名和table name以键值对形式存放在字典中
        :return: mysql_dict
        """

        self.r = session2.get('https://101.132.38.80:25601/?dbServerName=controller&n=tvhdr8xcqp.CurrentDbK1ListPage',
                              verify=False)
        # 使用BeautifulSoup方法把get获取到的text转化成html的树结构
        # 使用feetures 指定xml的特色
        self.soup = BeautifulSoup(self.r.text,features='lxml')
        # 使用tag对象类型，只获取html中tbody下面的内容
        self.soup_tbody = self.soup.tbody
        # 使用.contents，把soup_tbody子节点以列表形式输出
        self.soup_tbody_contents = self.soup_tbody.contents

        # 把数据库k1名和table name，放进字典中
        for i in range(0, len(self.soup_tbody_contents)):
            self.s = str(self.soup_tbody_contents[i])
            self.str_split = self.s.split('<td>')
            self.key = self.str_split[3].replace('</td>', '')

            self.value = self.str_split[4].replace('</td>', '')
            self.mysql_dict[self.key] = self.value
        return self.mysql_dict

    def save_table_k1_name(self):
        """
        把字典中的数据库表名覆盖写入到dict表中
        :return:
        """

        # 将字典中的内容写入到txt文件中
        with open('dict.txt', 'a', encoding='utf-8') as f:
            f.truncate(0)
        for k, v in self.mysql_dict.items():
            with open('dict.txt', 'a', encoding='utf-8') as f:
                f.write(k)
                f.write(':')
                f.write(v)
                f.write('\n')

    def check_table_add_and_del(self):
        """
        检查数据库的表是否有更新
        :return:
        """
        try:
            with open('dict.txt', 'r', encoding='utf-8') as f:
                self.lines = f.readlines()
        except:
            print('没有dict.txt文件，请先用save_table_k1_name创建dict.txt文件')
            raise
        # 读取dict.txt文件中的数据，把数据存如dict_1中
        for line in self.lines:
            line = line.replace('\n', '')
            line = line.split(':')
            self.dict_1[line[0]] = line[1]
        print(self.dict_1)

        # 对比新旧数据库表，验证是否有减少
        for k in self.dict_1.keys():
            try:
                self.mysql_dict[k]
            except KeyError:
                self.del_list.append(k)
        # 对比新旧数据库表，验证是否有新增
        for k in self.mysql_dict:
            try:
                self.dict_1[k]

            except KeyError:
                self.add_list.append(k)

        print('新增k1表：{}'.format(self.add_list))
        print('被删除的k1表：{}'.format(self.del_list))

    def select_table_name(self, name):
        """
        调用前需要先去使用把k1表名转成加密后的表名
        :param name:k1表名
        :return:加密后的表名
        """
        try:
            self.table_name = self.mysql_dict[name]
        except:
            print('表名错误')
            raise
        return self.table_name


    @context_manager
    def database_base_context(self):
        '''
        返回一个游标，自动根据实例的数据库信息，进行数据库连接操作，处理连接与关闭数据库操作
        '''
        try:
            Mysql_Operation.current_db_k1_dict(self)
            conn = pymysql.connect(host=self.host, db=self.db, user=self.user, password=self.password,
                                   port=self.port)
            cursor = conn.cursor()
            yield cursor
        finally:
            cursor.close()
            conn.close()

    def update_database_info(self, host, db, user, password, port):
        '''
        如果在实例化时未传递数据库信息，使用此方法更新数据库信息
        如果想要修改默认的数据库链接信息 也可以调用此方法
        '''
        self.host =host
        self.db = db
        self.user = user
        self.password = password
        self.port = port


    def select_data(self, data_type: str, value: str):
        '''
        传入自定义的常用查询类型以及查询值， 返回指定的id信息
        params: data_type 传入自定义的可用的common_table_info 的key 如不存在 报ValueError
        params: value 传入自定义的
        '''
        if data_type not in self.common_table_info.keys():
            raise ValueError('wrong data_type')
        else:
            with self.database_base_context() as cursor:
                table_name = Mysql_Operation.select_table_name(self, self.common_table_info[data_type]['table_name'])
                try:
                    ql_select = f'select * from {table_name} where { self.common_table_info[data_type]["where_condition"]}="{value}"'
                    cursor.execute(ql_select)
                    result = str(cursor.fetchone()[self.common_table_info[data_type]['result_index']])[2:-1:]
                    return f'select_table:{data_type},select_data{value},result:{result}'
                except:
                    raise ValueError('data_value not found')


if __name__ == '__main__':
    # 执行此实例化  就不需要更新数据库信息
    # mq = Mysql_Operation('101.132.38.80', '9ktam4gyqd', 'root', '', 3306)
    # 实例化时，如果不传递数据库信息，就不更新数据库信息
    mq = Mysql_Operation()

    mq.check_table_add_and_del()
    # 如果不需要进行数据库操作，就不调用此方法
    mq.update_database_info('101.132.38.80', '9ktam4gyqd', 'root', '', 3306)


    user_id = mq.select_data('user_id', 'luhaotian')
    print(user_id)
    org_id = mq.select_data('org_id', '11')
    print(org_id)
