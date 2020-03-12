'''
作者：seak
时间：
项目：
题目：
作用：
备注：删除银行课程
'''

#这个方法是得不到某个元素就等待一段时间，直到拿到某个元素位置。
import driver
from Tools.scripts.serve import app
from selenium import webdriver
import time
#初始化游览器
browser = webdriver.Chrome()

#进入被测地址
url = browser.get("http://inner.meeno.net:20684/dist/#/login?redirect=%2F")
#为浏览器对象创建一个等待时间，这个方法是得不到某个元素就等待一段时间


#元素定位
username = browser.find_element_by_name("username").send_keys('pzhbank3')
password = browser.find_element_by_name("password").send_keys("123456")
#点击登陆
click_login = browser.find_element_by_xpath("//button/span").click()
time.sleep(5)
click_class = browser.find_element_by_xpath("//div/div/div/div[1]/ul/div[4]/div/a/li/div/span").click()

#调整大小
browser.maximize_window()

#browser.quit()

