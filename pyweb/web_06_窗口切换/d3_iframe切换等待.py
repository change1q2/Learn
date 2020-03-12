"""
iframe 等待：

参数：
4种：
- 索引   1
- name  "baidu"
- webelement   e = driver.find_element_by_...()
- locator 元组  (By.XPATH, '//iframe[@name="baidu"])'


如何判断需要定位的元素在iframe 当中：
看源码下面的条星框


# 切换到父级iframe
driver.switch_to.parent_frame()

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

# iframe 等待
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
    (By.XPATH, '//iframe[@name="baidu"]')
))

# 定位
driver.find_element_by_id('kw')

# 定位主页面的元素，切换到主页面
driver.switch_to.default_content()
driver.find_element_by_id('hello')

# 切换到父级iframe
# driver.switch_to.parent_frame()
