'''
作者：seak
时间：
项目：
题目：
作用：
备注：银行登陆
1.将重复的条件放入前置条件， 打开游览器，关闭游览器
2.再写一个用例发现他们的执行逻辑是一样的就需要进行封装
3. 要将数据传入进去就用ddt数据驱动来管理数据
4.进行函数封装，使用PO模式进行页面和数据的分离,将login重新定义一个函数,（函数封装以后的代码逻辑）
5.进行类封装，将页面和代码逻辑进行分离，创建一个pages目录和datas目录
6.进一步优化，发现断言的地方信息不一定一样所以将断言提取出来重新封装一个函数get_error_msg
7.写一个登陆成功的，用例因为页面不一样了所以需要在pages中加入index_page
8.做数据分离，建立一个data文件将将测试数据都丢到里面去,并用locatoe来进行分层路劲处理
9.写一个登陆鉴权的操作，记住需要元素等待 因为弹出框可能会加载出来比较慢
10.加入日志进行日志捕获,
   （1）对可能获取不到元素的地方加入异常捕获,所有元素获取的地方都要加（例如在index_bank_page中）
   （2）异常捕获需要截屏save_screenshot，创建一个config文件夹里面用constant文件保存路径配置文件,

11.(1)考虑到异常捕获在每个元素的地方都要加太麻烦了，所以引入基业概念将常用的都放到基业
   (2)加入基页概念，创建一个common文件夹加入base_page,将常用的不改变的函数方法都放在基业里面
   (3)将基页中需要用的函数都导入到不同的地方，需要用到基页函数方法的地方都去继承基业的类就可以使用了

'''
import time
import unittest
import ddt
from selenium import webdriver
from pages.login_bank_page import LoginPage
from pages.index_bank_page import IndexPage
from data.login_bank_data import (
    test_data_error_01,
    test_data_success,
    login_data_invalid

)

@ddt.ddt
class TestLogin(unittest.TestCase):

    #前置条件将重复的逻辑都放在前置条件里面
    def setUp(self) -> None:
        # 1， 打开浏览器；
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(20)

        # 初始化要用到的页面
        self.login_bank_page = LoginPage(self.driver)
        self.index_bank_page = IndexPage(self.driver)


    #关闭游览器
    def tearDown(self) -> None:
        self.driver.quit()

    # @ddt.data(*test_data_error_01)
    # def test_login_01_error(self,test_info):#用test_info来接收test_data拆包后的参数,加数字可以代表执行的先后顺序
    #     """手机号码为空"""
        # 第一个：获取实际结果（封装以后执行的函数或者方法） res = request.visit()
        # actual = login(self.driver, test_info["username"], test_info["pwd"])
        # actual = self.login_bank_page.login(test_info['username'], test_info['pwd'])

        #将获取错误信息进行重新封装后要这么写
        # self.login_bank_page.login(test_info['username'], test_info['pwd'])
        # actual = self.login_bank_page.get_error_msg()
        # # 第二个：获取预期结果 test_info【‘expected’】
        # expected = test_info['expected']
        # # 第三个：断言
        # self.assertEqual(expected, actual)

    #没有授权的登录
    # 获取没有通过授权
    # @ddt.data(*login_data_invalid)
    # def test_login_02_invalid(self, test_info):
    #     # 登录
    #     self.login_bank_page.login(test_info['username'], test_info['pwd'])
    #  #   time.sleep(2)
    #     # 获取没有通过授权的实际结果
    #     actual = self.login_bank_page.get_invalid_msg()
    #     expected = test_info['expected']
    #     self.assertEqual(expected, actual)




    # 讲登录成功
    @ddt.data(*test_data_success)
    def test_login_success(self,test_info):
        """登录成功"""
        # 执行登录操作， login_page.login()
        self.login_bank_page.login(test_info['username'], test_info['pwd'])
        # 进入了？？页面  我的帐户[python]

        # 定位我的账户
        #self.index_bank_page.get()#如果遇到登陆报404错误可以使用这个代码手动进入当前页面
        time.sleep(3)
        #实际结果
        actual = self.index_bank_page.get_element_user()

        # 预期结果
        expected = test_info['expected']

        #断言，用asserIn可以只断言包含这里面的某个字就行
        self.assertIn(expected ,  actual.text)








"""
# 我们把页面操作的逻辑从测试代码当中提取出来。  函数封装的好处：
# 1， 实现了测试代码和页面代码的分离，维护更加方便。
    --- 一，当页面发生变化的时候，测试代码不需要修改；
    --- 二，测试需求发生变化的时候，页面代码不需要修改；
# 2， 维护成本低；
# 3， 提高代码的复用性。
  1， 逻辑一样的时候，可以重复使用同样的函数调用。
###                    2, 不同的测试逻辑（测试不同的模块的时候，如果重复用到了同样的步骤）
只需要去调用相关的函数就可以了。
# 4 ，可读性更强。

"""
