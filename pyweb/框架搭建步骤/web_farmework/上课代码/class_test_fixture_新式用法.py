#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pytest
from selenium import webdriver

@pytest.fixture()
def manage_browser():
    # 前置条件
    print("前置条件")
    driver = webdriver.Chrome()

    yield driver
    # 生成器概念

    # 后置条件
    # driver.quit()
    print("后置条件")



def test_baidu(manage_browser):
    browser = manage_browser
    browser.get("http://www.baidu.com")

