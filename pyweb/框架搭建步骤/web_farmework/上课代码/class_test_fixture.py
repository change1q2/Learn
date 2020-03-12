#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

driver = None

from selenium import webdriver

def before_testcase():
    """前置条件"""
    global driver
    driver = webdriver.Chrome()
    return driver

def after_testcase():
    """后置条件"""
    global driver
    driver.quit()
    print("后置条件")

    # 关闭浏览器，

def test_baidu():
    driver = before_testcase()
    driver.get("http://www.baidu.com")
    after_testcase()





