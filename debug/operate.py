"""
根据tool 封装常用方法
"""
import pymysql, pyperclip, os, paramiko
import pyzbar.pyzbar as pyzbar
from PIL import Image



class SumOperate:
    """ 其他 常用 非 selenium 类方法 """


   
    @staticmethod
    def get_2fa(code : str):
        """ 执行2fa 获取 验证码"""
        result = os.popen(f'kmg 2fa {code}').read()
        return result

    @staticmethod
    def mysql_opreate(ip:str="139.224.239.215", user:str="root", pw:str=None, dbname:str=None, sql:str=None):
        db = pymysql.connect(host=ip, user=user, password=pw, database=dbname)

        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        db.close()
        return data

    @staticmethod
    def get_phone_code(phone=13882336439):
        p = SumOperate.mysql_opreate(dbname='y9k2', sql=f"select * from kmg2md5_551aad19ecbabf4b1d08cf5c88a43e4f where k='{phone}';")
        # p = str(p[0][1], 'utf-8')

        p = eval(p[0][1])
        print (str(p["Code"]))
        return (str(p["Code"]))

    @staticmethod
    def get_img_info(path:str):
        """
        识别二维码
        """
        img = Image.open(path)
        img.show()
        barcodes = pyzbar.decode(img)
        for x in barcodes:
            return x.data.decode("utf-8")

    @staticmethod
    def get_clip_text():
        print(pyperclip.paste())
        return pyperclip.paste()

    @staticmethod
    def ssh_server(ip, port, username, pw ,cmd):
        """远程连接 服务器， 执行相关命令 """
        # 生成SSH客户端
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(ip, port, username, password=pw)
        stdin,stdout,stderr = s.exec_command(cmd)
        p = stdout.read()
        s.close()
        return p
    
    @staticmethod
    def sever_rest_pw(username="boziyoung@a.a"):
        p = SumOperate.ssh_server("139.224.239.215",22,"root", "", f"sdpController resetUser {username}")
        pw = str(p, encoding="utf-8")
        pw = pw.rsplit('\n')
        return pw[-2]

# SumOperate.get_phone_code()

# p = SumOperate.get_img_info(r"C:\Users\ZZ-WIN12\Desktop\sdpUi\image\1.jpg")
# print(p)

class MysqlSelect:

    def __init__(self,ip:str,user:str,password:str,dbname:str,port:int,sql:str):
        self.ip = ip
        self.user =user
        self.password = password
        self.port = port
        self.dbname = dbname
        self.sql = sql


    def __enter__(self):

        self.db = pymysql.connect(host=self.ip,user=self.user,password=self.password,database=self.dbname,port=self.port)
        self.cursor = self.db.cursor()
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchall()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.db.close()

        if exc_tb !=None:
            print(f'exc_type:{exc_type}')
            print(f'exc_val:{exc_val}')
            print(f'exc_tb:{exc_tb}')