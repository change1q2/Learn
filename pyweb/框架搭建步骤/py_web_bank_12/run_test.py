

"""
发现测试用例，然后运行用例，生成测试报告。
unittest

HTML


步骤：
1， 分析需求
2， 测试计划
3， 测试用例编写
4， 评审
5， 测试用例执行
6， 测试报告
"""

# 第一步：初始化测试套件

# 获取当前目录，
# 第二部：testloader.discover(test_case_dir), 加载测试用例
# 第三部：测试用例添加到测试套件

# 生成测试报告的目录和文件名
# 第四步：启动器， 运行， testrunner.run()


# pytest , 自动收集测试用例
# 自动执行测试用例。

#

import pytest
from other.time import now_datetime_time


ts = str(now_datetime_time())

pytest.main(['-m error', '-s', "--html=report/report_{}.html".format(ts)])


#pytest.main(['-m error', '-s', r"--alluredir=alluredir/"])

