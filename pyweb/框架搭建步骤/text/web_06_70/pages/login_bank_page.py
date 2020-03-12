'''
作者：seak
时间：
项目：
题目：
作用：
备注：

6.进一步优化，发现断言的地方信息不一定一样所以将断言提取出来重新封装一个函数get_error_msg
8.做数据分离，建立一个data文件将将测试数据都丢到里面去,并用locatoe来进行分层路劲处理
'''
import logging
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.constant import img_path
from selenium.webdriver import Chrome
from common.base_page import BasePage

#11.继承基业里面的类，就可以随便使用基业中的函数方法了
class LoginPage(BasePage):
    # locator 作为类属性管理
    """locator 分层的好处：
    当页面发生变化的时候，只需要检查固定位置的代码，
    便于管理。
    """
    login_bank_locator = (By.NAME,'username')
    pwd_bank_locator = (By.NAME,  'password')
    click_bank_locator  = (By.XPATH, '//*[@class="el-button btn-submit el-button--default el-button--medium is-plain"]/span')
    error_msg_locator = (By.XPATH, "//*[@class='el-form-item__error']")
    username_locator =(By.XPATH, "//input[@name='phone']")
    password_locator = (By.XPATH,"//input[@name='password']")
    invalid_msg_locator =(By.XPATH,'//*[@class="el-message__content"]')

    # driver, 浏览器对象 __init__,driver:Chrome 表示注释，driver对象是Chrome
    def __init__(self, driver:Chrome):
        self.driver = driver



    def login(self, username, pwd):
        # 3.输入网址
        url = 'http://inner.meeno.net:20684/dist2/'
        self.driver.get(url)

        # 4.定位元素
        # 用户名地址
        user_bank_element = self.driver.find_element(*self.login_bank_locator)
        # 密码地址
        pwd_bank_element = self.driver.find_element(*self.pwd_bank_locator)

        # 5.输入用户名和密码
        user_bank_element.send_keys(username)
        pwd_bank_element.send_keys(pwd)

        # 6.提交数据
        click_bank_element = self.driver.find_element(*self.click_bank_locator)
        click_bank_element.click()


        # # 7.断言
        # # 获取实际结果（登陆成功时这个就不适用了）
        # actual_msg = self.driver.find_element_by_xpath("//*[@class='el-form-item__error']")
        # return actual_msg.text

#6.进一步优化，发现断言的地方信息不一定一样所以将断言提取出来重新封装一个函数get_error_msg
    def get_error_msg(self):
        """获取错误提示"""
        error_msg = self.get_element(self.error_msg_locator)
        return error_msg.text

    # def get_invalid_msg(self):
    #     """获取没有通过授权的提示"""
    #     error_msg = self.driver.find_element(
    #         *self.invalid_msg_locator
    #     )
    #     return error_msg.text

   # 获取鉴权用显示等待
    def get_invalid_msg(self):
        error_msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.invalid_msg_locator)
        )
        return error_msg.text

    def get_element_username(self):
        """获取帐号输入的元素"""
        #11.使用基业继承以后可以直接使用基业里面的方法，就不需要每个需要捕获异常的地方进行异常捕获了直接调用方法就行
       # return self.driver.find_element(*self.username_locator)
        return self.get_element(self.username_locator)
    def get_element_pwd(self):
        """获取密码元素"""
        return self.get_element(self.password_locator)

    def clear_username(self):
        """清空手机号码"""
        return self.get_element_username().clear()


