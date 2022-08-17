import time
import unittest

import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.index_page import IndexPage
from Test_Datas import login_datas as LD
from ddt import ddt, data
from TestCases import conftest

"""
用例之间保持独立性不要藕断丝连 每个用例能独自运行
"""


#
# @ddt()
# 表示引入access_web这个fixture，在整个测试类里面只会运行一次
@pytest.mark.demo
@pytest.mark.usefixtures("fuc_demo")
def test_demo():
    print("ttttttttt")
    assert False


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # def setUp(self):
    #     # 前置：访问登录页面
    #     self.driver = webdriver.Chrome()  # 实例化一个driver
    #     self.driver.get("http://test-sh-mini-cms.dtinsights.cn/#/login")  # 每次执行用例都会打开一个浏览器
    #     self.lg = LoginPage(self.driver)  # 实例化ui登录页面一个对象
    #     # 打开浏览器后等待5秒
    #     # self.lg.login_exit()
    #     time.sleep(5)

    # @classmethod
    # def setUpClass(cls):
    #     # 这个前置用例只需要打开一次
    #     print("-------这是执行用例之前的，setUpClass整个测试类里只执行一次---------")
    #     cls.driver = webdriver.Chrome()  # 实例化一个driver
    #     cls.driver.get("http://test-sh-mini-cms.dtinsights.cn/#/login")  # 每次执行用例都会打开一个浏览器
    #     cls.lg = LoginPage(cls.driver)  # 实例化ui登录页面一个对象
    #     # 打开浏览器后等待5秒
    #     # cls.lg.login_exit()
    #     time.sleep(5)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("-------这是执行用例之前的，tearDownClass整个测试类里只执行一次---------")
    #     # 这个前置条件关闭一次
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     # 每次执行用例都刷新一次
    #     self.driver.refresh()

    # 正常用例 登录成功

    def test_login_1success(self, access_web):  # 使用conftest里面返回的两个值
        # 步骤：输入用户名 密码 点击登录
        access_web[1].login(LD.success_data['username'], LD.success_data['pwd'])
        # 等待10秒 看元素有没有出现 等待已经封装到index_page里面
        # 断言：调用index_page页面看是否能找到那个元素 判断是否为true
        assert (IndexPage(access_web[0]).isExist_ele())  # pytest的断言 true返回成功，false返回失败

    # 异常用例(用户名数据错误，密码为空，用户名为空)
    # @data(*LD.phone_datas)
    # # 利用ddt依次输入三次异常的数据
    # @pytest.mark.parametrize("item", LD.phone_datas)  # 使用pytest实现参数化
    # def test_login_0wronguser(self, item, access_web):  # 先执行这三个异常用例
    #     # 步骤：输入错误的用户名 密码 点击登录
    #     print(item)
    #     access_web[1].login(item['username'], item['pwd'])
    #     # 等待10秒 看元素有没有出现 等待已经封装到index_page里面
    #     # 断言：调用index_page页面看是否能找到那个元素 判断是否为true
    #     self.assertFalse(IndexPage(self.driver).isExist_ele())


if __name__ == '__main__':
    pytest.main()
