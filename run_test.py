#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: run_test.py
@time: 2021/10/25 16:43
@desc:
'''
import pytest
from common_utils.appium_serve import AppiumServe
import os
if __name__ == '__main__':
    pytest.main(['-v','--alluredir=./allure-report/raw','./TestCases/test_demo.py'])
    os.system("allure generate ./allure-report/raw -o allure-report/html --clean")
    #查看报告的方法
    # AppiumServe.release_port('8088')
    # os.system("allure open -h 127.0.0.1 -p 8088 ./allure-report/html")
