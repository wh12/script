'''
@File:demo.py
@DateTime:2021/12/18 12:45
@Author:wh
@Desc:
'''
from selenium import webdriver
import time
time.sleep(3)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s= Service(r"F:\Test_notbook\selenium\\chromed_driver\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
print(driver)
driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element(By.ID,"kw").send_keys("软件测试")
driver.find_element(By.ID,"su").click()

# driver.find_element_by_id("kw").send_keys("软件测试")
# driver.find_element_by_id("su").click()