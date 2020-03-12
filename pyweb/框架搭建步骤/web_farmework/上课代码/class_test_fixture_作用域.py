'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

'''
setUp:每个测试用例执行之前都会执行
setUpClass:每个测试用例方法整个类之前会执行的


'''
import pytest

from selenium import webdriver

# @pytest.fixture()
# def init_web():
#     #前置条件
#     yield    #返回测试用例当中需要的变量,driver, login_page
#
#     #return
#     #后置条件

'''
fixture  对应也有这样的作用于
1.每个测试用例都运行一次scope="function"
2.每个测试类只执行一次scope="class"
3.每个模块只执行一次scope="module"
4.每个包只执行一次scope="package"
5.整个会话只执行一次scope="session"
'''
import pytest

from selenium import webdriver
#1.每个测试用例都运行一次
test_data = [1,2,3]




#有4分参数可以使用scope="function",`` (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"全局``
@pytest.fixture()
def manage_browser():
    # 初始化浏览器
    driver = webdriver.Chrome()
    print("before")
    yield driver
    print("after")
    driver.quit()



# @pytest.mark.parametrize("test_info",test_data)
# def test_helloworld(test_info, manage_browser):
#     pass



class TestHelloworld:
    @pytest.mark.parametrize("test_info",test_data)
    def test_helloworld(self,test_info):
        pass

    @pytest.mark.usefixtures('manage_browser')
    def test_hellowrld_2(self, manage_browser):
        pass

# class TestRainBow:
#     @pytest.mark.parametrize("test_info", test_data)
#     def test_RainBow(self, test_info, manage_browser):
#         pass
#
#     @pytest.mark.usefixtures('manage_browser')
#     def test_RainBow_2(self):
#         '''空的'''
#         pass


if __name__ == '__main__':
   # 3'--reruns 3'（重复运行3次）,--reruns-delay 2'（间隔时间）
    pytest.main(['--reruns 3', '--reruns-delay 2'])