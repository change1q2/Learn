#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
pytest 存储测试夹具  fixture 的专用模块。

conftest.py 文件存放的位置


"""
import pytest
from selenium import webdriver

from pages.index_bank_page import IndexPage
from pages.login_bank_page import LoginPage
from selenium.webdriver import ChromeOptions

@pytest.fixture()
def manage_browser():
    # 浏览器二进制路径配置
    options = ChromeOptions()
    options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    # 初始化浏览器
    driver = webdriver.Chrome(options=options)
    # 设置隐式等待
    driver.implicitly_wait(20)
    login_bank_page = LoginPage(driver)
    index_bank_page = IndexPage(driver)

    yield driver, login_bank_page, index_bank_page
    driver.quit()


@pytest.fixture()
def login(test_info):
    """登录的夹具"""
    driver = webdriver.Chrome()
    login_bank_page = LoginPage(driver)
    index_bank_page = IndexPage(driver)

    # 登陆的逻辑
    login_bank_page.login(test_info['username'], test_info['pwd'])

    yield driver, login_bank_page, index_bank_page
    driver.quit()
    # 登录
