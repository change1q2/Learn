'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

#登陆失败的数据
test_data_error_01 = [
    {"username":"", "pwd": "", "expected": "请输入用户名"},
    {"username":"", "pwd": "123", "expected": "请输入用户名"},
]


#登陆需要鉴权的数据

login_data_invalid = [
    {"mobile":"15746732896", "pwd": "123", "expected": "此账号没有经过授权，请联系管理员!"},
]



#登陆成功的数据

test_data_success = [
    {"username":"pzhbank", "pwd": "123456", "expected": "运营数据"},
    {"username":"gelibank2", "pwd": "123456", "expected": "运营数据"},
]