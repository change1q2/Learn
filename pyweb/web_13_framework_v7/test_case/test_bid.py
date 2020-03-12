# #!/usr/bin/env python3
# #-*- coding:utf-8 -*-
# # email: wagyu2016@163.com
# # wechat: shoubian01
# # author: 王雨泽
# import time
# import unittest
# from decimal import Decimal
#
# from selenium import webdriver
#
# from data.login_data import login_data_success
# from pages.bid_page import BidPage
# from pages.index_page import IndexPage
# from pages.login_page import LoginPage
# from pages.user_page import UserPage
#
#
# class TestBid(unittest.TestCase):
#
#     def setUp(self) -> None:
#         """
#         前置条件：
#         1， 登录
#         :return:
#         """
#         self.driver = webdriver.Chrome()
#         # self.driver.save_screenshot()
#         self.driver.implicitly_wait(20)
#
#         # 初始化页面
#         self.login_page = LoginPage(self.driver)
#         self.index_page = IndexPage(self.driver)
#         self.bid_page = BidPage(self.driver)
#         self.user_page = UserPage(self.driver)
#
#         # 登录
#         login_data = login_data_success[0]
#         self.login_page.login(login_data['mobile'], login_data['pwd'])
#
#     def tearDown(self) -> None:
#         pass
#
#     # def test_bid_error(self):
#     #     "测试投资失败"
#     #     time.sleep(1)
#     #     self.index_page.get()
#     #
#     #     # 如果不等待新页面出现而直接定位元素，可能找到的是上一个页面当中的元素。
#     #     self.index_page.get_element_bid().click()
#     #
#     #     # 定位投标输入框
#     #     bid_element = self.bid_page.get_element_bid_input()
#     #
#     #     # 发送投标金额
#     #     bid_element.send_keys("1")
#     #
#     #     # 获取实际结果
#     #     actual = self.bid_page.get_element_bid_btn().text
#     #     self.assertEqual(actual, '请输入10的整数倍')
#
#     # PO
#     def test_bid_success(self):
#         """测试投资成功"""
#         time.sleep(1)
#         self.index_page.get()
#
#         # 如果不等待新页面出现而直接定位元素，可能找到的是上一个页面当中的元素。
#         self.index_page.get_element_bid().click()
#
#         # 定位投标输入框
#         bid_element = self.bid_page.get_element_bid_input()
#
#         # 获取余额, 字符串
#         money_before = bid_element.get_attribute("data-amount")
#
#         # 发送投标金额
#         bid_element.send_keys("100")
#
#         self.bid_page.get_element_bid_btn().click()
#
#         # 如何断言投资成功
#         actual = self.bid_page.get_success_msg().text
#         self.assertEqual(actual, '投标成功！')
#
#         # 断言余额是否正确扣除，
#         # 1， 获取投标之前的余额
#         # 2， 获取投标之后的余额  ==
#         self.bid_page.get_active_btn().click()
#         # user 页面 获取投标之后的余额
#
#         money_after = self.user_page.get_element_money().text[:-1]
#         self.assertEqual(Decimal(money_before) - Decimal("100") , Decimal(money_after))
#
#
#         # 投标详情页  定位输入框（输入金额）
#
#
#     # def test_bid_success(self):
#     #     """投资成功"""
#     #     pass
#
#
