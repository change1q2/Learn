"""
alert 切换的总结：
1， alert 弹框是 web 页面的原生控件，无法进行定位。
2， 当 alert 出现的时候，只需要完成切换，点击确认或者取消，让他消失，就可以了。

driver.switch_to.alert
注意： 没有括号

alert 等待：


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
driver.find_element_by_id('hello').click()

# TODO: 切换到 alert 弹框上面, switch_to 不需要加括号
# switch_to.alert 得到的是一个 Alert 对象
myalert = driver.switch_to.alert
# 确认按钮
myalert.accept()
# 取消按钮
# myalert.dismiss()

# alert 等待
WebDriverWait(driver, 10).until(EC.alert_is_present())

#


