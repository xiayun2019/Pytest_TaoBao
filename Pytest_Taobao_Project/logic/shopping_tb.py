#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/4/17 20:45
# @Description     : 淘宝购物界面
# @Software : PyCharm
import time

import allure

from Pytest_Taobao_Project.logic.login import Login
from Pytest_Taobao_Project.page import allPages


@allure.step('打开浏览器')
class GoodSale(Login):
    @allure.step("购买{goods}") #此种方式相较于with allure.step()能显示出参数
    def shopping(self, goods):
        self.open('https://www.taobao.com')
        # 输入商品名
        self.input(*allPages.taobao_index_searchInput, goods)
        # 点击搜索商品----增加是否登录的判断
        self.click(*allPages.taobao_index_searchConfirmButton)
        try:
            # 弹窗登录，没有则略过
            self.switch_frame(*allPages.taobao_login_iframe)
        except:
            try:
                self.login()
            except:
                pass
        # 点击商品
        self.click(*allPages.taobao_goods_choose_first)
        # 选择样式--需要切换到新页面
        self.switch_handle()
        # attributes的数量说明需要选择的属性数量
        attributes = self.locate(*allPages.taobao_goods_attribute, moreEl=True)
        print('属性值：', len(attributes))
        time.sleep(3)
        # 寻找每一个属性的第一个值，点击
        for i in range(len(attributes)):
            time.sleep(1)
            attributes[i].find_element('tag name', 'a').click()
        # 数量先清空，在输入
        # goods_num = self.locate(*allPages.taobao_goods_num)
        # goods_num.clear()
        # 双击清空
        self.double_click(*allPages.taobao_goods_num)
        self.input(*allPages.taobao_goods_num, '2')
        # 加入购物车-区分天猫及其他
        if 'tmall' in self.get_title():
            self.click(*allPages.taobao_TianMao_goods_addToCart)
        else:
            self.click(*allPages.taobao_goods_addToCart)
        try:
            try:
                # 弹窗登录，没有则略过
                self.switch_frame(*allPages.taobao_login_iframe)
            except:
                pass
            self.login()
        except Exception as e:
            print(e)
        else:
            # print(self.get_title())
            print("再次加入购物车")
            # 采用双击的方式清空
            self.double_click(*allPages.taobao_goods_num)
            # 输入数量
            self.input(*allPages.taobao_goods_num, '2')
            # 添加购物车的元素不同
            if 'tmall' in self.get_title():
                self.click(*allPages.taobao_TianMao_goods_addToCart)
            else:
                self.click(*allPages.taobao_goods_addToCart)
