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
from other.usestool import now_datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from config.constant import img_path


class BasePage:
    '''跟页面逻辑没有关系'''

    def __init__(self, driver):
        self.driver = driver

        # 显示等待的封装

    def wait_element_visible(self, locator, timeout=30, poll_frequency=0.5):
        '''显示等待，元素可见'''
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_element_precence(self, locator, timeout=30, poll_frequency=0.5):
        '''显示等待，元素出现'''
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout=30, poll_frequency=0.5):
        '''显示等待，元素可被点'''
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.element_to_be_clickable(locator))

    def get_element(self, locator):
        '''不需要显示等待'''
        try:
            return self.driver.find_element(*locator)
        except:
            # 截图保存,                                        #'写一个函数获取现在的时间戳'
            self.driver.save_screenshot(os.path.join(img_path, now_datetime()))
            logging.error("元素定位失败")

    #还有那些可以封装？
    #1.窗口切换，iframe,alert
    #2.鼠标拖拽
    def drag(self, src, target):
        '''鼠标拖拽'''
        ac = ActionChains(self.driver)
        ac.drag_and_drop(src,target)
        ac.perform()

    #js滚动到底部
    def scroll_to(self,width,height):
        '''窗口滚动'''

        js_code = 'window.scrollTo({},{})'
        self.driver.execute_script(js_code  )