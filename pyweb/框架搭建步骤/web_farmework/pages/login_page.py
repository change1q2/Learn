'''
作者：seak
时间：
项目：
题目：
作用：
备注：登录页
所有登陆页面操作

"""封装函数的作用：
1， 节省代码
2， 更加具有可读性
'''

#将页面所有的方法都放在类当中可以要什么就直调用什么（将页面逻辑都放在类当中）

from common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    #driver,游览器对象_init_
    # locator 作为类属性管理
    """locator 分层的好处：
    当页面发生变化的时候，只需要检查固定位置的代码，
    便于管理。
    """
    mobile_element_locator = (By.XPATH, "//input[@name='phone']")
    pwd_element_locator = (By.XPATH, "//input[@name='password']")
    error_msg_locator = (By.XPATH, "//div[@class='form-error-info']")
    invalid_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']")


    # css

    # 显示等待（locator, (By.XPATH, '//input...')）
    #使用显示等待不用拆包，因为显示等待就是传递元祖
    # def get_error_msg(self):
    #     error_msg = WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(self.error_msg_locator)
    #     )
    #     return error_msg.text

    # class

    # name
        #价格：Chrome代表这是游览器对象
    # def __init__(self,driver: Chrome):
    #     self.driver = driver




    def login(self, mobile, pwd):
        # 操作步骤
        '''
          #1.打开游览器(重复操作放到前置条件当中去)
        driver = webdriver.Chrome()
        #设置隐式等待
        driver.implicitly_wait(30)
        '''

        # 2.输入登录网址
        url = 'http://120.78.128.25:8765/login'
        self.driver.get(url)
        # 3定位元素
        mobile_element_locator = "//input[@name='phone']"
        mobile_element = self.driver.find_element_by_xpath(mobile_element_locator)

        pwd_element_locator = "//input[@name='password']"
        pwd_element = self.driver.find_element_by_xpath(pwd_element_locator)

        # 4.输入用户名和密码

        mobile_element.send_keys(mobile)
        pwd_element.send_keys(pwd)

        # 提交数据
        pwd_element.submit()

        # 断言
        actual_msg = self.driver.find_element_by_xpath("//div[@class='form-error-info']")

        return actual_msg.text

    # #不用显示等待传递要拆包
    # def get_error_msg(self):
    #     """获取错误提示"""
    #     error_msg = self.driver.find_element(
    #         *self.error_msg_locator
    #     )
    #     return error_msg.text

    #使用显示等待不用拆包，因为显示等待就是传递元祖
    def get_error_msg(self):
        error_msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.error_msg_locator)
        )
        return error_msg.text

    def get_invalid_msg(self):
        """获取没有通过授权的提示"""
        error_msg = self.driver.find_element(
            *self.invalid_msg_locator
        )
        return error_msg.text

    def get_element_mobile(self):
        """获取手机号码输入的元素"""
        #return self.driver.find_element(*self.mobile_element_locator)
        return self.get_element(self.mobile_element_locator)

    def get_element_pwd(self):
        """获取密码元素"""
    #    return self.driver.find_element(*self.pwd_element_locator)
        return self.get_element(self.pwd_element_locator)


    def clear_mobile(self):
        """清空手机号码"""
        return self.get_element_mobile().clear()

