#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: mycustompage.py
@time: 2021/10/27 14:01
@desc:
"""
import allure

from pageObject.basepage import BasePage


class MyPage(BasePage):
    def swipe_down_up(self):
        self.swipe_up()
    def get_screenshot(self,name):
        self.driver.get_screenshot_as_file(name)

