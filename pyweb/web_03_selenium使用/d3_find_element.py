#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
自动化测试是模拟手工：
1， 打开浏览器
2， 打开网站
3， python ， 他们去点点点的时候：是根据 HTML 元素

元素定位：在 HTML 当中去找到需要操作的元素（标签）

python 如何查找元素： 根据特征，
1，id 的唯一性非常明显




find_element_by...:
1, 如果找到多个元素，那么只会返回找到的第一个。 WebElement//*[@id="u"]

find_elements_by_...:
2, 一次性找到多个。
3， 不管找到多个少个，都会返回 list
列表当中的每一个成员就是一个 WebElement


ID 查找到的元素是唯一的：
坑： ID 可能是动态变化的。
什么时候通过ID 确定定位？什么时候不能
1，如果 ID 中包含数字，
2，包含一些不规则的字母或者数字。

简单的字母， jint,  yuz, 一般就不会变动。


"""
import time

from selenium import webdriver

# 初始化浏览器
# browser = webdriver.Chrome(executable_path=r'‪D:\chromedriver\chromedriver_79.exe')
browser = webdriver.Chrome()
# 进入被测网址
browser.get('http://www.baidu.com')

# 元素定位，
# 1， ID, 查找到的元素是一个 WebElement 对象，
# 如果没有找到，报错：NoSuchElementException
# input_element = browser.find_element_by_id('kw')
# print(input_element)
#
# # 如果输入内容，输入： send_keys()
# input_element.send_keys('柠檬班')
# time.sleep(3)


# 2, 通过 name 属性
# elem = browser.find_element_by_name('wd')
# elem.send_keys("lemonban")
# time.sleep(3)
#
# # 3, 通过 class
# browser.find_element_by_class_name()
#
# # 4, 通过 tagname, 标签名称。查找到的元素不具备唯一性
# browser.find_element_by_tag_name()

# 5, 专门用来定位 a 标签，连接， link_text
# e = browser.find_element_by_link_text('新闻')
# e.click()
# time.sleep(3)
#
# # 6, partial_link_text
# e = browser.find_element_by_partial_link_text('新')

# 7, xpath

# 8， css 选择器

# find_elements 得到的是一个列表。 list
e = browser.find_elements_by_id('kw')
print(e)