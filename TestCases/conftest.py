"""
可以给前置后置的内容放到这个文件中来

"""
import time
import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage

# 声明它是一个fixture
# fixture 默认代表setup和teardown
driver = None


@pytest.fixture(scope="class")  # 声明作用域为class
def access_web():
    """
    前置操作
    yield
    后置操作
    :return:
    """
    global driver
    # 前置条件
    print("-------这是执行用例之前的，setUpClass整个测试类里只执行一次---------")
    driver = webdriver.Chrome()  # 实例化一个driver
    driver.get("http://test-sh-mini-cms.dtinsights.cn/#/login")  # 每次执行用例都会打开一个浏览器
    lg = LoginPage(driver)  # 实例化ui登录页面一个对象
    time.sleep(5)
    yield (driver, lg)  # 分割线，后接受两个返回值
    # 后置条件
    print("-------这是执行用例之前的，tearDownClass整个测试类里只执行一次---------")
    # 这个前置条件关闭一次
    driver.quit()


@pytest.fixture(scope="class")
def refresh_page():
    global driver
    # 前置条件
    yield
    # 后置条件
    driver.refresh()

@pytest.fixture(scope="class")
def fuc_demo():
    print("我是开始的时候执行的-----")
    yield
    print("我是每次后置条件执行的----------")