'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''
db_host = 'localhost'
import pytest

import pytest


@pytest.mark.login
@pytest.mark.success
def test_demo_xianrenzhang():
    pass


@pytest.mark.login
@pytest.mark.failed
def test_demo_yuer():
    pass


@pytest.mark.yuz
class TestYang:
    @pytest.mark.success
    @pytest.mark.yang
    def test_yangleduo(self):
        pass



    @pytest.mark.skip("和现在的需求不符合，过期了。")#会自动过滤掉这条用例
    def test_yuz(self):
        pass

    @pytest.mark.skipif(db_host == 'localhost', reason='只测试线上环境，不测试本地环境')
    def test_develop_env(self):
        pass