"""
元素定位
id/classname/name/tagname

"""
import warnings

from selenium import webdriver
import warnings

# 启动浏览器，开启与浏览器之间的会话
# 存储log日志在具体的地址
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service_log_path=r"D:\chromedriver_service.log")
driver.get("https://www.baidu.com/")

# 方式一 id
warnings.simplefilter("ignore", DeprecationWarning)  # 忽略这个方法过时的警告信息
ele = driver.find_element_by_id("kw")

print(ele)
# 获取这个ele中的class属性
print(ele.get_attribute("class"))

# 方式二 class
eles = driver.find_element(by=By.CLASS_NAME, value="s_ipt")
driver.find_element_by_class_name("s_ipt")
print("使用CLASS_NAME查到的", eles)

# 方式三 name
# 有多个相同的name的时 用elements 如果有多个name只用element时，默认是选中的第一个
ele1 = driver.find_element(by=By.NAME, value="wd")
print("最新的NAME方法查到的name", ele1)

# 方法四 tagname
driver.find_elements(by=By.TAG_NAME, value="input")

# 方式五、六link_text、By.PARTIAL_LINK_TEXT
driver.find_element(by=By.LINK_TEXT, value="更多产品")  # 全部匹配link_text
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="产品")  # 部分匹配link_text

# 方法五 xpath
driver.find_element(by=By.XPATH, value="")
# 绝对定位，右键复制xpath即可，以//开头 非常依赖于页面的顺序和位置

"""
1、相对定位 以//开头 不依赖于页面的顺序和位置，只看页面中有没有符合表达式的元素；相对定位尽量不要用下标
2、格式：//标签名称[@属性名="属性值"] 例如：//input[@type="hidden"]
3、可以运用逻辑运算 and or， 格式：//标签名称[@属性名="属性值" and @属性名="属性值"]例如：//input[@type="hidden" and @name="ch"]
4、运用层级定位例如：//div[@id="u1"]//a[@id="s-top-loginbtn"]  父级和子级中用/或者//;
text()文本定位  查找例如：//div[@id="s-top-left"]//a[text()="地图"] 
contains(@属性名称/text(),属性值) 通过部分匹配部分class名字查找 例如：//div[contains(@id,"hotsearch") and contains(@class,"isindex")]

"""

# 方法六 轴运算
# ancestor:祖先节点、包括父
# parent:父节点
# perceding-sibling:当前元素节点标签之前的所有兄弟节点
# following-sibling:当前元素节点标签之后的所有兄弟节点
# 轴节点：节点名称    例如：//div//table//td//preceding::td

