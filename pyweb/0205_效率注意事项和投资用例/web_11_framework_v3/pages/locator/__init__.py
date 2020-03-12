#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""元素定位器，元素表达方式"""

class LoginLocator:
    """登录页面的元素定位方式"""
    mobile_element_locator = "//input[@name='phone']"
    pwd_element_locator = "//input[@name='password']"


class BidLocator:
    pass