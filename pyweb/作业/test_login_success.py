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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def test_login_success(self):
        #1.打开游览器
        driver = webdriver.Chrome()

        #2.设置隐式等待
        driver.implicitly_wait(30)

        #3.输入网址
        url = 'http://inner.meeno.net:20684/dist2/'
        driver.get(url)

        #4.定位元素
        #用户名地址
        login_bank_locator = 'username'
        user_bank_element = driver.find_element_by_name(login_bank_locator)
        #密码地址
        pwd_bank_locator ='password'
        pwd_bank_element = driver.find_element_by_name(pwd_bank_locator)

        # 5.输入用户名和密码
        user_bank_element.send_keys('pzhbank')
        pwd_bank_element.send_keys('123456')

        #6.提交数据
        click_bank_locator = '//*[@class="el-button btn-submit el-button--default el-button--medium is-plain"]/span'
        click_bank_element = driver.find_element_by_xpath(click_bank_locator)
        click_bank_element.click()

        # 因为跳转页面了加一个显示等待
        wait = WebDriverWait(driver, 30, 0.2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='type-title']/span")))

        print('显示等待：', wait)

        time.sleep(3)
        #8.断言
        #实际结果
        actual_msg = driver.find_element_by_xpath("//*[@class='type-title']/span")
        print("实际结果：",actual_msg.text)

        #预期结果
        self.assertIn('运营数据',actual_msg.text)

        #关闭游览器
        driver.quit()
