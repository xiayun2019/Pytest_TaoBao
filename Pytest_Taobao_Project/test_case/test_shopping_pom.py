#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/4/17 20:59
# @Description     : 测试用例
# @Software : PyCharm
import SafeDriver.drivers
import allure
import pytest
from Pytest_Taobao_Project.key_word.keyword_web import WebKeys
from Pytest_Taobao_Project.logic.shopping_tb import GoodSale
from Pytest_Taobao_Project.page import allPages


@allure.epic('淘宝用例')
class TestShop:
    #购物流程
    # @pytest.mark.slow
    goods = ['增高垫']

    @allure.feature('购买商品')
    @pytest.mark.parametrize('good', goods)
    def testcase_01(self, browser, good):
        """
        购物，购买随意商品
        """
        action = GoodSale(browser)
        action.shopping(good)
        action.assert_txt(*allPages.taobao_isSuccess_toCart, '已成功加入购物车')
        # SafeDriver.drivers.driver()

    #删除全部购物车商品
    def testcase_02(self,browser):
        #先调用进行购物
        action = GoodSale(browser)
        action.shopping()
        #删除购物车商品
        wk = WebKeys(browser)

        #全选商品

        #点击删除

        #点击确认

    def testcase_03(self, browser):
        """
        修改购物车商品
        :return:
        """
        # 先调用进行购物
        action = GoodSale(browser)
        action.shopping()
        wk = WebKeys(browser)

        #鼠标悬停

        #点击SKU

        #选择颜色分类

        #点击确认

    def testcase_04(self,browser):
        """
        移入收藏夹
        :param browser:
        :return:
        """
        # 先调用进行购物
        action = GoodSale(browser)
        action.shopping()
        wk = WebKeys(browser)

        #点击移入收藏夹

    def testcase_05(self,browser):
        """
        购买相似商品
        :param browser:
        :return:
        """
        action = GoodSale(browser)
        action.shopping()
        wk = WebKeys(browser)

