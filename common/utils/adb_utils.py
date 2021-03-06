#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: utils.py
@time: 2021/10/25 14:35
@desc:
"""
import os
import time

from common.log import logger


class AdbUtils(object):
    @staticmethod
    def adb_get_app_packagename_and_activity():
        """
        运行app后的第一时间执行
        :return:
        """
        # 下面两个命令都可以，适用于安卓8及以后的版本
        cmd = 'adb shell dumpsys window | findstr mCurrentFocus"'
        # cmd='adb shell dumpsys activity activities | findstr mResumedActivity'
        result = os.popen(cmd).read().strip()
        return result

    @staticmethod
    def is_app_insntall(app_package_name='com.door.qp.hjproject'):
        """
        判断是否安装目标app
        """
        # 只针对Android手机
        # 查看设备已安装的app包名
        app_package_list = os.popen('adb shell pm list packages -3').read().strip()
        # print(appPackageList)
        app_package = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'apk', 'app2.0.apk')
        # #判断是否已经安装,未安装则进行安装
        if app_package_name in app_package_list:
            # print('已安装')
            logger.info("com.door.qp.hjproject has been installed")
        else:
            # print('未安装')
            logger.info("com.door.qp.hjproject is not installed")
            # 安装app
            os.popen('adb install ' + app_package)
            # print('正在安装,请稍等')
            time.sleep(20)

    @staticmethod
    def adb_get_phone_size(devices_uuid='7XBRX18A16002686'):
        """
        查看屏幕分辨率
        :param devices_uuid:
        :return:
        """
        cmd = f'adb -s {devices_uuid} shell wm size'
        result = os.popen(cmd).read().strip()
        # print(result)
        return result

    @staticmethod
    def adb_get_phone_version(devices_uuid='7XBRX18A16002686'):
        """
        查看Android系统版本
        :param devices_uuid:
        :return:
        """
        cmd = f'adb -s {devices_uuid} shell getprop ro.build.version.release'
        result = os.popen(cmd).read().strip()
        # print(result)
        return result


if __name__ == '__main__':
    print(AdbUtils.adb_get_phone_size())
    print(AdbUtils.adb_get_phone_version())
    print(AdbUtils.adb_get_app_packagename_and_activity())
    pass
