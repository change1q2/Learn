#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

from selenium.webdriver.common.by import By

from common.base_page import BasePage


class UserPage(BasePage):
    money_locator = (By.CLASS_NAME, 'color_sub')

    def get_element_money(self):
        """定位余额元素"""
        return self.get_element(self.money_locator)

