#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# element

def set_attribute():
    """发送js代码"""
    pass

driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

input_elem = driver.find_element_by_id('kw')

# 获取属性
print(input_elem.get_attribute('name'))

# set_attribute
