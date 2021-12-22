'''
@File:register.py
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
    def test_register_success(self):
        print("注册成功！")
#测试用例2
    def test_existuser(self):
        print("历史用户注册！")

#测试用例3
    def test_invaliduser(self):
        print("无效注册！")

