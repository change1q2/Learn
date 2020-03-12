"""
============================
Author:柠檬班-木森
Time:2019/11/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from HomeWorkuntist.untist.py15.Homework.HTMLTestRunnerNew import HTMLTestRunner
from HomeWorkuntist.untist.py15.Homework.readexcel import ReadExcel
from HomeWorkuntist.untist.py15.Homework.testcases import LoginTestCase, RegisterTestCase

# 第一步，创建一个测试套件
from HomeWorkuntist.untist.py16.HomeWork import testcases

suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))

# 第三步：创建一个测试运行程序启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个html格式报告文件，将句柄传给stream
                        tester="musen",  # 报告中示的测试人员
                        description="python24第二次作业报告",  # 报告中显示描述信息
                        title="24期的登陆和注册的ddt测试报告")  # 报告中的标题

# 第四步：使用启动器去执行测试套件
runner.run(suite)
