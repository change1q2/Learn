"""
============================
Author:柠檬班-木森
Time:2019/11/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

# 导入登录功能函数
from login import login_check
from register import register


# 定义登录的测试用例类
class LoginTestCase(unittest.TestCase):

    def __init__(self, methodName, data, expected):
        super().__init__(methodName)
        self.data = data
        self.expected = expected

    def test_login(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = self.data
        # 2、预期结果：
        expected = self.expected

        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)

        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)


class RegisterTestCase(unittest.TestCase):

    def __init__(self, methodName, data, expected):
        super().__init__(methodName)
        self.data = data
        self.expected = expected

    def test_register(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = self.data
        # 2、预期结果：
        expected = self.expected

        # 第二步：执行功能函数，获取实际结果
        result = register(*data)

        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)
