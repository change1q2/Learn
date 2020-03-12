#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
# xpath: 先到浏览器当中去确认xpath 表达式是否正确

# 如何去表示xpath:
1, //input[@class='' and ...]
2, //input[contains(@class, 'class_value')   and    @id='id value']

关系：
1， . 或者 ..
2,  /  或者 //  只能从父级元素到子元素
3， 轴运算，    ...//parent::div

概念：
不知道是什么元素：
通配符：：     * 号

元素的构成：
- tagnamee
- 属性
- text()=
- 子元素（关系）

text 文本在 web 自动化测试当中，不是元素属性，
不能使用 @符号去表示。

//a[contains(text(), '新')]

在web 自动化测试当中，使用 selenium 有没有通过 text 文本进行定位的方式？？  1，xpath
在web 自动化测试当中，使用 selenium 有没有直接通过 text 文本进行定位的方式？？
selenium 有没有直接封装 text 定位方式？

：
//a[contains(text(), '新')][1]
xpath 索引是从 1 开始的，不是从 0 开始的。

TODO: 一般来说，我们不会去使用 索引进行元素定位

not a and b or (c in d)

索引的优先级非常高，手工提升其他部分的优先级，最后才使用索引。
(//a[contains(text(), '新')])[1]
table, ul, ol <li>

# 组合上下级的关系 / 表示：父子关系
//form[@name='f']/span[@id='s_kw_wrap']

# // 表示：祖先和子孙关系
//form[@name='f']//span[@id='s_kw_wrap']
# 轴运算


xpath 元素定位：
1， 什么时候使用 xpath:
没有明显特征的元素: id, name, class_name
name, class_name, 能找到多个元素

2， 先到浏览器当中去验证 xpath 表达式。
检查表达式是否正确，
2， 是否唯一。

xpath:
1, 喜欢直接 copy 浏览器当中的 xpath, 杜绝使用。
2， xpath 的插件， 当你们熟练使用在工作当中，为了提升效率，可以使用 chropath 插件。
在学习阶段，不要去用。

面试：xpath, 必考。


css 选择器：
组合条件
input 的元素 并且 id = kw
input#kw  # 表示 id
input.s_ipt  . 表示 class

通用的表示属性的方式：
input[id='kw']

面试题： css 和 xpath 的区别：优劣势：什么时候 css, 什么时候 xpath
1，css 更加简洁
2， xpath 的功能更强大。  对于简单的元素定位，css, 复杂的元素，xpath.
3. xpath 可以使用 text 文本定位， css 不行。
4. 效率。通常来说，xpath 的解析效率会低。css 要快一些。。 IE






"""

# bg s_ipt_wr quickdelete-wrap

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 通过 class_name 定位元素
# TODO: 中间不能有空格
# 只能提取其中的某一个值，

# TODO: 但是如果是 xpath 表达式，class='' 可以有空格


# e = driver.find_element_by_class_name('s_ipt_wr')
# print(e)

# s_kw_wrap

e = driver.find_element_by_xpath("//span[@id='s_kw_wrap' and @class='s_ipt_wr']")

# xpath的函数： //span[contains(@class, 's_ipt_wr')]
# 定位百度首页当中包含新这个字的 a 标签
# partial link text
# xpath


e = driver.find_element_by_id()

e = driver.find_element_by_name()

# time.sleep()
# 强制等待
# 智能等待：隐式等待，和显示等待
# 自定义等待: 自己封装。


