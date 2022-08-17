"""

一个页面一个类
一个功能一个方法
测试用例里面才需要加断言，pageObject不需要断言
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Locators.loginpage_locators import LoginPageLocator as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    """元素定位 调用loginpage_locators文件中的定位元素
    起个别名叫loc
    """

    # 登录页面元素封装
    def login(self, username, pwd):

        # 输入用户名，用户名参数化
        # 后加*，以下是给元组解包去掉元组外面的()
        doc = "登录模块-登录功能"
        self.input_text(loc.name_text, username, doc)
        # 输入密码，密码参数化
        self.input_text(loc.pwd_text, pwd, doc)
        # 点击登录按钮
        self.click_element(loc.button_login, doc)

    def login_exit(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="el-input__inner" and @placeholder="用户名')))

    # 获取密码为空的异常用例
    def get_login_nopwd(self):
        self.wait_elePresence(loc.nopwd_button, 10)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.nopwd_button))
        return self.driver.find_element(*loc.nopwd_button).text  # 返回文本值

    # 用户名为空的异常用例
    def get_login_nousername(self):
        self.wait_elePresence(loc.nouser_button,10)
        # 返回用户名为空的提示的文本值
        a = self.driver.find_element(*loc.nouser_button).text
        print("打印出来text是什么", a)
        return self.driver.find_element(By.XPATH, loc.nouser_button).text  # 如果不解包 可以这样写
