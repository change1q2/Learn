 #!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import time
import unittest

import ddt
from selenium import webdriver

from data.login_data import (
    login_data_error,
    login_data_success,
    login_data_invalid
)

from pages.index_page import IndexPage
from pages.login_page import LoginPage



@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """打开浏览器，"""
        cls.driver = webdriver.Chrome()
        # 设置隐式等待
        cls.driver.implicitly_wait(20)
        # 初始化要用到的页面
        cls.login_page = LoginPage(cls.driver)
        cls.index_page = IndexPage(cls.driver)

        cls.driver.get("http://120.78.128.25:8765/login")

    @classmethod
    def tearDownClass(cls) -> None:
        """关闭浏览器"""
        cls.driver.quit()

    def setUp(self) -> None:
        # 1， 打开浏览器；
        self.login_page.get_element_mobile().clear()
        self.login_page.get_element_pwd().clear()

    def tearDown(self) -> None:
        pass

    @ddt.data(*login_data_error)
    def test_login_01_error(self,  test_info):
        """手机号码为空"""

        # 第一个：获取实际结果（封装以后执行的函数或者方法） res = request.visit()
        self.login_page.login(test_info['mobile'], test_info['pwd'])
        actual = self.login_page.get_error_msg()
        # 第二个：获取预期结果 test_info【‘expected’】
        expected = test_info['expected']
        # 第三个：断言
        self.assertEqual(expected, actual)

    # @ddt.data(*login_data_invalid)
    # def test_login_02_invalid(self, test_info):
    #     # 登录
    #     self.login_page.login(test_info['mobile'], test_info['pwd'])
    #     # 获取没有通过授权的实际结果
    #     actual = self.login_page.get_invalid_msg()
    #     expected = test_info['expected']
    #     self.assertEqual(expected, actual)

    # 讲登录成功
    @ddt.data(*login_data_success)
    def test_login_03_success(self, test_info):
        """登录成功"""
        # 执行登录操作， login_page.login()
        self.login_page.login(test_info['mobile'], test_info['pwd'])
        # 进入了？？页面  我的帐户[python]
        # 定位我的账户

        # 等待窗口被打开
        time.sleep(1)
        self.index_page.get()
        actual = self.index_page.get_element_user()

        # 预期结果
        expected = test_info['expected']
        self.assertIn(expected ,  actual.text)

        # 获取实际结果。



    # def


# PO模式  POM
# 英文全称： Page Object Model
# 讲 UI 当中的 页面封装成 对象

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


提升测试效率：
1，

"""
