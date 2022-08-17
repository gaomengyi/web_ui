"""
1、封装基本函数：执行日志、等待时长、异常处理、失败截图
2、所有页面的公共部分
"""
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime

from Common.dir_config import screenshot_dir


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素存在
    def wait_elePresence(self, locator, times=30, poll_frequency=0.5, doc=""):
        """
        :param locator: 元素定位 元组形式
        :param times: 查询的时间
        :param poll_frequency:
        :param doc:模块名
        :return:
        """
        logging.info("等待元素{0}可见".format(locator))
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            return True
        except:
            # exception看到的结果是最详细的对比error
            logging.exception("等待元素可见失败！！！")
            self.save_screenshot(doc)
            return False

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("查找元素{0}".format(locator))
        try:
            return self.driver.find_element(*locator)  # 给元素剖解去掉外层
        except:
            logging.info("查找元素失败！！！")
            self.save_screenshot(doc)
            raise

            # 点击操作

    def click_element(self, locator, doc=""):
        # 找元素
        logging.info("{0}正在执行{1}元素的点击操作".format(doc, locator))  # 在什么页面哪个元素执行点击操作
        ele = self.get_element(locator, doc)  # 调用get_element中的返回结果所以不需要再次剖解
        # 元素操作
        try:
            ele.click()
        except:
            logging.info("元素点击失败！！!")
            self.save_screenshot(doc)
            raise

            # 输入操作

    def input_text(self, locator, text, doc=""):
        # 找元素
        logging.info("{0}正在执行{1}元素的输入操作".format(doc, locator))  # 在什么页面哪个元素执行点击操作
        ele = self.get_element(locator, doc)  # 调用get_element中的返回结果所以不需要再次剖解
        # 元素操作
        try:
            ele.send_keys(text)
        except:
            logging.info("元素输入内容失败！！!")
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        logging.info("{0}正在执行{1}元素获取元素文本操作".format(doc, locator))  # 在什么页面哪个元素执行点击操作
        ele = self.get_element(locator, doc)  # 调用get_element中的返回结果所以不需要再次剖解
        # 元素操作
        try:
            return ele.text
        except:
            logging.info("获取元素的文本内容失败！！!")
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        logging.info("{0}正在执行获取{1}元素的属性".format(doc, locator))  # 在什么页面哪个元素执行点击操作
        ele = self.get_element(locator, doc)  # 调用get_element中的返回结果所以不需要再次剖解
        # 元素操作
        try:
            return ele.get_attribute(attr)
        except:
            logging.info("获取元素的属性失败！！!")
            self.save_screenshot(doc)
            raise

    # 关闭弹窗
    def alert_action(self, locator, action="accept", doc=""):
        logging.info("{0}正在执行{1}关闭弹窗操作".format(doc, locator))  # 在什么页面哪个元素执行点击操作
        # 先找到弹窗定位到弹窗里面
        alert = self.get_element(locator, doc)
        # 元素操作
        try:
            alert.action()
        except:
            logging.info("关闭弹窗失败！！!")
            self.save_screenshot(doc)
            raise

    # 切换iframe
    def switch_iframe(self, locator, doc=""):
        """

        :param locator: 元素定位
        :param doc: 当前页面名称
        :return:
        """
        # 先查找到iframe元素
        iframe = self.get_element(locator, doc)  # 定位iframe框架
        try:
            self.driver.switch_to.frame(iframe)  # 切换到iframe框架
        except:
            logging.info("切换iframe失败")
            self.save_screenshot(doc)
            raise

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换
    # 截图操作
    def save_screenshot(self, name):
        # 图片名称：页面名称_操作名称_操作名称_年-月-日 时:分:秒.png
        # 直截取当前浏览器当中的网页内容
        file_name = screenshot_dir + "{0}_{1}.png"
        self.driver.save_screenshot(file_name)
        logging.info("截图成功,截图的路径为{0}".format(file_name))
