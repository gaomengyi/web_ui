# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

driver = webdriver.Chrome()
# 打开网页
driver.get("http://test-sh-mini-cms.dtinsights.cn/#/login")
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@class="el-input__inner" and '
                                                                          '@type="text"]')))
# 输入账号密码，点击登录按钮
driver.find_element(by=By.XPATH, value='//input[@class="el-input__inner" and @type="text"]').send_keys("18339914656")
driver.find_element(by=By.XPATH, value='//input[@class="el-input__inner" and @type="password"]').send_keys(
    "18339914656")
driver.find_element(by=By.XPATH, value='//button[@type="button"]').click()
# 点击内容管理tab页
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//span[text()="内容管理"]')))
# 点击内容管理
driver.find_element(by=By.XPATH, value='//span[text()="内容管理"]').click()
time.sleep(3)
# 点击报道，进入报道列
driver.find_element(by=By.XPATH, value='//span[text()="报道"]').click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div['
                                                                          '1]/div/div/form/div['
                                                                          '4]/div/div/div/div/input')))

# 点击状态下拉框搜索，展开下拉框
driver.find_element(by=By.XPATH,
                    value='//*[@id="app"]/section/section/main/div/div[1]/div/div/form/div[4]/div/div/div/div/input').click()
time.sleep(3)
# 选择草稿箱选项并点击
driver.find_element(by=By.XPATH, value='//*[@class="el-select-dropdown__item"]//span[text()="草稿箱"]').click()

"""
浏览网页需要滚动条滚动的区域 如果滚动条不滚动会报错不可见错误
1、移动到元素对象底端与当前窗口底部对齐 driver.execute_script("arguments[0].scrolllntoView(false)",element)
2、移动到元素对象顶端与当前窗口顶部对齐 driver.execute_script("arguments[0].scrolllntoView()",element)
3、移动到页面底部 driver.execute_script("window.scrolllnTo(0,document.boby.scrollHeight);")
4、移动到页面顶部 driver.execute_script("window.scrolllnTo(document.boby.scrollHeight);")
"""
# 滚动条处理
# 1、找到要滚动可视的区域
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div['
#                                                                           '1]/div/div/div[3]/ul/li[2]')))
# ele = driver.find_element(by=By.XPATH, value='//*[@id="app"]/section/section/main/div/div[1]/div/div/div[3]/ul/li[2]')
# # 2、使用js实现滚动操作 滚动到底部
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# ele.click()  # 点击第二页翻页

# 点击添加报道按钮
WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    (By.XPATH, '//button[@class="el-button el-button--primary el-button--default me-right2"]')))
driver.find_element(by=By.XPATH,
                    value='//button[@class="el-button el-button--primary el-button--default me-right2"]').click()

# 移动滚动轴到 ele1属性位置
time.sleep(5)
ele1 = driver.find_element(by=By.XPATH, value='//div[@class="el-upload-dragger"]')
# 移动滚动轴滚动到页面底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-upload-dragger"]')))
# 点击这个属性打开上传文件弹窗
ele1.click()

# 调用upload上传文件exe文件
os.system(r"C:\Users\EDY\AppData\Local\AutoIt v3\SciTE\upload.exe")
