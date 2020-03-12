'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
#启动文件



import unittest
#第一步，创建一个测试套件
from 课堂代码重练.py24_13day.HomeWork2 import testcase
from 课堂代码重练.py24_13day.HomeWork2.HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.TestSuite()

#第二步，将测试用列加载到套件中
#第二种方式用类
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(testcase.RegisterTestCase))



#第三步，创建一个测试运行启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
                        tester="seak",                    # 报告种显示的测试人员
                        description="python24第一份测试报告",        # 报告种显示描述信息
                        title="24期作业的测试报告")                 # 报告的标题

#第四步，使用启动器去执行测试套件
runner.run(suite)