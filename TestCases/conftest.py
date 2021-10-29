#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: conftest.py
@time: 2021/10/25 14:26
@desc:
'''
import pytest
from appium import webdriver
from pageObject.basepage import BasePage
from common_utils.utils import AdbUtils, FileUtils
from config.root_config import DEVICE_INFO_PATH
from common_utils.appium_serve import AppiumServe

# @pytest.fixture(scope='session')
@pytest.fixture(scope='session',autouse=True)
def start_appium_session(cmdopt):
    # print(cmdopt)
    device_info = cmdopt

    # 先判断app是否已安装
    AdbUtils.is_app_insntall()
    #     device_info={
    #         'platformName': 'Android',
    #         'platformVersion': '10',
    #         'unicodeKeyboard': True ,
    #         'resetKeyboard': True  ,
    #         'automationName': 'uiautomator2',
    #         'deviceName': '7XBRX18A16002686',
    #         'appPackage': 'com.door.qp.hjproject',
    #         'appActivity': 'com.qp.LaunchActivity',
    #         # 'appPackage': 'com.tencent.mobileqq',
    #         # 'appActivity': '.activity.SplashActivity',
    #         'noReset': False ,
    #         'skipServerInstallation': True,
    #         'skipDeviceInitialization': True
    #     }

    #手动启appium服务
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_info)
    #自动启动appium服务
    AppiumServe.start_appium_server(ip='127.0.0.1', port=4723, bport=62001)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', device_info)
    base=BasePage()
    #设置类变量driver
    driver=base.set_driver(driver)
    yield driver

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store",
                     default='devices1',
                     choices=['devices1','devices2'],
                     help="将命令行参数--cmdopt添加到pytest配置中")


@pytest.fixture(scope="session")
def cmdopt(request):
    default_device_path = DEVICE_INFO_PATH
    default_device_info = FileUtils.read_yaml(default_device_path)
    cmdopt_value=request.config.getoption("--cmdopt")
    return default_device_info.get(cmdopt_value)

@pytest.fixture(scope="session")
def connect_airtest():
    """
    连接airtest
    """
    BasePage().connect_airtest()

