"""
1, 鼠标悬停到设置
2， 点击高级设置



select（下拉框） 选择的用法
1， 直接定位 option 元素，点击
2， Select

"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

# 鼠标悬停到设置
action = ActionChains(driver)
# 定位元素
setting_elem = driver.find_element_by_xpath("//a[@name='tj_settingicon' and @href='http://www.baidu.com/gaoji/preferences.html']")
action.move_to_element(setting_elem)
# 释放动作

action.perform()


# 点击高级搜索 //a[text()="高级搜索"]
gaoji_setting = driver.find_element_by_xpath('//a[text()="高级搜索"]')
action.click(gaoji_setting)
# 释放动作
action.perform()

# action.click().move_to_element().context_click().drag_and_drop().perform()

time.sleep(2)


# select方法一: 直接定位定位微软doc
# doc_elem = driver.find_element_by_xpath("//option[@value='doc']")
# doc_elem.click()
# time.sleep(2)

# select方法二: 使用 selenium 封装
# 第一步：定位 select 元素
s_elem = driver.find_element_by_name('ft')
# 第二部：初始化 Select 类
select = Select(s_elem)
# 第三部：选择, 三种方式：1， value, 2, text,  3, index
select.select_by_value('doc')

# select.select_by_visible_text('微软 Word (.doc)')
# select.select_by_index(1)

time.sleep(2)

