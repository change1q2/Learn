'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import time
import unittest
import ddt
import pytest
from selenium import webdriver
from pages.login_bank_page import LoginPage
from pages.index_bank_page import IndexPage
from data.login_bank_data import (
    test_data_error_01,
    test_data_success,
    login_data_invalid

)



class TestNewUserCreat(unittest.TestCase):

    #前置条件将重复的逻辑都放在前置条件里面
    def setUp(self) -> None:
        # 1， 打开浏览器；
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(20)

        # 初始化要用到的页面
        self.login_bank_page = LoginPage(self.driver)
        self.index_bank_page = IndexPage(self.driver)

        #登陆
        login_bank_data = test_data_success[0]
        self.login_bank_page.login(login_bank_data['username'], login_bank_data['pwd'])


    #关闭游览器
    def tearDown(self) -> None:
        self.driver.quit()



    #新增用户成功
    def test_new_user_creat_success(self,test_info):
