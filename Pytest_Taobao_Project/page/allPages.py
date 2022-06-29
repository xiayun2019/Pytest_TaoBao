#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/4/17 20:23
# @Description     : 集合页面元素
# @Software : PyCharm

"""
淘宝登录页:https://login.taobao.com/member/login.jhtml
"""
taobao_login_iframe = ('xpath', '//iframe[contains(@id,"J_MiniLoginIfr")]')
taobao_login_user = ('id', 'fm-login-id')
taobao_login_pwd = ('id', 'fm-login-password')
taobao_login_login = ('xpath', '//button[text()="登录"]')
#登录滑块和框
taobao_login_slipper_ele = ('xpath', '//span[@class="nc-lang-cnt"]')
taobao_login_slipper_button = ('id', 'nc_1_n1z')

"""
淘宝首页
"""
taobao_index_searchInput = ('id', 'q')
taobao_index_searchConfirmButton = ('xpath', '//button[text()="搜索"]')

"""
搜索商品后的选择
样式：
"""
taobao_goods_choose_first = ('xpath', '//a[contains(@id,"J_Itemlist_PLink")]')
taobao_goods_attribute = ('xpath', '//ul[contains(@class,"J_TSaleProp")]')
taobao_goods_num = ('xpath', '//input[contains(@class,"tb-text")]')
#天猫 id J_LinkBasket
taobao_TianMao_goods_addToCart = ('id', 'J_LinkBasket')
#
taobao_goods_addToCart = ('xpath', '//a[@class="J_LinkAdd"]')
#是否加入成功的断言
taobao_isSuccess_toCart = ('xpath', '//div[@class="result-hint"]')
