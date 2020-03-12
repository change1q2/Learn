#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
强制等待：
1， 不灵活
2， 如果等待时间不足，程序会报错；
3， 如果等待时间过长，自动化测试的效率非常低。

智能等待：
什么时候加载完成，就等到什么时候

隐式等待
当初始化一个浏览器之后，养成加隐式等待的习惯。
监控器，设置一次就可以了

隐式等待只能用来等待元素出现，查找元素
alert

显示等待：（难点）

"""


import time

from selenium import webdriver

driver = webdriver.Chrome()

# 设置隐式等待的时间,
# 最大等待时间是 30 s ， 如果超过 30s, 元素还没有加载出来，报错，程序无法执行。
# 设置隐式等待超时时间，课可以稍微长一点。
# 如果元素在 2s 的时候， 已经加载出来了，就不会继续等待了，等待 2 s 就结束了。
# n 次 7 s 的时候，7
# time.sleep(2)

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")


elem = driver.find_element_by_id('kw')


other_elem = driver.find_element_by_name("s...")




