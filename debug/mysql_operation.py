import requests
import re
import os
from bs4 import BeautifulSoup
import pymysql
data = {'Email':'luhaotian1@zhuozhuo.io','Password':'Aa111111+'}

session2 = requests.Session()

r = session2.post('https://101.132.38.80:25601/?n=acnSdp.httpApi.AdminSignInAction',data = data,verify=False)
session = re.findall("Session=(.*?); Path=/;",r.headers['Set-Cookie'])
cookies = r.cookies
cookie = requests.utils.dict_from_cookiejar(cookies)


twofa = os.popen('kmg 2fa KH2KFBHMKNKE2VQTNDEXVXALKKYLV6D7').read()
data = {'googleCode':twofa,'clientTime':'Wed May 18 2022 15:17:46 GMT+0800'}
r = session2.post('https://101.132.38.80:25601/?n=acnSdp.httpApi.CtUserSignInCheckGoogleAuthAction',data= data,cookies = cookie,verify=False)



class Mysql_Operation:

    def __init__(self):
        # 临时存放当前获取到的数据库表名的键值对
        self.mysql_dict={}
        # 临时存放获取到dict.txt文件中数据库表名的键值对
        self.dict_1 = {}
        # 新增k1表
        self.del_list = []
        # 被删除的k1表
        self.add_list = []



    def current_db_k1_dict(self):
        """
        把数据库的k1名和table name以键值对形式存放在字典中
        :return: mysql_dict
        """



        self.r = session2.get('https://101.132.38.80:25601/?dbServerName=controller&n=tvhdr8xcqp.CurrentDbK1ListPage',verify=False)
        # 使用BeautifulSoup方法把get获取到的text转化成html的树结构
        self.soup = BeautifulSoup(self.r.text)
        # 使用tag对象类型，只获取html中tbody下面的内容
        self.soup_tbody = self.soup.tbody
        # 使用.contents，把soup_tbody子节点以列表形式输出
        self.soup_tbody_contents = self.soup_tbody.contents

        print(self.soup_tbody_contents)

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
            with open('dict.txt','r',encoding='utf-8') as f:
                self.lines = f.readlines()
        except:
            print('没有dict.txt文件，请先用save_table_k1_name创建dict.txt文件')
            raise

        # 读取dict.txt文件中的数据，把数据存如dict_1中
        for line in self.lines:
            line = line.replace('\n','')
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

    def select_table_name(self,name):
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

    def select_user_id(self,host,db,user,password,port,name):
        """
        查询userid``````
        :param host:数据库的地址
        :param db:库名
        :param user:登录数据库的用户名
        :param password:登录数据库的密码
        :param port:数据库的端口号
        :param name:查询的用户的用户名
        :return:用户的userid值
        """
        Mysql_Operation.current_db_k1_dict(self)

        self.conn = pymysql.connect(host=host,db=db,user=user,password=password,port=port)
        self.cursor = self.conn.cursor()
        table_name = Mysql_Operation.select_table_name(self,'k1NameToId')
        ql_select_user_id = 'select * from {} where k="{}"'.format(table_name,name)
        self.cursor.execute(ql_select_user_id)
        result = self.cursor.fetchone()
        user_id = str(result[1])[2:-1:]
        self.cursor.close()
        self.conn.close()
        return user_id

    def select_org_id(self,host,db,user,password,port,name):
        """
        查询orgid
        :param host:数据库的地址
        :param db:  库名
        :param user:登录数据库的用户名
        :param password:登录数据库的密码
        :param port: 数据库的端口号
        :param name: 查询使用的组织名
        turn:组织的orgid值
        """
        Mysql_Operation.current_db_k1_dict(self)
        self.conn = pymysql.connect(host=host,db=db,user=user,password=password,port=port)
        self.cursor = self.conn.cursor()
        table_name = Mysql_Operation.select_table_name(self,'K1Org')
        ql_select_org_id = 'select * from {} where v="{}"'.format(table_name,name)
        self.cursor.execute(ql_select_org_id)
        result = self.cursor.fetchone()
        self.org_id = str(result[0])[2:-1:]
        self.cursor.close()
        self.conn.close()
        return self.org_id

    def select_group_id(self,host,db,user,password,port,name):
        self.conn = pymysql.connect(host=host,db=db,user=user,password=password,port=port)
        self.cursor = self.conn.cursor()
        table_name = Mysql_Operation.select_table_name(self,'')
        ql_select_org_id = 'select * from {} where v="{}"'.format(table_name,name)
        self.cursor.execute(ql_select_org_id)
        result = self.cursor.fetchone()









mq = Mysql_Operation()

mq.current_db_k1_dict()
# user_id = mq.select_user_id('101.132.38.80','9ktam4gyqd','root','',3306,'luhaotian')
# print(user_id)
# org_id = mq.select_org_id('101.132.38.80','9ktam4gyqd','root','',3306,'11')
# print(org_id)




