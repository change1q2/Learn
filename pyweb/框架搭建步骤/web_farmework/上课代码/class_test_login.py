'''
作者：seak
时间：
项目：
题目：
作用：
备注：登陆的方法
最开始的初版逻辑
'''
import ddt
import unittest
from selenium import webdriver

test_data = [
    {"mobile":"", "pwd": "", "expected": "请输入手机号"},
    {"mobile":"123", "pwd": "", "expected": "请输入正确的手机号"},
]

@ddt.ddt
class TestLogin(unittest.TestCase):

    #将前置条件:需要重复操作的都写在前置条件中
    def setUp(self) -> None:
     #1.打开游览器
        self.driver = webdriver.Chrome()
    #设置隐式等待
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        #关闭游览器，直接写driver的话在setUp中的driver传递不过来，所以加上一个self设置为实例属性进行传递

        #driver.quit(0)
        self.driver.quit()
    @ddt.data(*test_data)
    def test_login_no_mobile(self, test_info):
        '''手机号码为空'''
        #操作步骤
        '''
          #1.打开游览器(重复操作放到前置条件当中去)
        driver = webdriver.Chrome()
        #设置隐式等待
        driver.implicitly_wait(30)
        '''

        #2.输入登录网址
        url = 'http://120.78.128.25:8765/login'
        self.driver.get(url)
        #3定位元素
        mobile_element_locator =  "//input[@name='phone']"
        mobile_element = self.driver.find_element_by_xpath(mobile_element_locator)

        pwd_element_locator = "//input[@name='password']"
        pwd_element = self.driver.find_element_by_xpath( pwd_element_locator)

        #4.输入用户名和密码

        mobile_element.send_keys(test_info['mobile'])
        pwd_element.send_keys(test_info['pwd'])

        #提交数据
        pwd_element.submit()

        #断言
        actual_msg = self.driver.find_element_by_xpath("//div[@class='form-error-info']")
        self.assertEqual(test_info["expected"], actual_msg.text)

