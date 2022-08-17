"""
测试编辑报道
1、前提条件：登录成功
2、有已经存在的报道
3、前置条件如果没有报道可以通过接口加报道
步骤：
步骤一、登录成功
步骤二、报道页面获取编辑前的报道名称
步骤三、选择一个报道点击编辑按钮
步骤四、修改报道名称点击保存按钮
断言：（断言部分不能太多）
步骤五、比对断言列表的报道名称！=之前报道名称
"""
from PageObjects.login_page import LoginPage

"""
设计测试用例原则
1、每个测试用例保证他的独立性 互不影响
2、多个用例使用一个前置条件时 可以将前置添加写入setup中
3、选择的测试用例可以带有目的性，例如这部分是做冒烟测试（主流程的用例），那部分是做回归测试（繁琐的重复执行的用例做回归测试）
4、自动化测试也可以做配置检查、数据库检查等
"""
import time
import unittest
from PageObjects.index_page import IndexPage
from selenium import webdriver
from TestCases.test_login import TestLogin
from PageObjects.report_page import ReportPage
from Test_Datas import login_datas as LD


class TestReport(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        global driver
        # 前置条件 打开浏览器并且登录成功

        # 这个前置用例只需要打开一次
        print("-------这是执行用例之前的，setUpClass整个测试类里只执行一次---------")

        cls.driver = webdriver.Chrome()  # 实例化一个driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://test-sh-mini-cms.dtinsights.cn/#/login")

        # 实例化ui登录页面一个对象
        cls.index_page = IndexPage(cls.driver)
        cls.report = ReportPage(cls.driver)
        # 调用登录成功的方法
        lg = LoginPage(cls.driver)
        # 步骤：输入用户名 密码 点击登录
        lg.login(LD.success_data['username'], LD.success_data['pwd'])

    @classmethod
    def tearDownClass(cls):
        global driver
        print("-------这是执行用例之前的，tearDownClass整个测试类里只执行一次---------")
        # 这个前置条件关闭一次
        # cls.driver.quit()

    def tearDown(self):
        print('每次执行用例都刷新一次')
        # 每次执行用例都刷新一次
        self.driver.refresh()

    # 新建报道成功正常用例
    def test_creat_report_success(self):
        # 先打开报道列表
        self.index_page.report_list()
        # 执行新建报道操作
        self.report.creat_report("0803报道", "0803报道内容")
