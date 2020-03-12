"""
1, 鼠标悬停到设置
2， 点击高级设置



select 选择的用法
1， 直接定位 option 元素，点击
2， Select

"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

# 输入键盘， send_keys("柠檬班")
e = driver.find_element_by_id('kw')
e.send_keys('柠檬班')
# 提交的方式：1，点击百度一下，  2， 回车， 3，submit(是一定要在一个form 表单当中。)

# 输入回车键
e.send_keys(Keys.ENTER)

# e.send_keys(Keys.CANCEL, 'a')

time.sleep(2)

#
# find_element_by()  ==> js find_element_
# click()    ===> js  click()

# 发送 js 代码
driver.execute_script()