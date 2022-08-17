"""
鼠标操作
double_click 双击
context_click 右键操作
drag_and_drop 拖动操作，左键按住一个元素拖动到另外一个区域
move_to_element() 鼠标悬停 常用
preform()

"""
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#  访问一个网页
driver.get("https://www.baidu.com/")
driver.maximize_window()
time.sleep(5)
# 第一步 找到要操作的元素
ele = driver.find_element(by=By.XPATH, value='//span[@id="s-usersetting-top" and text()="设置"]')
# 第二步 实例化ActionChains类
# ac = ActionChains(driver)
# # 第三步 将鼠标操作添加到actions列表中
# ac.move_to_element(ele)
# # 第四步 调用perform执行鼠标操作
# ac.perform()  # 现在鼠标的焦点设置在这个元素上

# 可以写成一个步骤
ActionChains(driver).move_to_element(ele).perform()

"""
定位悬浮的下拉框中“高级搜索" 让下拉列表出现再处理
"""
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//span[text()="高级搜索"]')))
driver.find_element(by=By.XPATH, value='//span[text()="高级搜索"]').click()

"""
定位点击下拉框中的下拉列表属性
引入select类
"""
from selenium.webdriver.support.ui import Select

# 1、找到select元素
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="adv-setting-ft"]/div/div[2]/div[2]')))

select_ele = driver.find_element(by=By.XPATH, value='//*[@id="adv-setting-ft"]/div/div[2]/div[2]')
# 2、实例化select类对象
s = Select(select_ele)

# 3、选择下拉框(必须标签是select才可以操作)
# 方式一、下标从0开始
s.select_by_index(6)
# #方式二、value值
# s.select_by_value("ppt")
# #方式三、文本内容
# s.select_by_visible_text("RTF 文件 （.rtf)")
