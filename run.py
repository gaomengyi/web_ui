import unittest
import HTMLTestRunner

from Common.dir_config import htmlreport_dir
from TestCases.test_login import TestLogin
from TestCases.test_report import TestReport

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestReport))  # 只执行这个类下的所有用例
# runner = unittest.TextTestRunner()
with open(htmlreport_dir, 'wb')as file:
    # HTMLTestRunner.HTMLTestRunner   模块.类
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='高萌萌的测试报告名称',
                                           description='高萌萌测试报告的描述', tester='高萌萌')
    runner.run(suite)
