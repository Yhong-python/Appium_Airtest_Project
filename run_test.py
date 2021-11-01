#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: run_test.py
@time: 2021/10/25 16:43
@desc:
'''
import pytest
from common.utils.cmd_utils import AppiumServe
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-v','--alluredir=./allure-report/raw', './TestCases/test_demo.py'])
    os.system("allure generate ./allure-report/raw -o allure-report/html --clean")
    # 查看报告的方法
    # AppiumServe.release_port('8088')
    # os.system("allure open -h 127.0.0.1 -p 8088 ./allure-report/html")

    # pytest.main(['-m','test_1.py','-s'])
    # '--log-format=%(asctime)s %(levelname)s %(message)s', '--log--date-fromat=%Y-%m-%d %H:%M:%S',
