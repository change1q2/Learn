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

    def __init__(self, methodName, data, expected):
        super().__init__(methodName)#重写父类后一定要继承原来父类里面拥有的函数
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


# 如果直接运行这个文件，就使用unittest中的main函数来执行测试用例
if __name__ == '__main__':
    unittest.main()
