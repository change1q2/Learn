#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""

1, chromedriver 的版本问题。
如果出现版本不匹配，不支持，换一个chromedriver 的版本。

2，元素定位 8 大元素定位
6 种元素：
1， id
2,  name
3,  class_name
4,  link_text
5,  partial_link_text
6,  tagname（爬虫）

1, 只有 id 是唯一的。能用 id 就用 id
2, name ， 用户交互有关系。 input, select, textarea,
3, class_name 经常用来进行元素定位。坑：：：
4， link_text 只能用来定位连接

xpath xml 路径语言
css

xpath 定位：分为什么路径和什么路径？？

我想去查找一个元素：特征：不仅 class_name 要 == ？， 而且  name 要 == 多少

//标签名称[@class_name='值' and @name='name值' and @id='id值']

"""



