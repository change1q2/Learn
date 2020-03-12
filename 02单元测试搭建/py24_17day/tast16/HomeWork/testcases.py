"""
============================
Author:柠檬班-木森
Time:2019/11/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================

使用DDT的方式来获取EXCLE表中的数据
"""
import unittest

# 导入登录功能函数
from HomeWorkuntist.untist.py15.Homework.login import login_check
from HomeWorkuntist.untist.py15.Homework.readexcel import ReadExcel
from HomeWorkuntist.untist.py15.Homework.register import register
#
# excel = ReadExcel("cases.xlsx", "login")
#
# excel2 = ReadExcel("cases.xlsx", "register")


# 定义登录的测试用例类
from HomeWorkuntist.untist.py16.HomeWork.ddt import ddt,data


# 用ddt方法定义一个登陆方法的类
@ddt  # @ddt 做的事情等同于这句代码==> LoginTestCase = ddt(LoginTestCase)
class LoginTestCase(unittest.TestCase):

    '''
    原方法：
    # def __init__(self, methodName, data, expected, case_id):
    #     super().__init__(methodName)
    #     self.data = data
    #     self.expected = expected
    #     self.case_id = case_id
    '''
    #读取EXCLE表中的login单元名
    excel = ReadExcel("cases.xlsx", "login")
    #读取excle中的数据并放在cases中
    cases = excel.read_data()


    '''
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

    '''
    '''
    补充知识：
    eval() 返回传入字符串的表达式的结果。
    
    '''

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


#用ddt方法定义一个注册是测试用类
@ddt# @ddt 做的事情等同于这句代码==> RegisterTestCase = ddt(RegisterTestCase)
class RegisterTestCase(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "register")
    cases = excel.read_data()

    @data(*cases)
    def test_register(self,case):
        # 第一步：准备用例的执行的数据
        case_data = eval(case["data"])
        expected = eval(case["expected"])
        case_id = case["case_id"]
        # 第二步：调用功能函数，获取实际结果
        result = register(*case_data)

        # 第三步：比对实际结果和预期结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            # 用例执行未通过
            self.excel.write_data(row=case_id + 1, column=5, value="未通过")
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=5, value="通过")




