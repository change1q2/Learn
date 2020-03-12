#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
setUp: 每个测试用例执行之前都会执行的
setUpClass:  每个测试用例方法整个类之前会执行的。


fixture 对应的也有这样的作用域：
1， 每个测试用例都运行一次；
2， 每个测试类只执行一次：
3， 每个模块只执行一次
4， 每个包只执行一次
5， 整个会话只执行性一次
"""
import pytest
from selenium import webdriver

test_data = [1,2,3]


@pytest.fixture(scope='module')
def manage_browser():
    # 初始化浏览器
    driver = webdriver.Chrome()
    print("before")
    yield driver
    print("after")
    driver.quit()


@pytest.fixture(scope='function')
def delete_cookie():
    # 初始化浏览器

    print("delete cookie before")
    yield
    print("delete cookie after")




class TestHellworld:
    @pytest.mark.parametrize("test_info", test_data)
    def test_helloworld(self, test_info):
        pass

    @pytest.mark.usefixtures('manage_browser')
    def test_helloworld_2(self):
        """空的"""
        pass


class TestRainBow:
    @pytest.mark.parametrize("test_info", test_data)
    def test_RainBow(self, test_info, delete_cookie, manage_browser ):
        pass

    def test_RainBow_2(self):
        """空的"""
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(['--reruns 3', '--reruns-delay 2'])




