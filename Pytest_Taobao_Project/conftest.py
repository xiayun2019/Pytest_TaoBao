#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/4/17 21:06
# @Description     : 这是一个**功能的Python文件
# @Software : PyCharm
import os
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    """
    定义全局浏览器启动
    :return:
    """
    os.popen(r'F:\PyCharm\project\Pytest_Taobao_Project\chrome.bat')
    sleep(3)
    print('打开浏览器成功')
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    # options.add_argument(r'user-data-dir=C:\Users\44365\AppData\Local\Google\Chrome\User Data')
    options.debugger_address = '127.0.0.1:9100'
    # options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
    driver = webdriver.Chrome(options=options)
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source":
    #         """
    #         Object.defineProperty(navigator, 'webdriver',
    #         {get: () => undefined})
    #         """
    # })

    #隐是等待10s
    driver.implicitly_wait(10)
    yield driver
    #用例后置，关闭浏览器
    # driver.quit()
    # os.system('taskkill /im chromedriver.exe /F')
    # os.system('taskkill /im chrome.exe /F')
    sleep(5)


