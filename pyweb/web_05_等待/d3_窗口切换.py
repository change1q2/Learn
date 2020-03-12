import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

input_elem = driver.find_element_by_id('kw')
input_elem.send_keys('柠檬班')

# 百度提交
driver.find_element_by_id('su').click()


# 点击腾讯课堂
ketang = driver.find_element_by_xpath('//*[contains(text(), "lemon.ke.qq.com/")]')
ketang.click()

# 获取窗口 window_name 名（）, 句柄（窗口的id）
handles = driver.window_handles
print(handles)
# 切换窗口
driver.switch_to.window(handles[-1])
#
e = driver.find_element_by_xpath('//h4[text()="华华老师"]')
print(e.text)


