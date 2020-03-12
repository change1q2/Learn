'''
作者：seak
时间：
项目：
题目：
作用：
备注：首页
根据PO模式的思想，每一个页面单独建立一个类
'''
from selenium.webdriver.common.by import By
from common.base_page import BasePage

class IndexPage(BasePage):
    url = 'http://120.78.128.25:8765/Index/index.html'
    bid_elem_locator = (By.CLASS_NAME, "btn-special")
    user_elem_locator = (By.XPATH,"//a[@href='/Member/index.html']")

    # def __init__(self, driver):
    #     self.driver = driver

    def get_element_user(self):
        '''获取用户名'''
        #return self.driver.find_element_by_xpath(*self.user_elem_locator)

        return self.get_element(self.user_elem_locator)

    def get(self):
        '''打开当前页面'''
        self.driver.get(self.url)

    def get_element_bid(self):
        '''获取投标元素'''
     #   return self.driver.find_element(*self.bid_elem_locator)

        return self.get_element(self.bid_elem_locator)
