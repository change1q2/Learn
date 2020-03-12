#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

class IndexPage:

    url = 'http://120.78.128.25:8765/Index/index'

    def __init__(self, driver):
        self.driver = driver

    def get_element_user(self):
        """获取用户"""
        return self.driver.find_element_by_xpath("//a[@href='/Member/index.html']")

    def get(self):
        """打开当前页面"""
        self.driver.get(self.url)

