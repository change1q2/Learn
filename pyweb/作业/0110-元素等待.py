'''
作者：seak
时间：
项目：
题目：
作用：
备注：
根据上课内容，使用显示等待，在百度页面搜索柠檬班，定位柠檬班腾讯课堂当中的 “小简老师”
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()
#进行隐式等待:得不到某个元素就等待一段时间，直到拿到某个元素位置，超过对应等待时间会报异常。
driver.implicitly_wait(30)

#输入游览器地址
driver_url = driver.get("https://www.baidu.com")

#找到搜索框
#显示等待
e1 = WebDriverWait(driver, 30, 0.2).until(
    EC.presence_of_element_located((By.XPATH,"//input[@id='su']"))
)
print(e1)
find_su = driver.find_element_by_id("kw").send_keys("柠檬班")

#找到百度一下，点击
find_kw = driver.find_element_by_id("su").click()

#显示等待
e2 = WebDriverWait(driver, 30, 0.2).until(
    EC.presence_of_element_located((By.XPATH,"//div/a[contains(text(),'lemon.ke.qq.com')]"))
)
print(e2)

#找到柠檬班腾讯课堂，点击
#find_lemone = driver.find_element_by_link_text("柠檬班_腾讯课堂")
find_lemone = driver.find_element_by_xpath("//div/a[contains(text(),'lemon.ke.qq.com')]")


#等待新窗口出现
handeles = driver.window_handles #列表
print("点击之前的所有句柄",handeles)

before_handeles = driver.current_window_handle #字符串
print("切换之前的窗口句柄",before_handeles)

#点击柠檬班课堂
find_lemone.click()
#..............................................................................................
#等待新窗口的打开new_window_is_opened
WebDriverWait(driver,20).until(
    EC.new_window_is_opened(handeles)
)
print("等待之后的句柄",driver.current_window_handle)#字符串
print("等待之后的所有句柄",driver.window_handles)#列表

#窗口切换switch_to.window
driver.switch_to.window(driver.window_handles[-1])#字符串
print("切换之后的窗口句柄",driver.current_window_handle)

# #找到小简老师点击
teacher = driver.find_element_by_xpath("//h4[contains(text(),'小简')]")
print(teacher)
teacher.click()
#关闭游览器
time.sleep(2)
driver.quit()