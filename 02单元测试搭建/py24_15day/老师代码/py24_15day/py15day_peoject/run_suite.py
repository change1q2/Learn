"""
============================
Author:柠檬班-木森
Time:2019/11/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from HTMLTestRunnerNew import HTMLTestRunner
from readexcel import ReadExcel
from testcases import LoginTestCase, RegisterTestCase

# 第一步，创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中

# 1、读取登录功能函数的用例数据，创建用例对象，添加到套件
excel = ReadExcel("cases.xlsx", "login")
cases = excel.read_data()
for item in cases:
    # 创建一个用例对象
    case = LoginTestCase("test_login", eval(item['data']), eval(item["expected"]), item["case_id"])
    suite.addTest(case)

# 2、读取注册功能函数的用例数据，创建用例对象，添加到套件
excel = ReadExcel("cases.xlsx", "register")
cases = excel.read_data()
for item in cases:
    case = RegisterTestCase("test_register", eval(item["data"]), eval(item["expected"]), item["case_id"])
    suite.addTest(case)

# 第三步：创建一个测试运行程序启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个html格式报告文件，将句柄传给stream
                        tester="musen",  # 报告中示的测试人员
                        description="python24第二次作业报告",  # 报告中显示描述信息
                        title="24期上课的测试报告")  # 报告中的标题

# 第四步：使用启动器去执行测试套件
runner.run(suite)
