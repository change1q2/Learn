'''
作者：seak
时间：
项目：
题目：
作用：
备注：
功能函数
'''

def login_check(username=None,password=None):
    """
       登录校验的函数
       :param username: 账号
       :param password:  密码
       :return: dict type
       """
    if all([username,password]):
        if username == 'python24' and password == 'lemonban':
            return{"code":0,"msg":"登陆成功"}
        else:
            return{"code":1,"msg":"帐号或者密码不正确"}
    else:
        return{"code":1,"msg":"所有参数不能为空"}