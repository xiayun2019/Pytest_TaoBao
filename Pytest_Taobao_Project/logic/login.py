#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/4/17 20:21
# @Description     : taobao 登录基类
# @Software : PyCharm
import allure

from Pytest_Taobao_Project.key_word.keyword_web import WebKeys
from Pytest_Taobao_Project.page import allPages


class Login(WebKeys):
    @allure.step("登录")
    def login(self):
        # 输入用户名
        self.input(*allPages.taobao_login_user, '18226141872')
        # 输入密码
        self.input(*allPages.taobao_login_pwd, 'xiayun666')
        try:
            # 如果有滑块
            self.drop_by_offset(*allPages.taobao_login_slipper_ele, *allPages.taobao_login_slipper_button)
        except Exception as e:
            pass
        # 点击登录
        self.click(*allPages.taobao_login_login)