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
from 课堂代码重练.py24_13day.HomeWork import testcases
from HTMLTestRunnerNew import *
from 课堂代码重练.py24_13day.runtest2 import suite

#第一步，创建一个测试套件
suite = unittest.TestSuite()

#第二步，将测试用例加入到测试套件中
#4种方法，先记住前2个
#1.通过加载模块去加载用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))

# #2.通过模块类去加载
# loader = unittest.TestLoader()
# suit.addTest(loader.loadTestsFromTestCase(testcases.LoginTestCase))

#第三步，创建一个测试运行启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
                        tester="seak",                    # 报告种显示的测试人员
                        description="python24第一份测试报告",        # 报告种显示描述信息
                        title="24期上课的测试报告")                 # 报告的标题
#第四步，使用启动器
runner.run(suite)