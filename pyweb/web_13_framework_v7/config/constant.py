#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import os

# 项目路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# img 路径
img_path = os.path.join(root_path, 'img')
# 如果路径不存在，创建一个
if os.path.exists(img_path):
    os.mkdir(img_path)

