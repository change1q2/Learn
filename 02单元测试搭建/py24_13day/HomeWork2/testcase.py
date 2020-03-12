'''
作者：seak
时间：
项目：
题目：
作用：
备注：

注册成功               预期结果：{"code": 1, "msg": "注册成功"}
两次密码不一致         预期结果：{"code": 0, "msg": "两次密码不一致"}
账号已存在             预期结果：{"code": 0, "msg": "该账号已存在"}
密码长度小于6     预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
密码长度大于18    预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
账号长度小于6     预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
账号长度大于18    预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
账号为空          预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
密码为空          预期结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}

'''
#编写测试用例

import unittest
from 课堂代码重练.py24_13day.HomeWork2.register import register


class RegisterTestCase(unittest.TestCase):

    #基本套路
    def setUp(self):
        # 每条用例执行之前都会执行
        print("用例{}开始执行--".format(self))

    def tearDown(self):
        # 每条用例执行之后都会执行
        print("用例{}执行结束--".format(self))

    @classmethod
    def setUpClass(cls):
        # 当成测试用例类中的用例执行之前，会执行改方法
        print("-----setup---classs-----")

    @classmethod
    def tearDownClass(cls):
        # 当成测试用例类中的用例执行完毕，会执行改方法
        print("-----teardown---classs-----")

     #用例编写
    def test_register(self):
        '''正常注册  '''
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ('python2', '123456','123456')
        # 2、预期结果：
        excepted = {"code": 1, "msg": "注册成功"}
        # 第二步：执行功能函数，获取实际结果
        result = register(*data)
        # 第三步：比对实际结果和预期结果
        self.assertEqual(excepted, result)

    def test_register_pwd_dis(self):
        '两次密码不一致'
        #第一步：准备用列数据
        #1.用列参数
        data = ("python2","123456a","1234566")
        #2.预期结果
        '预期结果'
        excepted = {"code": 0, "msg": "两次密码不一致"}
        #第二步，执行功能函数
        result = register(*data)
        #第三步，对比实际结果和预期结果
        self.assertEqual(excepted, result)

    def test_register_user_exist(self):
        '用户已存在'
        #第一步，准备测试数据
        #1.测试传入参数
        data = ("python24","123456","123456")
        #2.期望结果
        excepted = {"code": 0, "msg": "该账号已存在"}
        #第二步，执行功能函数
        result = register(*data)
        #第三步，对比实际结果
        self.assertEqual(excepted,result)

    def test_register_pwd_lt6(self):
        '密码长度小于6位数'
        #第一步，准备用列数据
        #1.用列传入参数
        data = ("pppp",'123456','123456')
        #2.期望结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        #第二步，执行用列,拆包
        result = register(*data)
        #第三步，对比期望和实际结果,断言
        self.assertEqual(excepted,result)

    def test_register_pwd_max18(self):
        '密码长度大于18位'
        #第一步，准备用列参数
        #1.准备传入参数
        data = ("pppp1",'123456789qwertyuiop','123456789qwertyuiop')
        #2.期望
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}


        #第二步，执行用列，拆包
        result = register(*data)


        #第三步，对比期望与实际结果，断言
        self.assertEqual(excepted,result)