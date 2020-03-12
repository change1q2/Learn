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

# 放大窗口
# 强制等待
time.sleep(2)
browser.maximize_window()

#  缩小窗口
time.sleep(2)
browser.minimize_window()

# 设置窗口的大小, 长，宽，做为参数传递进去：单位，像素
time.sleep(2)
browser.set_window_size(800, 600)



# UI: 用户界面
# web 是一种 ui
# app
# 桌面应用，GUI ,

#
time.sleep(2)
browser.get("http://www.douban.com")

# 后退， back
time.sleep(2)
browser.back()

# 前进， forward
time.sleep(2)
browser.forward()

# 刷新，
time.sleep(2)
browser.refresh()

# 关闭浏览器
browser.quit()

# 关闭标签页
# browser.close()



