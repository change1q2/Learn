'''
作者：seak
时间：
项目：
题目：
作用：
备注：登陆的方法
函数封装后的代码逻辑

所有重复的都需要封装只剩下三个东西
1.获取实际结果（封装以后执行的函数或者方法） res = request.visit()
2.获取预期结果 test_info['expected']
3.断言
'''
import ddt
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.index_page import IndexPage

test_data = [
    {"mobile":"", "pwd": "", "expected": "请输入手机号"},
    {"mobile":"123", "pwd": "", "expected": "请输入正确的手机号"},
]

test_data_success = [{"mobile":'18684720553', "pwd":"python", "expected": "登录成功" }]
@ddt.ddt
class TestLogin(unittest.TestCase):

    #将前置条件:需要重复操作的都写在前置条件中
    def setUp(self) -> None:
     #1.打开游览器
        self.driver = webdriver.Chrome()
    #设置隐式等待
        self.driver.implicitly_wait(30)

    #初始化要用到的页面
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

    def tearDown(self) -> None:
        #关闭游览器，直接写driver的话在setUp中的driver传递不过来，所以加上一个self设置为实例属性进行传递

        #driver.quit(0)
        self.driver.quit()


    @ddt.data(*test_data)
    def test_login_erro(self, test_info):
        '''手机号码为空'''

        #封装完了以后一般用例代码只包含这三个(测试代码)

        #1.获取实际结果（封装以后执行的函数或者方法） res = request.visit()
        #actual = login(self.driver,test_info['mobile'], test_info['pwd'])#去定义一个login
        actual = self.login_page.login(test_info['mobile'], test_info['pwd'])

        #2.获取预期结果 test_info['expected']
        expected = test_info['expected']

        #3.断言
        self.assertEqual(expected, actual)

    # #登陆成功
    # @ddt.data(*test_data_success)
    # def test_login_success(self,test_info):
    #     '''登陆成功'''
    #     #执行登陆操作，login_page.login()
    #     self.login_page.login(test_info['mobile'], test_info['pwd'])
    #     # 进入了？？页面  我的帐户[python]
    #     # 定位我的账户
    #
    #     self.index_page.get()
    #     actual = self.index_page.get_element_user()
    #
    #     #预期结果
    #     expected = '我的账户[python]'
    #     self.assertIn(expected, actual.text)

        #获取实际结果
