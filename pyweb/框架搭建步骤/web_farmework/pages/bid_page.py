'''
作者：seak
时间：
项目：
题目：
作用：
备注：投标的页面
'''
from selenium.webdriver.common.by import By
from common.base_page import BasePage

#继承以后可以不需要__init__方法了
class BidPage(BasePage):

    #投标输入框
    bid_input_locator = (By.CLASS_NAME,'form-control')

    #投标金额是10的整数倍
    bid_btn_locator = (By.CLASS_NAME,'bin-special')
    # 投标金额不是10的整数倍错误提示
    bid_error_locator = (By.CLASS_NAME, 'bin-special')

    #投标成功弹窗
    bid_success_locator = (By.XPATH,"//div[@class='layui-layer-content']//div[@class='capital_font1 note']")

    #激活按钮
    bid_active_locator = (By.XPATH,"//div[@class='layui-layer-content']//button")

    # def __init__(self,driver):
    #     self.driver = driver

    def get_element_bid_input(self):
        '''定位投标输入元素'''
      #  return self.driver.find_element(*self.bid_input_locator)

    #继承以后可以使用如下方法
        return self.get_element(self.bid_input_locator)

    def get_element_error_msg(self):
        #return self.driver.find_element(*self.bid_error_locator)

        return self.get_element(self.bid_error_locator)

    def get_element_bid_btn_msg(self):
        '''获取投标按钮'''
       # return self.driver.find_element(*self.bid_btn_locator)
        return self.get_element(self.bid_btn_locator)

    def get_success_msg(self):
        '''定位投标成功弹窗'''
       # return self.driver.find_element(*self.bid_success_locator)
        return self.get_element(self.bid_success_locator)

    def get_bid_active_locator(self):
        '''定位投资成功激活按钮'''
       # return self.driver.find_element(*self.bid_active_locator)
        return self.get_element(self.bid_active_locator)