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
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


#显示等待简单实用方式
def wait_element(driver,timeout,poll,locator):
    locator = ("xpath","//input[@id='kw']")
    used_time = 0
    while True:
        try:
           #driver.find_element(By.XPATH,"//input[@id='kw']")#直接这么写没有找到会报异常，可以弄个异常捕获try except
            e = driver.find_element(*locator)#locator有两个参数，这里进行拆包将方法里面只传的一个locator元祖拆包成2个参数传给find_element
            return e
        except:
            time.sleep(0.2)
            used_time += poll
#超时了抛出一个异常
    raise TimeoutError("元素定位超时")

e = wait_element(driver,30,0.4,('id',"kw"))
e.send_keys("柠檬班")


def Explicit_Waits(driver, way, path):
    try:
        ele = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((way, path)))
        return ele
    except Exception as e:
        print('元素寻找失败： ' + str(e))

