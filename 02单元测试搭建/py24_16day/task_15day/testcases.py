"""
============================
Author:柠檬班-木森
Time:2019/11/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from login import login_check
from readexcel import ReadExcel

from py24_16day.task_15day.ddt import ddt, data


# excel = ReadExcel("cases.xlsx", "login")
# login_cases = excel.read_data()
# excel2 = ReadExcel("cases.xlsx", "register")
# register_cases = excel2.read_data()


# 定义登录的测试用例类
@ddt  # @ddt 做的事情等同于这句代码==> LoginTestCase = ddt(LoginTestCase)
class LoginTestCase(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "login")
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        # 第一步：准备用例的执行的数据
        case_data = eval(case["data"])
        expected = eval(case["expected"])
        case_id = case["case_id"]
        # 第二步：调用功能函数，获取实际结果
        result = login_check(*case_data)

        # 第三步：比对实际结果和预期结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            # 用例执行未通过
            self.excel.write_data(row=case_id + 1, column=5, value="未通过")
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=5, value="通过")

# @ddt
# class RegisterTestCase(unittest.TestCase):
#
#     @data(*[11,22,33,444])
#     def test_register(self,item):
#         pass
