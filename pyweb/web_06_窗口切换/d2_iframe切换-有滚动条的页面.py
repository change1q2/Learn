"""
iframe 切换。

用法：
driver.switch_to.frame()
参数：
1, frame 的索引，
2， iframe 标签的 name 属性
3， iframe 元素的 webelement 对象


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("file:///C:/data/jianguoyun/projects/python24/web_06_%E7%AA%97%E5%8F%A3%E5%88%87%E6%8D%A2/switch_iframe.html")
# 定位 hello world
driver.find_element_by_id('hello')

# 定位 iframe
# 如何判断一个元素在 iframe 当中
# 切换 iframe

# 1,通过 name 切换
# driver.switch_to.frame('baidu')
# # 再定位 iframe 当中的元素
# e = driver.find_element_by_id('kw')


# 2， 通过 webelement 切换
iframe_elem = driver.find_element_by_xpath('//iframe[@name="baidu"]')
driver.switch_to.frame(iframe_elem)

# 3, 通过索引
driver.switch_to.frame(0)




