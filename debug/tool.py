"""
二次封装selenium的工具
"""
from selenium import webdriver
# 使用显示等待查找元素更好控制时间以及报错
from selenium.webdriver.support.wait import WebDriverWait
# 使用 EC模块对网页的元素是否存在进行判定
from selenium.webdriver.support import expected_conditions as EC
from common.webelement import SignUpInElemnet
import os
from common.operate import MysqlSelect
import os
import paramiko

class Tool:
    def __init__(self):
        """
        初始化浏览器
        """
        options = webdriver.ChromeOptions()
        # 忽略https证书错误
        options.add_argument('--ignore-certificate-errors')
        # 忽略其他无关日志错误
        options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
        self.driver = webdriver.Chrome('/Users/luhaotian/Desktop/chromedriver',options=options)
        # self.driver.set_window_size(1080,720)
        self.driver.maximize_window()

    def open_url(self, url):
        """
        打开网页
        """
        # url = "http://" + url
        # self.driver.maximize_window
        self.driver.get(url)

    def element_find(self, locator, timeout=5, index=0):
        """
        查找网页上单个元素
        使用 element——list 全局查找，默认使用返回元素列表的第一个位，支持自己传入其它index，使用不同element
        """
        try:
            element = self.elements_find_list(locator=locator, timeout=timeout)
            return element[index]
        except Exception as msg:
            print(f'该{locator}没有找到\n{msg}')

    def elements_find_list(self, locator, timeout=10):
        """寻找网络上同属性值的所有元素"""
        try:
            elements_list = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return elements_list
        except Exception as msg:
            print(f'该{locator}list没有找到\n{msg}')

    def send_key(self, locator=None, text=None,  index=0):
        """
        输入字符
        """
        element = self.element_find(locator, index=index)
        # 输入之前清除输入框
        element.clear()
        element.send_keys(text)

    def clicks(self, locator, timeout=5):
        """点击元素"""
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def quit_browser(self):
        """
        关闭浏览器
        """
        self.driver.quit()

    def refresh_windows(self):
        """
        刷新当前网页窗口
        """
        self.driver.refresh()

    def judge_element_view(self, locator, time=10):
        """
        判断元素的文本值是否可见
        可见返回元素本身
        不可见返回False
        """
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        
        except Exception as msg:
            print(f'{locator}该元素找不到:\n{msg}')
            return False

    def judge_element_text(self, locator, text, time=10):
        """
        获得元素的文本信息，判断是否相等
        相等就返回True
        """
        try:
            result = WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except Exception as msg:
            result = f'该{locator}元素文本错误：\n{msg}'
            return result

    def get_web_text(self, locator, time=10):
        """ 得到网页上可见元素的文本信息 """
        try:
            text = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return text.text
        except Exception as msg:
            print(f'{locator}文本不可见\n{msg}')
            return False

    def judge_element_value(self, locator=None, timeout=10, text=None):
        """判断元素的value值"""
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text))
            return result
        except Exception as msg:
            print(f'该元素找不到,\n{msg}')

    def wait_element_vanish(self, locator=None, time=10):
        """
        等待元素消失
        元素消失返回false
        未消失，退出当前循环，继续循环
#### #设置时间的更改
        """
        while True:
            try:
                v = WebDriverWait(self.driver, time).until_not(EC.visibility_of_element_located(locator))
                print(f'可见元素已消失:{v}')
                break
            except:
                print('可见元素未消失')
                continue

    def get_input_text(self, locator):
        """获取输入框的文本信息"""
        text = self.judge_element_view(locator)
        return text.get_attribute('value')

    def judge_element_exist(self, element_list):
        """判断一系列元素是否存在"""
        for x in element_list:
            result = self.judge_element_view(x)
            # print(f'这是：{result}\n')
            if result is False:
                print(f'该{x}不可见')
                break
            else:
                return True

    def set_net_conditions(self, offline=False, latency=5, throughput=500 * 1024):
        """
        设置网络环境
        offline:网络状态设置，默认为Fales(不断网），True(断网）
        latency:网络延迟设置，默认5ms
        throughput:可以直接设置上下行网络速率
        """
        self.driver.set_network_conditions(offline=offline, latency=latency, throughput=throughput)

    def new_window_open(self, new_web):
        """打开新窗口"""
        new_web = "http://" + new_web
        # 创建js语句
        js = "window.open"+f'("{new_web}")'+";"
        # 执行js 语句
        self.driver.execute_script(js)

    def save_current_window(self):
        """保存当前窗口句柄"""
        # mainWindow变量保存当前窗口的句柄
        mainWindow = self.driver.current_window_handle
        return mainWindow

    def save_all_window(self):
        """储存所有窗口的句柄"""
        allHandles = self.driver.window_handles
        return allHandles

    def click_other_window(self, handle):
        """进入其他窗口"""
        self.driver.switch_to.window(handle)

    def switch_frame(self, frame_name=None):
        """ 切换新窗口 """
        self.driver.switch_to.frame(frame_name)

    def screenshot_element(self, locator, path:str,  index=0):
        """ 获取 元素的截图 """
        el = self.element_find(locator, index=index)
        el.screenshot(path)

    def full_screenshot(self, filename):
        """ 获取全局截图 """
        import os
        p = os.path.abspath(".")
        # print(p)
        # 注意转义字符的问题， 需要输出 \ 时 ，需要两个 \\
        n = os.path.join(p, "image\\", filename)
        # print(n)
        self.driver.get_screenshot_as_file(n)

    def get_url_current(self):
        return self.driver.current_url

    def email_login(self,url,email,password):

        self.open_url(url)
        self.send_key(SignUpInElemnet.email_input.value,email)
        self.send_key(SignUpInElemnet.password_input.value,password)
        self.clicks(SignUpInElemnet.sing_in_btn.value)
        with MysqlSelect(ip='106.15.50.141',user='test',password='123456',dbname='y9k2',port=3306,sql='select * from kmg2md5_f03e5fdd05ebee4e224c8f80e8068124 where k="luhaotian1@zhuozhuo.io"') as pf:
            two_fa = str(pf[0][1])[2:-1:]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('106.15.50.141', 22, 'root', '')




        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(f'sdpController  DoubleAuthTypeSetAsGoogle ')

        # stdin, stdout, stderr = ssh.exec_command(f'sdpController  DoubleAuthTypeSetAsGoogle && ./twoFaDecrypt -UserId {two_fa} -Psk y63m6mysx5n7sacn3jm43d9d9j6ww7ur')
        # ssh.exec_command(f'./twoFaDecrypt -UserId {two_fa} -Psk y63m6mysx5n7sacn3jm43d9d9j6ww7ur')

        # 获取命令结果
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        a = result.decode('utf-8')
        two_fa_key = a[10::]
        two_fa_code = os.popen(f'kmg 2fa {two_fa_key}').read()




        ssh.close()

        print(two_fa_code)

        self.send_key(SignUpInElemnet.two_fa_window.value,two_fa_code)

    # def add_getaway(self):




