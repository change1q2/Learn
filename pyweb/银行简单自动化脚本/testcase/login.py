'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

import time


from selenium import webdriver
#初始化游览器
driver= webdriver.Chrome()

#获取游览器地址
get_url = driver.get('http://inner.meeno.net:20684/dist/')
time.sleep(2)

#使用xpath获取输入账号窗口
#输入账号
username = driver.find_element_by_xpath('//input[@placeholder="请输入账号"]')
username.send_keys('pzhbank')
#输入密码
password = driver.find_element_by_xpath("//input[@name='password']")
password.send_keys('123456')

#找到登录按钮点击
login = driver.find_element_by_xpath()