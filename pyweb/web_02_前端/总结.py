#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
1, 打开浏览器
2，输入被测网址
3，点点


HTML 和页面内容有什么关系呢？？？
HTML 的源码内容是和页面内容对应的。


认识 HTML: HyperText Markup Language，
全称：超文本标记性语言。

标记性语言：
- HTML
- markdown
- XML (微信)， 安卓app


标签：是用来在 html 当中打标记的单位。
分为很多种类：
- 表示连接的标签
- 表示图片的标签
- 表示输入框的标签

标签的表示方式：（一般来说是成对出现，标签对）
<标签名> 内容 </标签名>
<a>新闻</a>

<标签名 属性名="属性值" 属性名2="属性值2" > 内容 </标签名>
<a href='' class=''>新闻</a>

标签的具体组成部分：
- 标签名称
- 标签属性
- 文本内容
- 下属标签

标签：对应的是一种类型的展示形式
属性：既可以丰富特征，又可以改变标签的展示方式。

a 标签一般是和 href 属性绑定起来使用的。

img 标签通常和 src 属性组合起来使用

iframe：在一个网页网页当中嵌套子网页

input 元素：一定要带 name 属性，
radio， checkbox 要带 value 属性。

select 元素内容： 只能是 option 元素


"""
import requests
from selenium import webdriver




