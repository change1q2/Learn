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
import testcases

# 创建测试套件
suite = unittest.TestSuite()

# 添加一个模块中所有的测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))



# 生成html文件的的测试报告

with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            title='柠檬班测试报告',
                            description='这是我们24期的第一次生成报告的作业',
                            tester='MuSen')

    runner.run(suite)


