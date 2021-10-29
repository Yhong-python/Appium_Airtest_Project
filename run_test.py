#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: run_test.py
@time: 2021/10/25 16:43
@desc:
'''
import pytest
import os
if __name__ == '__main__':
    pytest.main(['-v','--alluredir=./allure-report/raw','./TestCases/test_demo.py'])
    os.system("allure generate ./allure-report/raw -o allure-report/html --clean")