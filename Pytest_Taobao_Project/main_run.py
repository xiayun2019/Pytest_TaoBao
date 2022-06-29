#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xiayun
# @Time     : 2022/4/17 20:57
# @Description     : 执行接口
# @Software : PyCharm
import os

import pytest


def run():
    pytest.main(['-s', '-v', './test_case/test_shopping_pom.py',
                 # '--maxfail', '2',
                 # '-m', 'slow'  # 指定运行的用例 标签slow
                 '--allure-features=购买商品',
                 '--alluredir', './reportData',
                 '--clean-alluredir'
                 ])
    # os.system('allure generate ./reportData -o ./report/ --clean')
    os.system('allure serve reportData')




if __name__ == '__main__':
    run()