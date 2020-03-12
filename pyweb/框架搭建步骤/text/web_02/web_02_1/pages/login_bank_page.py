'''
作者：seak
时间：
项目：
题目：
作用：
备注：

6.进一步优化，发现断言的地方信息不一定一样所以将断言提取出来重新封装一个函数get_error_msg
'''

class LoginPage:
    # driver, 浏览器对象 __init__
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        # 3.输入网址
        url = 'http://inner.meeno.net:20684/dist2/'
        self.driver.get(url)

        # 4.定位元素
        # 用户名地址
        login_bank_locator = 'username'
        user_bank_element = self.driver.find_element_by_name(login_bank_locator)
        # 密码地址
        pwd_bank_locator = 'password'
        pwd_bank_element = self.driver.find_element_by_name(pwd_bank_locator)

        # 5.输入用户名和密码
        user_bank_element.send_keys(username)
        pwd_bank_element.send_keys(pwd)

        # 6.提交数据
        click_bank_locator = '//*[@class="el-button btn-submit el-button--default el-button--medium is-plain"]/span'
        click_bank_element = self.driver.find_element_by_xpath(click_bank_locator)
        click_bank_element.click()

        # # 7.断言
        # # 获取实际结果（登陆成功时这个就不适用了）
        # actual_msg = self.driver.find_element_by_xpath("//*[@class='el-form-item__error']")
        # return actual_msg.text

#6.进一步优化，发现断言的地方信息不一定一样所以将断言提取出来重新封装一个函数get_error_msg
    def get_error_msg(self):
        """获取错误提示"""
        error_msg = self.driver.find_element_by_xpath(
            "//*[@class='el-form-item__error']"
        )
        return error_msg.text

    def get_element_username(self):
        """获取帐号输入的元素"""
        return self.driver.find_element_by_xpath("//input[@name='phone']")

    def get_element_pwd(self):
        """获取密码元素"""
        return self.driver.find_element_by_xpath("//input[@name='password']")

    def clear_username(self):
        """清空手机号码"""
        return self.get_element_username().clear()