#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
1, 打开浏览器
2，输入被测网址
3，点点

selenium
1, 安装 pip install selenium
2, 安装浏览器驱动
1） 使用什么浏览器，就安装什么驱动。chrome, chromedriver.
2)  版本匹配，81版本，下载对应 81 版本的驱动

下载地址：https://npm.taobao.org/
下载下来：放到 python 根目录下面， 便于查找驱动


TODO: 面试题： selenium 进行自动化测试的流程和原理（图）
"""

from selenium import webdriver

# 初始化浏览器
browser = webdriver.Chrome()

