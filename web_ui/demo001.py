from selenium import webdriver

# 打开浏览器
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 访问一个网页
driver.get("https://www.baidu.com/")

# 窗口最大化
driver.maximize_window()
# 回退上一页
driver.back()
# 回到下一页
driver.forward()
# 刷新
driver.refresh()

# 获取标题
print(driver.title)
# 获取网址
print(driver.current_url)
# 获取窗口的句柄
print(driver.current_window_handle)
# 结束会话,关闭当前的窗口
driver.quit()
# driver.find_element(by=By.XPATH,"")
