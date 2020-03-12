#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import logging
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.constant import img_path


class BasePage:
    """basepage 当中跟具体的页面逻辑有关系吗？？"""

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visible(self, locator, timeout=30, poll_frequency=0.5):
        """等待元素可见"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_precence(self, locator, timeout=30, poll_frequency=0.5):
        """等待元素出现"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout=30, poll_frequency=0.5):
        """等待元素可被点"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.element_to_be_clickable(locator))

    def get_element(self, locator):
        """不需要显示等待"""
        try:
            return self.driver.find_element(*locator)
        except:
            # 截图保存
            self.driver.save_screenshot(os.path.join(img_path, 'screenshot2020_02_07_21_34_30.png'))
            logging.error("元素定位失败")

    # 还有哪些逻辑可以封装在 basepage 当中。
    #1， 窗口切换，iframe, alert 切换。
    # 鼠标拖拽
    def drag(self, src, target):
        """鼠标拖拽"""
        ac = ActionChains(self.driver)
        ac.drag_and_drop(src, target)
        ac.perform()

    # js 滚动到底部
    def scroll_to(self, width, height):
        """窗口滚动"""
        js_code = 'window.scrollTo({}, {})'.format(width, height)
        self.driver.execute_script(js_code)



