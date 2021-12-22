'''
@File:user.py
@DateTime:2021/12/17 12:12
@Author:wh
@Desc:
'''
import unittest

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器！")

    def setUp(self):
        print("登录禅道！")

    def tearDown(cls):
        print("登出禅道！")
#测试用例1
    def test_adduser(self):
        print("执行添加组织用户测试用例！")

#测试用例2
    def test_showuser(self):
        print("执行查看组织用户测试用例！")

#测试用例3
    def test_updateuser(self):
        print("执行修改组织用户测试用例！")

#测试用例4
    def test_delete(self):
        print("执行删除组织用户测试用例！")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器！")