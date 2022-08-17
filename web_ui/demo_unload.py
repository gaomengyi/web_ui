import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
长传操作：
有两种情况
1、如果是input可以直接输入路径 那么直接调send_keys输入路径即可
2、非input标签的上传，则需要借助第三方工具
2.1 Autolt 我们去调用其生成的au3或者exe文件
2.2 SendKeys第三方库（目前只支持2.7版本）网址：https://pypi.python.org/pypi/SendKeys
2.3 python pywin32库，识别对话框句柄进而操作
工具：pywin32和spy++
pyautolt库
"""

