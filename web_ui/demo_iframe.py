import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# 给这个模块设置别名为EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
切换iframe
1、首先找到你要切换的iframe
"""
driver = webdriver.Chrome()
driver.get("https://ke.qq.com/")
driver.maximize_window()
# 使用显性等待判断登录按钮存在并点击
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, '//a[text()="登录" and @class="btn-default mod-entry-login js-login-op"]')))  # 里面使用的是一个元组
time.sleep(3)
element.click()
# 方式一、切换frame进入到另一个html页面
# 用xpath定位进入iframe页面
# time.sleep(1)
# driver.switch_to.frame(driver.find_element(By.XPATH, value='//div[@class="login-qq-iframe-wrap"]//iframe'))
# driver.find_element(By.XPATH, value='//a[@class="link" and @id="switcher_plogin"]').click()

# 方式二、iframe等待并切换
time.sleep(1)
# 使用显性等待找到ifrmae并切换进入iframe页面中去
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//div[@class="login-qq-iframe'
                                                                                     '-wrap"]//iframe')))
time.sleep(1)
driver.find_element(By.XPATH, value='//a[@class="link" and @id="switcher_plogin"]').click()

# 从iframe中回到默认页面
driver.switch_to.default_content()  # 跳回到顶层文件中 默认的页面
driver.switch_to.parent_frame()  # 跳回到他的父级页面
