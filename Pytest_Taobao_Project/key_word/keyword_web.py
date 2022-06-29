#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/3/13 20:29
# @Description     : selenium 关键字驱动类:常用操作行为封装为关键字
# @Software : PyCharm
"""
1、创建driver
2、访问url
3、定位元素
4、click
5、send_keys
6、webDriverWait
7、quit
8、相对定位器(作业)

"""
import os
import time
from datetime import datetime

import allure
from selenium import webdriver

# 自定义关键字类
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with, RelativeBy
from selenium.webdriver.support.wait import WebDriverWait
from Selenium_POM.Utils.chromeOptions import chromeOptions

# def open_browser(type_):
#     if type_ == 'Chrome':
#         driver = webdriver.Chrome(options=chromeOptions())
#         driver.set_page_load_timeout(5)
#         return driver
#     else:
#         try:
#             driver = getattr(webdriver, type_)()
#         except Exception:
#             driver = webdriver.Chrome()
#         return driver


"""
python反射机制
    四大内置函数：getattr,获取指定类的属性
    getattr(类，属性)  = 类.属性  ，获取函数需要加上()
"""


class WebKeys:

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(5)
        self.driver.implicitly_wait(10)

    #获取title
    def get_title(self):
        return  self.driver.title

    # 访问url
    def open(self, url):
        try:
            self.driver.get(url)
        except:
            # 加载慢的情况执行刷新操作
            self.driver.refresh()

    def locate(self, name=None, value=None, relative: RelativeBy = None, moreEl=False):
        if moreEl:
            return self.driver.find_elements(name, value)
        if relative is None:
            el = self.driver.find_element(name, value)
            self.locator_station(el)  # 圈出定位地方
            self.scroll_to_view(el)     #移动到视野中
            return el
        else:
            return self.driver.find_element(relative)  # 相对定位方法

    def click(self, name, value):
        self.locate(name, value).click()

    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 显示等待
    def web_el_wait(self, name, value):
        WebDriverWait(self.driver, 10).until(
            lambda el: self.locate(name, value),
            message="元素查找失败"
        )

    # 强制等待
    def wait(self, time_=3):
        time.sleep(time_)

    # 切换句柄
    def switch_handle(self, isclose_=False, index=1):
        handle = self.driver.window_handles
        if isclose_:
            self.driver.close()
        self.driver.switch_to.window(handle[index])

    def switch_frame(self, name=None, value=None):
        # 第一种方法
        # if name == 'id' or name == 'name':
        #     self.driver.switch_to.frame(value)
        # self.driver.switch_to.frame(self.locate(name,value))
        # 第二种方法
        # try:
        #     self.driver.switch_to.frame(self.locate('id',value))
        # except NoSuchElementException:
        #     try:
        #         self.driver.switch_to.frame(self.locate('name',value))
        #     except NoSuchElementException:
        #         self.driver.switch_to.frame(self.locate(name,value))
        # 第三种方法
        if name is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate(name, value))

    # 退出iframe
    def exit_frame(self):
        self.driver.switch_to.default_content()

    # 相对定位
    def relative_locate(self, relative_name: By, relative_vlaue: str, location: str, name, value):
        relative = locate_with(relative_name, relative_vlaue)  # 返回RelativeBy对象
        # if location in (locator:=['above','below','to_left_of','to_right_of']):
        #     relative_ = getattr(relative,location)(self.locate(name,value))
        #     return self.locate(relative=relative_)
        # else:
        #     raise Exception('定位方式错误，正确方式包括{}'.format(locator))
        relative_ = getattr(relative, location)(self.locate(name, value))
        return self.locate(relative=relative_)

    def assert_txt(self, name, value, txt):
        try:
            if txt == self.locate(name, value).text:
                return True
            else:
                print('实际结果:{}与预期结果：{},不一致'.format(self.locate(name, value).text,txt))
                raise Exception
        except:
            if not os.path.exists('./failImage'):
                os.mkdir('./failImage')
            file_name = "./failImage/{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), "用例失败截图")
            self.driver.save_screenshot(file_name)
            with open(file_name, mode='rb') as f:
                file = f.read()
            allure.attach(file, f'预期结果：{txt}不存在', allure.attachment_type.PNG)
            return False

    # js执行器
    def js(self, js: str, locator=None):
        if locator is None:
            self.driver.execute_script(js)
        else:
            self.driver.execute_script(js, locator)

    # 鼠标悬停
    def mouse_hold(self, name, value):
        ActionChains(self.driver).move_to_element(self.locate(name, value)).perform()

    # 显示点位点
    def locator_station(self, locator):
        self.driver.execute_script('arguments[0].setAttribute("style",arguments[1]);',
                                   locator,
                                   "border:2px solid red;"
                                   )
    #聚焦显示
    def scroll_to_view(self,locator):
        self.js(
            'arguments[0].scrollIntoView({block: "center"})',
            locator
        )
    #双击事件
    def double_click(self, name, value):
        ActionChains(self.driver).double_click(self.locate(name, value)).perform()

    #模拟滑块
    def drop_by_offset(self,se_name,se_value,sb_name,sb_value):
        slipper_ele = self.locate(se_name,se_value)
        slipper_button = self.locate(sb_name,sb_value)
        print('滑块是否可见', slipper_button.is_displayed())
        if not slipper_button.is_displayed():
            self.js('arguments[0].setAttribute("style","display:block")', slipper_button)
        print('滑块是否可见2:', slipper_button.is_displayed())
        ActionChains(self.driver).click_and_hold(slipper_button).perform()
        ActionChains(self.driver).move_by_offset(258, 0).perform()
        ActionChains(self.driver).pause(0.5).release().perform()
        # ActionChains(self.driver).drag_and_drop_by_offset(slipper_button,300,32).perform()

    def close(self):
        self.driver.quit()
