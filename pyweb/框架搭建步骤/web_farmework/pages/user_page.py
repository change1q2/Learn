'''
作者：seak
时间：
项目：
题目：
作用：
备注：用户界面
'''
from selenium.webdriver.common.by import By
from common.base_page import BasePage

class UserPage(BasePage):
    money_locator = (By.CLASS_NAME,'color_sub')


    # def __init__(self,driver):
    #     self.driver = driver



    def get_element_money(self):
        '''定位余额元素'''
     #   return self.driver.find_element(*self.money_locator)
        return self.get_element(self.money_locator)
