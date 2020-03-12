'''
作者：seak
时间：
项目：
题目：
作用：
备注：银行登陆
'''
import time
import unittest
import ddt
import pytest
from selenium import webdriver
from pages.login_bank_page import LoginPage
from pages.index_bank_page import IndexPage
from data.login_bank_data import (
    test_data_error_01,
    test_data_success,
    login_data_invalid

)


@ddt.ddt
class TestLogin(unittest.TestCase):

    #前置条件将重复的逻辑都放在前置条件里面
    def setUp(self) -> None:
        # 1， 打开浏览器；
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(20)

        # 初始化要用到的页面
        self.login_bank_page = LoginPage(self.driver)
        self.index_bank_page = IndexPage(self.driver)


    #关闭游览器
    def tearDown(self) -> None:
        self.driver.quit()



    # #没有授权的登录
    # # 获取没有通过授权
    @pytest.mark.failed
    @ddt.data(*login_data_invalid)
    def test_login_02_invalid(self, test_info):
        # 登录
        self.login_bank_page.login(test_info['username'], test_info['pwd'])
        time.sleep(2)
        # 获取没有通过授权的实际结果
        actual = self.login_bank_page.get_invalid_msg()
        expected = test_info['expected']
        self.assertEqual(expected, actual)




    # # 讲登录成功
    # @pytest.mark.success
    # @ddt.data(*test_data_success)
    # def test_login_success(self,test_info):
    #     """登录成功"""
    #     # 执行登录操作， login_page.login()
    #     self.login_bank_page.login(test_info['username'], test_info['pwd'])
    #     # 进入了？？页面  我的帐户[python]
    #
    #     # 定位我的账户
    #     #self.index_bank_page.get()#如果遇到登陆报404错误可以使用这个代码手动进入当前页面
    #     time.sleep(3)
    #     #实际结果
    #     actual = self.index_bank_page.get_element_user()
    #
    #     # 预期结果
    #     expected = test_info['expected']
    #
    #     #断言，用asserIn可以只断言包含这里面的某个字就行
    #     self.assertIn(expected ,  actual.text)








"""
# 我们把页面操作的逻辑从测试代码当中提取出来。  函数封装的好处：
# 1， 实现了测试代码和页面代码的分离，维护更加方便。
    --- 一，当页面发生变化的时候，测试代码不需要修改；
    --- 二，测试需求发生变化的时候，页面代码不需要修改；
# 2， 维护成本低；
# 3， 提高代码的复用性。
  1， 逻辑一样的时候，可以重复使用同样的函数调用。
###                    2, 不同的测试逻辑（测试不同的模块的时候，如果重复用到了同样的步骤）
只需要去调用相关的函数就可以了。
# 4 ，可读性更强。

"""
