'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
from 课堂代码重练.py24_13day.HomeWork.login import login_check

'''
在unittest中
测试用例类:自己定义的类只要继承于unittest中的TestCase,那么这个类就是一个测试用例类

测试用例：测试用例类中，以test开头的方法就是一条测试用例


用例执行通没通过的评判标准：断言异常


一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。 
而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。只能直接类名.属性名或类名.方法名
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。可以来调用类的属性，类的方法，实例化对象等，避免硬编码


        使用*args可以传入多个参数，并且处理时，按照现将多个值转成一个元组处理
        data = {"a": 1, "b": 2} 
        def foo(*kwargs):
        print kwargs
        #foo(data, "aaa", "bbb")
        
        **代表了给函数传入参数的方式是：a=1形式，即：参数名=参数值，并且不管传入几个值，该函数都会转化为字典处理
           data = {"a": 1, "b": 2}
           def foo(**kwargs):
           print kwargs 
           foo(a=1, b=2)　　     
        

'''
import unittest
from login import login_check

#定义一个测试用列类，类名为LoginTestCase，参数为unittest.TestCase
class LoginTestCase(unittest.TestCase):

    #定义一个setUP方法，每条用例执行之前都会执行这个类
    def setUp(self):
        print("用例{}开始执行--".format(self))

    #定义一个tearDown方法，每条用例执行结束后都会执行这个类
    def tearDown(self):
        print("用例{}执行结束".format(self))

    # @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
    # 可以来调用类的属性，类的方法，实例化对象等，避免硬编码
    @classmethod #修饰器
    # 定义一个setUpClass方法， 当成测试用例类中的用例执行之前，会执行改方法
    def setUpClass(cls):
        print("----setup--classs----")

    @classmethod
    #定义一个tearDownClass方法，当成测试用例类中的用例执行完毕，会执行改方法
    def tearDownClass(cls):
        print("----teardown---classs")

#定义各种测试用列
     #定义一个登陆成功测试用例
    def test_login_pass(self):
        #第一步：准备用列数据
        #1.用列的参数
        data = ("python24","lemonban")
        #2.预期结果
        expected = {"code":0,"msg":"登陆成功"}

        #第二步，执行功能函数，获取实际结果
        result = login_check(*data)

        #第三步，比对实际结果和预期结果
        self.assertEqual(expected,result)

     #定义一个登陆密码错误失败测试用列的方法
    def test_login_pwd_error(self):
        #第一步准备测试用例
        #1.用列的参数
        data = ('python24','123')
        #2.预期结果
        expected = {"code":1,"msg":"帐号或者密码不正确"}
        #第二步，执行功能函数，获取实际结果
        result = login_check(*data)
        #第三步，比对实际结果和预期结果
        self.assertEqual(expected,result)

    def test_login_user_error(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ("python", "lemonban")
        # 2、预期结果：
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def test_login_user_is_none(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = (None, "lemonban")
        # 2、预期结果：
        expected = {"code": 1, "msg": "所有的参数不能为空"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def test_login_pwd_is_none(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ('python24', None)
        # 2、预期结果：
        expected = {"code": 1, "msg": "所有的参数不能为空"}
        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

    def login_test(self):
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ("python24", "lemonban")
        # 2、预期结果：
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：执行功能函数，获取实际结果
        result = login_check(*data)

        # 第三步：比对实际结果和预期结果
        self.assertEqual(expected, result)

# 如果直接运行这个文件，就使用unittest中的main函数来执行测试用例
if __name__ == '__main__':
    unittest.main()