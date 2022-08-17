from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

"""
回车 Keys.ENTER
删除 Keys.BACK_SPACE
空格 Keys.SPACE
回退键 Keys.ESCAPE
刷新 Keys.F5
"""
driver = webdriver.Chrome()
#  访问一个网页
driver.get("https://www.baidu.com/")
driver.maximize_window()
time.sleep(5)
# 搜索内容并回车
driver.find_element(by=By.ID, value='kw').send_keys("古天乐", Keys.ENTER)

"""
浏览网页需要滚动条滚动的区域 如果滚动条不滚动会报错不可见错误
1、移动到元素对象底端与当前窗口底部对齐 driver.execute_script("arguments[0].scrolllntoView(false)",element)
2、移动到元素对象顶端与当前窗口顶部对齐 driver.execute_script("arguments[0].scrolllntoView()",element)
3、移动到页面底部 driver.execute_script("window.scrolllnTo(0,document.boby.scrollHeight);")
4、移动到页面顶部 driver.execute_script("window.scrolllnTo(document.boby.scrollHeight);")
"""

"""
修改时间控件，不可编辑改为可编辑状态
"""
driver.get("https://www.12306.cn/index/")
driver.maximize_window()

# js语句
js = 'var ele = document.getElementById("train_date");ele.readOnly=false;ele.value="2018-12-30";'
# 执行js语句
driver.execute_script(js)
