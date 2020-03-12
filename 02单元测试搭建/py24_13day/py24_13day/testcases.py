"""
============================
Author:柠檬班-木森
Time:2019/11/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from login import login_check

"""
测试用例类:自己定义的类只要继承于unittest中的TestCase,那么这个类就是一个测试用例类

测试用例：测试用例类中，以test开头的方法就是一条测试用例


用例执行通没通过的评判标准：断言异常


"""


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # 每条用例执行之前都会执行
        print("用例{}开始执行--".format(self))

    def tearDown(self):
        # 每条用例执行之后都会执行
        print("用例{}执行结束--".format(self))

    @classmethod
    def setUpClass(cls):
        # 当成测试用例类中的用例执行之前，会执行改方法
        print("-----setup---classs-----")

    @classmethod
    def tearDownClass(cls):
        # 当成测试用例类中的用例执行完毕，会执行改方法
        print("-----teardown---classs-----")

    def test_login_pass(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ("python24", "lemonban")
        # 2、预期结果：
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)

        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def test_login_pwd_error(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ("python24", "123")
        # 2、预期结果：
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def test_login_user_error(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ("python", "lemonban")
        # 2、预期结果：
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def test_login_user_is_none(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = (None, "lemonban")
        # 2、预期结果：
        expected = {"code": 1, "msg": "所有的参数不能为空"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def test_login_pwd_is_none(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ('python24', None)
        # 2、预期结果：
        expected = {"code": 1, "msg": "所有的参数不能为空"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def login_test(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ("python24", "lemonban")
        # 2、预期结果：
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)

        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)


# 如果直接运行这个文件，就使用unittest中的main函数来执行测试用例
if __name__ == '__main__':
    unittest.main()
