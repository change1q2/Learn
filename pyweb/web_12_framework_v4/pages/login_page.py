#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""登录页面的操作"""

from selenium.webdriver.common.by import By

from common.base_page import BasePage

"""封装函数的作用：
1， 节省代码
2， 更加具有可读性


POM:  PO 模式
PageObject
页面的逻辑全部都放到一个对象当中

作用好处：
# 我们把页面操作的逻辑从测试代码当中提取出来。  函数封装的好处：
# 1， 实现了测试代码和页面代码的分离，维护更加方便。
    --- 一，当页面发生变化的时候，测试代码不需要修改；
    --- 二，测试需求发生变化的时候，页面代码不需要修改；
# 2， 维护成本低；
# 3， 提高代码的复用性。
  1， 逻辑一样的时候，可以重复使用同样的函数调用。
###                    2, 不同的测试逻辑（测试不同的模块的时候，如果重复用到了同样的步骤）
只需要去调用相关的函数就可以了。
# 4 ，可读性更强。

"""
# Page Object


class LoginPage(BasePage):
    # driver, 浏览器对象 __init__
    # locator 作为类属性管理
    """locator 分层的好处：
    当页面发生变化的时候，只需要检查固定位置的代码，
    便于管理。
    """
    mobile_element_locator = (By.XPATH, "//input[@name='phone']")
    pwd_element_locator = (By.XPATH, "//input[@name='password']")
    error_msg_locator = (By.XPATH, "//div[@class='form-error-info']")
    invalid_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']")

    # css

    # 显示等待（locator, (By.XPATH, '//input...')）

    # class

    # name

    def login(self, mobile, pwd):
        """登录"""
        url = 'http://120.78.128.25:8765/login'
        # 2， 输入登录网址，
        self.driver.get(url)
        # 3，定位元素，
        # mobile_element_locator = "//input[@name='phone']"
        mobile_element = self.driver.find_element(*self.mobile_element_locator)

        # pwd_element_locator = "//input[@name='password']"
        pwd_element = self.driver.find_element(*self.pwd_element_locator)
        # 4，输入用户名和密码
        mobile_element.send_keys(mobile)
        pwd_element.send_keys(pwd)

        # 提交数据
        pwd_element.submit()

    def get_error_msg(self):
        """获取错误提示"""
        error_msg = self.driver.find_element(
            *self.error_msg_locator
        )
        return error_msg.text

    # def get_error_msg(self):
    #     error_msg = WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(self.error_msg_locator)
    #     )
    #     return error_msg.text


    def get_invalid_msg(self):
        """获取没有通过授权的提示"""
        error_msg = self.get_element(
            self.invalid_msg_locator
        )
        return error_msg.text

    def get_element_mobile(self):
        """获取手机号码输入的元素"""
        return self.get_element(self.mobile_element_locator)

    def get_element_pwd(self):
        """获取密码元素"""
        return self.get_element(self.pwd_element_locator)

    def clear_mobile(self):
        """清空手机号码"""
        return self.get_element_mobile().clear()


