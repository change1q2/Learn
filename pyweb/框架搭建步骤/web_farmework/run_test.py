'''
作者：seak
时间：
项目：
题目：
作用：
备注：
pytest 运行：
1， pytest.main()   python: 代码形式.  生产环境。
2， 命令行的形式   : 在项目根目录下运行 pytest 命令
3， pycharm 右键运行（如果pycharm 没有出现 pytest 命令，run. configraiton 当中进行配置。）


pytest 收集测试用例的规则（pytest 将怎样的函数看成是测试用例）
1， 模块名：  test_*.py 或者是 *_test.py
2， 类名： TestLogin
3,  方法名： test_

类形式：
class TestYang:

    # 不要写 __init__() 函数， 容易报错

    def test_yangleduo(self):
        pass

pytest打标签
把正向用例，打一个 success 的标签
使用方法：：
0， 标签最好提前注册（pytest 的版本）
1， 在对应的用例方法名称上加一个标签： @pytest.mark.标签名称
TODO: 2， 运行的时候，只运行指定标签下面的测试用例  pytest -m  "success", 标签名加双引号，记住，不要用
单引号
3,


可以同时打多个标签吗？
能，直接在方法明上加上多个 @pytest.mark.标签名
可以多个标签一起执行吗？and or
能， pytest -m "login and success"

或者
pytest -m "login or success"


跳过某些用例
1，跳过测试用例的执行： pytest.mark.skip ,  不是自己定义的，是 pytest 内置的标记，
2， 条件跳过。（环境不同，判断数据库地址，生成环境：“23.45.67.233”）
@pytest.mark.skipif(db_host == 'localhost', reason='只测试线上环境，不测试本地环境')
def test_develop_env(self):
    pass

'''
import time
import pytest

#自动收集测试用例，自动执行
# pytest.main()

# #可以选择某些固定标签进行用例执行
# pytest.main(['-m failed','-s'])

#pytest生成测试报告
ts = str(int(time.time()))
#pytest.main(['-m failed', '-s', "--html=report/report_{}.html".format(ts)])

pytest.main(['-m error', '-s', r"--alluredir=alluredir/"])

