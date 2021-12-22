'''
@File:config.py
@DateTime:2021/12/17 21:13
@Author:wh
@Desc:
'''
import sys
import os
# print(os.getcwd())
# print(os.path.dirname(os.path.dirname(__file__)))
driver_path=f"{os.path.dirname(os.path.dirname(__file__))}\driver\chromedriver.exe"
url="http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html"
file=r"D:\PythonLx\script\data\testdata.xlsx"
sheet="login"
log_path=r"D:\PythonLx\script\log\log.txt"