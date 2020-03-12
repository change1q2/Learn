import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

# 定时器，等待器, poll_frequency(轮训时间，频率)
# wait = WebDriverWait(driver, 30, 0.2)
# 计时器，等待谁出来，等待什么事情发生，条件：当。。。出现 True, False,
# if (a == b)

# 等待某个条件被触发。
# 表示元素被加载
# condition = EC.visibility_of_element_located()


# 表示元素可以被看见，查看。可视
# 等待元素可以被点击
# condition = EC.presence_of_element_located()


# TODO:
# 条件。
# 1, visib, 2, presence, EC.element_to_be_clickable
# 2, locator,一定一定是一个什么类型的？？？ 元组，


# 定位器
# locator = ('xpath', "//input[@id='kw']")
# # 条件
# condition = EC.visibility_of_element_located( locator   )
# e = wait.until(condition)
# # wait.until_not()
# print(e)
#
# # logger, handler, logger.add,  setLevel
#
#
# e = WebDriverWait(driver, 30, 0.2).until(
#         EC.visibility_of_element_located((By.XPATH, "//input[@id='kw']")))


# 偷懒
# 弄懂显示等待的原理
# f


# 学习阶段，不要去用
# 显示等待。
def wait_element(driver, timeout, poll, locator):
    # locator = ("xpath", "//")
    used_time = 0
    while used_time < timeout:
        try:
            e = driver.find_element(*locator)
            return e
        except:
            time.sleep(poll)
            used_time += poll
    # 超时了
    raise TimeoutError('元素定位超时')


e = wait_element(driver, 30, 0.4, ('id', 'kw'))

e.send_keys("柠檬班")


