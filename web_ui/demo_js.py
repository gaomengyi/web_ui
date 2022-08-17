from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
driver.maximize_window()

"""
修改时间控件，不可编辑改为可编辑状态
"""
# js语句
# 给js代码放到一行里面 可以通过命令进行执行
js = 'var ele = document.getElementById("train_date");ele.readOnly=false;ele.value="2018-12-30";'
# 执行js语句
driver.execute_script(js)
js_click = 'var b = document.getElementById("search_one");b.click();'
driver.execute_script(js_click)
