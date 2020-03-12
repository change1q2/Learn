#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import time
import unittest

from selenium import webdriver

from data.login_data import login_data_success
from pages.index_page import IndexPage
from pages.login_page import LoginPage


class TestBid(unittest.TestCase):

    def setUp(self) -> None:
        """
        前置条件：
        1， 登录
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

        # 初始化页面
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

        # 登录
        login_data = login_data_success[0]
        self.login_page.login(login_data['mobile'], login_data['pwd'])



    def tearDown(self) -> None:
        pass

    def test_bid_error(self):
        "测试投资失败"
        time.sleep(1)
        self.index_page.get()

        # 如果不等待新页面出现而直接定位元素，可能找到的是上一个页面当中的元素。
        self.index_page.get_element_bid().click()
        print('hello')


    # def test_bid_success(self):
    #     """投资成功"""
    #     pass


