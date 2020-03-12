#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
1, 下载 webdriver, 放到。。。 python 根目录
2， 导入 selenium

browser = webdriver.Chrome(executable_path=)
executable_path 是 webdriver.exe 的可执行路径。
1， 如果放到了python 根目录，自动到环境变量当中查找
2， 如果不放到环境变量，自己根据关键字参数配置

浏览器操作：


"""

import time

from selenium import webdriver

# 初始化浏览器
# browser = webdriver.Chrome(executable_path=r'‪D:\chromedriver\chromedriver_79.exe')
browser = webdriver.Chrome()
# 进入被测网址
browser.get('http://www.baidu.com')

# 获取网页的 URL 地址
print(browser.current_url)

# 获取网页的标题
print(browser.title)

# 获取网页的源代码
print(browser.page_source)

# window_handlers  获取所有的窗口，所有的标签页
print(browser.window_handles)

# 获取现在正处于的标签页, window_handler , 窗口句柄。 ===》 窗口的 ID
print(browser.current_window_handle)


