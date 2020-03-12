
db_host = 'localhost'

# 打一个成功标签
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



    @pytest.mark.skip("和现在的需求不符合，过期了。")
    def test_yuz(self):
        pass

    @pytest.mark.skipif(db_host == 'localhost', reason='只测试线上环境，不测试本地环境')
    def test_develop_env(self):
        pass

