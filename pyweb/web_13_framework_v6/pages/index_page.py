#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

from selenium.webdriver.common.by import By

from common.base_page import BasePage


class IndexPage(BasePage):

    url = 'http://120.78.128.25:8765/'

    user_elem_locator = (By.XPATH, "//a[@href='/Member/index.html']")
    bid_elem_locator = (By.CLASS_NAME, "btn-special")


    def get_element_user(self):
        """获取用户"""
        return self.get_element(self.user_elem_locator)

    def get(self):
        """打开当前页面"""
        self.driver.get(self.url)

    def get_element_bid(self):
        """获取投标元素"""
        return self.get_element(self.bid_elem_locator)

