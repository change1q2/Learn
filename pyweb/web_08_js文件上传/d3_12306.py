#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
使用 js 的主要场景：
1， 修改网页内容
2， selenium 并没有提供的对应的浏览器或者网页元素操作的方法。

"""

import time

from selenium import  webdriver

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(20)

driver.get("https://www.12306.cn/index/")

# 查找到修改的元素
date_element = driver.find_element_by_id('train_date')

# 发送 js 指令
js_code = 'arguments[0].readOnly = false;'
# python 字符串格式化 "{1} helloword {0} {2}".format(date_element, v1, v2,)

driver.execute_script(js_code, date_element )

# 系统和系统之间的交互，python 和 js 的交互
time.sleep(0.2)
# 第二不： 修改 value 属性
js_code = 'arguments[0].value = "2020-01-23";'
driver.execute_script(js_code, date_element )



