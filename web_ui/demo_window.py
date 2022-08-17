import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 给这个模块设置别名为EC
from selenium.webdriver.support import expected_conditions as EC

"""
一般第一个打开的句柄都会在最后一个
driver.switch_to.window(handles[-1]) 最新的句柄
driver.current_window_handle 切换到当前句柄

"""
driver = webdriver.Chrome()
driver.get("https://baidu.com/")
driver.maximize_window()
driver.find_element(By.ID, value='kw').send_keys("柠檬班")
handles = driver.window_handles  # 当前窗口为1
driver.find_element(By.XPATH, value='//*[@id="su"]').click()
# handles = driver.window_handles  # 当前窗口为1
element1 = WebDriverWait(driver, 20).until(driver.find_element(By.XPATH, value='//*[@id="1"]/div/div[1]/h3/a'))
element1.click()
# 显性等待-等待新的窗口的出现
WebDriverWait(driver, 20).until(EC.new_window_is_opened(handles))
handles = driver.window_handles  # 重新获取一次窗口
# 窗口切换，切换到最新打开的一个窗口
time.sleep(3)
driver.switch_to.window(handles[-1])
print("当前窗口的句柄{0}".format(driver.current_window_handle))
element2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//nav[@class="nav-tabs"]//div['
                                                                                     '@class="details"][1]//span[1]')))
element2.click()

print("打开窗口的句柄", handles)
print("当前窗口的句柄{0}".format(driver.current_window_handle))



