'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import logging

from selenium.webdriver.common.by import By


class IndexPage:
    # locator 作为类属性管理
    """locator 分层的好处：
    当页面发生变化的时候，只需要检查固定位置的代码，
    便于管理。
    """

    index_bank_locator = (By.XPATH, "//*[@class='type-title']/span")
    url = 'http://inner.meeno.net:20684/dist2/#/homepage/interStatistic'

    def __init__(self, driver):
        self.driver = driver
    # 10.
    # 加入日志进行日志捕获,
    # （1）对可能获取不到元素的地方加入异常捕获, 所有元素获取的地方都要加（例如在index_bank_page中）
    def get_element_user(self):
        """获取运营数据"""
        try:
            return self.driver.find_element(*self.index_bank_locator)
        except:
            logging.error()
    def get(self):
        """打开当前页面"""
        self.driver.get(self.url)