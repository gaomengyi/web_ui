import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# 给这个模块设置别名为EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

"""
等待：三种等待方法
1、强制等待 sleep(秒)
2、隐性等待=全局等待 implicity_wait(秒) 设置最长等待时间，在这个时间内加载完成，则执行下一步 整个driver的会话周期，设置一个即可全局都可用
会话周期：打开浏览器到关闭浏览器
切换弹窗的时候 并不能解决所有问题
3、显性等待 明确等到某个条件满足之后再往下执行，否则继续等待，直到超过设置的最大时间，超过抛出异常
WebDriverWait(driver, 10).until()
"""

driver = webdriver.Chrome()
driver.get("https://baidu.com")
# 强制等待
time.sleep(2)
driver.maximize_window()
# 全局等待
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH, value='//a[contains(@class,s-top-login-btn) and @id="s-top-loginbtn"]').click()
# WebDriverWait类，显性等待
time.sleep(1)
# 传参为元素表达式作为一个元组
# 显性等待查找元素是否存在
element = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.XPATH, '//input[@id="TANGRAM__PSP_11__userName"]')))
element.send_keys("18339914656")
