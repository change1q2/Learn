#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
鼠标操作：
- element.click()

全局：
- 双击
- 右击
- 移动悬停
- 鼠标拖拽

"""


from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

# 第一步：初始化 actionchains
action = ActionChains(driver)
# 第二部：定位要操作的元素
element = driver.find_element_by_id('...')
# 执行对应的操作,右击
action.context_click(element)
# 执行完操作以后，加 释放动作
action.perform()