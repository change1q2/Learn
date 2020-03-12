#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


"""
测试数据管理模块

测试数据分组的依据：
测试，页面逻辑不一样
"""

login_data_error = [
    {"mobile":"", "pwd": "", "expected": "请输入手机号"},
    {"mobile":"123", "pwd": "", "expected": "请输入正确的手机号"},
]


login_data_invalid = [
    {"mobile":"15746732896", "pwd": "123", "expected": "此账号没有经过授权，请联系管理员!"},
]


login_data_success = [
    {"mobile":"18684720553", "pwd": "python", "expected": "我的帐户[python]"},
]