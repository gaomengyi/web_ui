import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Locators.loginpage_locators import LoginPageLocator as loc
from Common.basepage import BasePage


class ReportPage(BasePage):

    def creat_report(self, title, content):
        """
        现在已经进入新建报道页面
        :param title: 报道标题名称
        :param content: 内容名称
        :return:
        """
        # 点击作者展开作者下拉框
        time.sleep(3)
        self.click_element(loc.writer)
        # 选择作者下拉框中的第二个
        time.sleep(3)
        self.click_element(loc.chose_writer)
        # 输入标题内容
        time.sleep(3)
        self.input_text(loc.title_text, title)
        # 等待并进入到文本iframe中去
        WebDriverWait(self.driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(loc.content_iframe_text))
        # 输入文本内容
        time.sleep(3)
        self.input_text(loc.content_text, content)

        # 滚动条移动到底部
        time.sleep(3)
        js = "var q=document.body.scrollTop=10000"
        self.driver.execute_script(js)

        # 点击行业领域展开行业领域下拉框
        time.sleep(3)
        self.click_element(loc.field)

        # 选择行业领域中的第一个
        time.sleep(3)
        self.click_element(loc.chose_field)

        # 查找发布按钮出现并点击操作
        time.sleep(3)
        # self.wait_elePresence(loc.fabu_button)
        self.click_element(loc.fabu_button)
