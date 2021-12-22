'''
@File:runner.py
@DateTime:2021/12/17 12:45
@Author:wh
@Desc:
'''
import unittest
from BeautifulReport import BeautifulReport


# suite=unittest.TestSuite()
# suite.addTests(unittest.defaultTestLoader.discover(start_dir=r"D:\PythonLx\script\testcases",pattern='test*.py'))
# test_runner = unittest.TextTestRunner()
# test_runner.run(suite)
#加在准备好的测试用例
cases=unittest.defaultTestLoader.discover(start_dir=r"D:\PythonLx\script\testcases",pattern='test*.py')
#执行测试用例
result=BeautifulReport(cases)
#生成测试报告
result.report(description="系统用户的测试报告",filename="SIT测试报告",report_dir=r"D:\PythonLx\script\report")
