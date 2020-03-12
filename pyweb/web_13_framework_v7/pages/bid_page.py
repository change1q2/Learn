#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class BidPage(BasePage):

    # 投标输入框
    bid_input_locator = (By.CLASS_NAME, 'form-control')
    # 投标金额不是 10 的整数倍错误提示
    bid_btn_locator = (By.CLASS_NAME, 'btn-special')
    # 投标成功弹框
    bid_success_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[contains(@class, 'capital_font1')]")
    # 激活按钮
    bid_activee_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")

    def get_element_bid_input(self):
        """定位投标输入框元素"""
        return self.get_element(self.bid_input_locator)

    def get_element_bid_btn(self):
        """获取投标按钮"""
        return self.get_element(self.bid_btn_locator)

    def get_success_msg(self):
        """定位投资成功弹框"""
        return self.get_element(self.bid_success_locator)

    def get_active_btn(self):
        """定位投资成功激活按钮"""
        return self.get_element(self.bid_activee_locator)