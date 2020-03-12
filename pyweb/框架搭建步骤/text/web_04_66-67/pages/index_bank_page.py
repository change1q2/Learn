'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

class IndexPage:

    url = 'http://inner.meeno.net:20684/dist2/#/homepage/interStatistic'

    def __init__(self, driver):
        self.driver = driver

    def get_element_user(self):
        """获取运营数据"""
        return self.driver.find_element_by_xpath("//*[@class='type-title']/span")

    def get(self):
        """打开当前页面"""
        self.driver.get(self.url)