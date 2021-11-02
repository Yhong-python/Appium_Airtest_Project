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


    #以下运行方式为jenkins中配置参数化构建时，取里面的参数进行运行
    # import sys
    # import pytest
    # jenkins_params=''
    # try:
    #     jenkins_params=sys.argv[1]
    # except IndexError:
    #     print("当前没有选中任何测试选项，执行所有测试")
    # except:
    #     raise
    # marks=''
    # if "ALL" not in jenkins_params and jenkins_params!='':  #执行部分的
    #     marks_list=jenkins_params.split(',')
    #     marks=' or '.join(marks_list)
    #     run_cmd=['-v',f'-m={marks}']
    # else:
    #     run_cmd=['-v']
    # print(f"当前的执行参数为{run_cmd}")
    # pytest.main(run_cmd)