#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import unittest
import ddt
from selenium import webdriver
from pages.login_page import LoginPage
from pages.index_page import IndexPage


test_data = [
    {"mobile":"", "pwd": "", "expected": "请输入手机号"},
    {"mobile":"123", "pwd": "", "expected": "请输入正确的手机号"},
]




@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 1， 打开浏览器；
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(20)

        # 初始化要用到的页面
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    # @ddt.data(*test_data)
    # def test_login_error(self,  test_info):
    #     """手机号码为空"""
    #     # 第一个：获取实际结果（封装以后执行的函数或者方法） res = request.visit()
    #     self.login_page.login(test_info['mobile'], test_info['pwd'])
    #     actual = self.login_page.get_error_msg()
    #     # 第二个：获取预期结果 test_info【‘expected’】
    #     expected = test_info['expected']
    #     # 第三个：断言
    #     self.assertEqual(expected, actual)

    # 讲登录成功
    def test_login_success(self):
        """登录成功"""
        # 执行登录操作， login_page.login()
        self.login_page.login("18684720553", 'python')
        # 进入了？？页面  我的帐户[python]
        # 定位我的账户

        self.index_page.get()
        actual = self.index_page.get_element_user()
        print("打印实际结果：",actual)

        # 预期结果
        expected = '我的帐户[python]'
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

"""