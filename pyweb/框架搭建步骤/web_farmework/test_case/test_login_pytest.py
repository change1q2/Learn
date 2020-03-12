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

from data.login_data import (
    login_data_error,
    login_data_success,
    login_data_invalid
)

from pages.index_page import IndexPage
from pages.login_page import LoginPage


# @ddt.ddt
class TestLogin():

    @pytest.mark.error
    # @ddt.data(*login_data_error)
    @pytest.mark.parametrize("test_info", login_data_error)
    def test_login_01_error(self,  test_info,  manage_browser):
        """手机号码为空"""
        driver, login_page, index_page = manage_browser
        # 第一个：获取实际结果（封装以后执行的函数或者方法） res = request.visit()
        login_page.login(test_info['mobile'], test_info['pwd'])
        actual = login_page.get_error_msg()
        # 第二个：获取预期结果 test_info【‘expected’】
        expected = test_info['expected']
        # 第三个：断言
        assert expected == actual


    def test_success(self):
        pass


if __name__ == '__main__':
    # 如果想使用 pytest 当中的参数化和 fixture
    pytest.main()
