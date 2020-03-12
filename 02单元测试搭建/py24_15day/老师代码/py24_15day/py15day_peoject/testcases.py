"""
============================
Author:柠檬班-木森
Time:2019/11/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

'''
再去封装两个读取数据的方法
一个写入数据的方法

'''
import unittest

# 导入登录功能函数
from login import login_check
from readexcel import ReadExcel
from register import register

excel = ReadExcel("cases.xlsx", "login")

excel2 = ReadExcel("cases.xlsx", "register")


# 定义登录的测试用例类
class LoginTestCase(unittest.TestCase):

    def __init__(self, methodName, data, expected, case_id):
        super().__init__(methodName)
        self.data = data
        self.expected = expected
        self.case_id = case_id

    def test_login(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = self.data
        # 2、预期结果：
        expected = self.expected

        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)

        # 第三步：比对实际结果和预期结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            # 用例执行未通过
            excel.write_data(row=self.case_id + 1, column=5, value="未通过")
            raise e
        else:
            excel.write_data(row=self.case_id + 1, column=5, value="通过")


class RegisterTestCase(unittest.TestCase):

    def __init__(self, methodName, data, expected, case_id):
        super().__init__(methodName)
        self.data = data
        self.expected = expected
        self.case_id = case_id

    def test_register(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = self.data
        # 2、预期结果：
        expected = self.expected

        # 第二步：执行功能函数，获取实际结果
        result = register(*data)

        # 第三步：比对实际结果和预期结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            # 用例执行未通过
            excel2.write_data(row=self.case_id + 1, column=5, value="未通过")
            raise e
        else:
            excel2.write_data(row=self.case_id + 1, column=5, value="通过")
