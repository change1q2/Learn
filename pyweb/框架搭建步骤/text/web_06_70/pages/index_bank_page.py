'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import logging
import os

from selenium.webdriver.common.by import By
from config.constant import img_path
from other.time import now_datetime_time
from common.base_page import BasePage
class IndexPage(BasePage):
    # locator 作为类属性管理
    """locator 分层的好处：
    当页面发生变化的时候，只需要检查固定位置的代码，
    便于管理。
    """

    index_bank_locator = (By.XPATH, "//*[@class='type-title']/span")
    url = 'http://inner.meeno.net:20684/dist2/#/homepage/interStatistic'


    def get_element_user(self):
        """获取运营数据"""
        return self.get_element(self.index_bank_locator)

    def get(self):
        """打开当前页面"""
        self.driver.get(self.url)