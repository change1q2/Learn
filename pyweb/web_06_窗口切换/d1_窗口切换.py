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

#显示等待#更好的表达方式,BY.XPATH可以解耦
e2 = WebDriverWait(driver, 30, 0.2).until(
    EC.presence_of_element_located((By.XPATH,"//div/a[contains(text(),'lemon.ke.qq.com')]"))
)
print(e2)
# 找到腾讯课堂位置
ketang = driver.find_element_by_xpath('//*[contains(text(), "lemon.ke.qq.com/")]')

#获取窗口句柄： window_name 名（），句柄（黄口的id）
# handeles = driver.window_handles
# print(handeles)
# #切换窗口
# driver.switch_to.window(handeles[-1])


handles = driver.window_handles
print("点击之前的所有的句柄", handles)

before_handle = driver.current_window_handle
print("切换之前", driver.current_window_handle)
#点击腾讯课堂
ketang.click()

#连起来使用
#WebDriverWait(driver, 20,0.2).until(EC.new_window_is_opened(   handles    ))

# print("等待之后", driver.current_window_handle)
#
# print("等待之后的所有的窗口句柄", driver.window_handles)
#
# driver.switch_to.window(driver.window_handles[-1])
# print("切换之后的窗口句柄", driver.current_window_handle)


#关闭游览器
time.sleep(2)
driver.quit()




