import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Locators.loginpage_locators import LoginPageLocator as loc
from Common.basepage import BasePage


class IndexPage(BasePage):

    def isExist_ele(self):
        # 验证是否登录成功？首页右上角的“欢迎,xxx"是否存在 如果存在返回true 否则返回false
        locator = (By.XPATH, '//span[text()=" 欢迎！高梦依 "]')
        # self.wait_elePresence(locator)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(locator))
            return True
        except:
            return False

    # 打开报道列表操作
    def report_list(self):
        # 等待内容管理元素出现
        time.sleep(5)
        # self.wait_elePresence(loc.nr_select)
        # 点击内容管理下拉框展开报道
        self.click_element(loc.nr_select)
        # 等待报道管理按钮出现
        time.sleep(5)
        # self.wait_elePresence(loc.click_report)
        # 点击报道管理进入报道列表
        self.click_element(loc.click_report)
        # 等待新建报道按钮出现
        time.sleep(5)
        # self.wait_elePresence(loc.creat_report)
        # 点击报道页面的新建报道按钮
        self.click_element(loc.creat_report)


