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
import testcases



# 第一步，创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中

# 第1种，通过模块去加载用例
# 创建一个加载对象
# import testcases
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))

# 第2种：通过测试用例类去加载
# import testcases
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(testcases.LoginTestCase))

# 第3种 ：添加单条测试用例
# from testcases import LoginTestCase
# 创建一个用例对象
# 注意点：通过用例类去创建测试用例对象的时候，需要传入用例的方法名（字符串类型）
# case = LoginTestCase("test_login_pass")
# suite.addTest(case)

# 第4种，指定测试用例的所在的目录路径，进行加载（）
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r"用例文件所在的目录的绝对路径"))


# 第三步：创建一个测试运行程序启动器
runner = unittest.TextTestRunner()

# 第四步：使用启动器去执行测试套机
runner.run(suite)
