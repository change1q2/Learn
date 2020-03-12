'''
作者：seak
时间：
项目：
题目：
作用：
备注：出路文件路径
'''

import os

#获取项目路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(root_path)

#img路径
img_path = os.path.join(root_path,'img')
print(img_path)
#如果路径不存在就先创建一个
# if os.path.exists(img_path):
#     os.mkdir(img_path)
