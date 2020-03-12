'''
作者：seak
时间：
项目：
题目：
作用：
备注：银行登陆
1.将重复的条件放入前置条件， 打开游览器，关闭游览器
2.再写一个用例发现他们的执行逻辑是一样的就需要进行封装
3. 要将数据传入进去就用ddt数据驱动来管理数据
4.进行函数封装，使用PO模式进行页面和数据的分离,将login重新定义一个函数,（函数封装以后的代码逻辑）
5.进行类封装，将页面和代码逻辑进行分离，创建一个pages目录和datas目录

'''

import unittest
import ddt
from selenium import webdriver
from pages.login_bank_page import LoginPage

#要将数据传入进去就用ddt数据驱动来管理数据
test_data = [
    {"username":"", "pwd": "", "expected": "请输入用户名"},
    {"username":"", "pwd": "123", "expected": "请输入用户名"},
]

@ddt.ddt
class TestLogin(unittest.TestCase):

    #前置条件将重复的逻辑都放在前置条件里面
    def setUp(self) -> None:
        # 1， 打开浏览器；
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(20)

        # 初始化要用到的页面
        self.login_page = LoginPage(self.driver)


    #关闭游览器
    def tearDown(self) -> None:
        self.driver.quit()

    @ddt.data(*test_data)
    def test_login_error(self,test_info):#用test_info来接收test_data拆包后的参数
        """手机号码为空"""
        # 第一个：获取实际结果（封装以后执行的函数或者方法） res = request.visit()
       # actual = login(self.driver, test_info["username"], test_info["pwd"])
        actual = self.login_page.login(test_info['username'], test_info['pwd'])
        # 第二个：获取预期结果 test_info【‘expected’】
        expected = test_info['expected']
        # 第三个：断言
        self.assertEqual(expected, actual)





