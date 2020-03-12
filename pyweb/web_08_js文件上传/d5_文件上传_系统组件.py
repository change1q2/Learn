#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
文件上传：
input 元素， 如果我想去上传文件
# elenent = find....()
# element.send_keys(r"d:\cases.xlsx")


如果不是 input 元素：通过 js 去调用组件：

接口测试：测试后端  services

UI 测试: web, app, 桌面软件，

"""

import time
import pyautogui as ui

from selenium import  webdriver

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(20)

driver.get("file:///C:/data/jianguoyun/projects/python24/web_08_js文件上传/demo.html")

file_elem = driver.find_element_by_name('mfile')
file_elem.click()

# 系统之间要等待
time.sleep(1)

# 写入文件
ui.write(r"d:\cases.xlsx")
# 输入回车
time.sleep(0.5)
ui.press('enter', presses=2)

time.sleep(2)





