from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# 给这个模块设置别名为EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
"""
三种切换
driver.switch_to.alert
driver.switch_to.frame()
driver.switch_to.window()
"""

driver = webdriver.Chrome()

driver.get(r'C:\Users\EDY\PycharmProjects\python_web\web_ui\demo.html')

# 判断弹窗是否出现
WebDriverWait(driver, 10).until(EC.alert_is_present())
# alert切换 不是html切换
alert = driver.switch_to.alert
# alert文本
print(alert.text)
# 关闭弹出框（接受）
alert.accept()
# 关闭弹出框（忽略）
# alert.dismiss()


