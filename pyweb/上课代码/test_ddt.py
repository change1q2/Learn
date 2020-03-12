#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
ddt 是 unittest 当中的模块
参数化
"""
import unittest

import ddt
import pytest

def before_testcase():
    """前置条件"""
    print("前置条件")
    driver = "谷歌浏览器"
    return driver

def after_testcase():
    """后置条件"""
    print("后置条件")
    # 关闭浏览器，




test_data = [
    {"username": "yuze"},
    {"username": "xiaohong"},
    {"username": "doc"},
]

@pytest.mark.parametrize('test_info',  test_data)
# 第一个参数：是接收数据的变量名， 第二个参数是所有的测试数据
def test_ddt(test_info):
    # 前置条件执行
    driver = before_testcase()
    print(test_info)
    assert 1 == 1
    after_testcase()



#
# @ddt.ddt
# class TestDDT(unittest.TestCase):
#     @ddt.data(*test_data)
#     def test_ddt_2(self, test_info):
#         print(test_info)
#         assert 1 == 2




