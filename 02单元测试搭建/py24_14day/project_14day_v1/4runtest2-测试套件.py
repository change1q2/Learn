"""
============================
Author:柠檬班-木森
Time:2019/11/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
这个文件是测试程序运行的启动文件

"""
import unittest

from HTMLTestRunnerNew import HTMLTestRunner
from testcases import LoginTestCase
from readexcel import ReadExcel
# 第一步，创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中


# 读取excel中所有的用例数据
excel = ReadExcel("cases.xlsx","login")
cases = excel.read_data()


for item in cases:
    # 创建一个用例对象
    case = LoginTestCase("test_login", eval(item['data']), eval(item["expected"]))
    suite.addTest(case)

# # 注意点：通过用例类去创建测试用例对象的时候，需要传入用例的方法名（字符串类型）
# case = LoginTestCase("test_login",("python24", "lemonban"),{"code": 0, "msg": "登录成功"})
# suite.addTest(case)




# 第三步：创建一个测试运行程序启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个html格式报告文件，将句柄传给stream
                        tester="musen,小明,大哥",                    # 报告中示的测试人员
                        description="python24第一份测试报告",        # 报告中显示描述信息
                        title="24期上课的测试报告")                 # 报告中的标题

# 第四步：使用启动器去执行测试套机
runner.run(suite)
