# '''
# 作者：seak
# 时间：
# 项目：
# 题目：
# 作用：
# 备注：投标
# '''
# import time
# import unittest
# from decimal import Decimal
#
# from selenium import webdriver
# from data.login_data import login_data_success
# from pages.index_page import IndexPage
# from pages.login_page import LoginPage
# from pages.bid_page import BidPage
# from pages.user_page import UserPage
#
# class TestBid(unittest.TestCase):
#
#     def setUp(self) -> None:
#         '''前置条件
#         #1.登陆
#         #2.有标可投
#         #3， 有钱。  没有钱就要充值，冲多少？大于投资金额。
#         #4， 标的有余额可以供你投。
#         '''
#      #1.初始化游览器
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(20)
#
#         #初始化页面
#         self.login_page = LoginPage(self.driver)
#         self.index_page = IndexPage(self.driver)
#         self.bid_page = BidPage(self.driver)
#         self.user_page = UserPage(self.driver)
#
#         #登录
#         login_data = login_data_success[0]
#        # self.driver.save_screenshot()#截屏
#         self.login_page.login(login_data['mobile'],login_data['pwd'])
#
#
#     def tearDown(self) -> None:
#             pass
#
#     def test_bid_error(self):
#         '''测试投资失败'''
#         time.sleep(2)
#         #self.index_page.get()  #有404BUG用这个线进入页面再执行避开这个BUG
#         url = 'http://120.78.128.25:8765/Index/index.html'
#         self.driver.get(url)
#
#         # 如果不等待新页面出现而直接定位元素，可能找到的是上一个页面中的元素
#         self.index_page.get_element_bid().click()
#         print("hello")
#
#         #定位投标输入框
#         bid_element = self.bid_page.get_element_bid_input()
#         #发送投标金额
#         bid_element.send_keys("1")
#         #获取实际结果
#         actual = self.bid_page.get_element_error_msg().text
#         self.assertEqual(actual,'请输入10的整数倍')
#
#
#
#
#     # def test_bid_success(self):
#         """投资成功"""
#         time.sleep(2)
#         self.index_page.get()  # 有404BUG用这个线进入页面再执行避开这个BUG
#
#         # 如果不等待新页面出现而直接定位元素，可能找到的是上一个页面中的元素
#         self.index_page.get_element_bid().click()
#         print("hello")
#
#         # 定位投标输入框
#         bid_element = self.bid_page.get_element_bid_input()
#
#         #获取余额字符串
#         money_before = bid_element.get_attribute("data-amount")
#
#         # 发送投标金额
#         bid_element.send_keys("100")
#         # 获取实际结果
#         self.bid_page.get_element_bid_btn_msg().click()
#
#         #断言是否成功
#         actual = self.bid_page.get_success_msg().text
#         self.assertEqual(actual,'投标成功')
#
#         #断言余额是否扣除成功
#         #1.获取投标之前的余额
#         #2.获取投标之后的余额
#         self.bid_page.get_bid_active_locator().click()
#
#         #user页面，获取投标之后的余额
#
#         #获取他的text文本，因为有个元不能进行加减乘除，所以要去掉元
#         money_after = self.user_page.get_element_money().text[:-1]
#
#         #用decimal可以解决精度问题
#         self.assertEqual(Decimal(money_before) - Decimal("100"),Decimal(money_after))
#
#
#
#
#
#
