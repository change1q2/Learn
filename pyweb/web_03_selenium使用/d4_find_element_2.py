"""
5 中元素定位方式存在的问题：
元素定位不精确。可能出现多个


解决的思路：
1， 你找到多个，find_elements 找到多个，通过 索引值去确定是哪一个。

2,  不仅 tagname 叫 a, 而且 name = 。。。 而且 class_name
组合条件的方式进行范围的缩小。
1， xpath
2,  css


xpath:
1, 绝对路径： /html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input
2， 相对路径：./jay/斗牛.plac     xpath:   //form/span[1]/input

使用绝对路径还是相对路径：
请你使用相对路径，不到万不得已，千万别使用绝对路径。
更加稳定。


"""

from selenium import webdriver

# 初始化浏览器
# browser = webdriver.Chrome(executable_path=r'‪D:\chromedriver\chromedriver_79.exe')
browser = webdriver.Chrome()
# 进入被测网址
browser.get('http://www.baidu.com')

e = browser.find_elements_by_tag_name('a')

print(e[4])

