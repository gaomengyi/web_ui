import os

"""
框架项目顶层目录
"""
# 定位到根目录
base_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
testdatas_dir = os.path.join(base_dir, "Test_Datas")
testcases_dir = os.path.join(base_dir, "TestCases")
htmlreport_dir = os.path.join(base_dir, "outputs\\reports\\test_report.html")
screenshot_dir = os.path.join(base_dir, "outputs\\screenshots")
