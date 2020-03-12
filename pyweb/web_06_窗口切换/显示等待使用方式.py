'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

#显示等待
#1.初始化定时器，加一个定时器，poll_frequency(轮询时间)
wait = WebDriverWait(driver,30,0.2) #driver游览器要做的事情，30代表等待30秒，0.2代表频率，每0.2秒查询一次
#计时器等待什么事情发生，出现True,不出现False
#if(a == b)

#表示元素被加载
#condition = EC.presence_of_element_located()
#表示元素可以被查看
#condition = EC.visibility_of_all_elements_located()
#表示元素可以被点击
#condition = EC.element_to_be_clickable(locator)

#使用方式，locator确定定位方式和定位数据，传递到condition，condition再将地址传给until就完整的判断出整个条件的传递
#2.初始化定位器,locator一定是一个元祖
locator =("xpath", "//input[@id='kw']")
#3.将定位放到条件当中
condition = EC.element_to_be_clickable(locator)
#4.等某个条件被触发
e = wait.until(condition)
#wait.until_not()#某个条件不被触发
print(e)
#综合起来使用
# e = WebDriverWait(driver,30,0.2).until(
#     EC.presence_of_element_located(("xpath","//input[@id='kw']")))

#更好的表达方式,BY.XPATH可以解耦
e = WebDriverWait(driver,30,0.2).until(EC.presence_of_element_located((By.XPATH,"//input[@id='kw']")))
