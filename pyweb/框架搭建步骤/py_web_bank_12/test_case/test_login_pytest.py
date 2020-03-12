#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import time
import unittest

import ddt
import pytest
from selenium import webdriver

from data.login_bank_data import (
    test_data_error_01,
    test_data_success,
    login_data_invalid

)

from pages.index_bank_page import IndexPage
from pages.login_bank_page import LoginPage


# @ddt.ddt
class TestLogin():

    @pytest.mark.error
    # @ddt.data(*test_data_error_01)
    @pytest.mark.parametrize("test_info",  test_data_error_01)
    def test_login_01_error(self,  test_info,  manage_browser):
        """手机号码为空"""
        driver, login_bank_page, index_bank_page = manage_browser
        # 第一个：获取实际结果（封装以后执行的函数或者方法） res = request.visit()
        login_bank_page.login(test_info['username'], test_info['pwd'])
        actual = login_bank_page.get_error_msg()
        # 第二个：获取预期结果 test_info【‘expected’】
        expected = test_info['expected']
        # 第三个：断言
        assert expected == actual


    def test_success(self):
        pass


if __name__ == '__main__':
    # 如果想使用 pytest 当中的参数化和 fixture
    pytest.main()
