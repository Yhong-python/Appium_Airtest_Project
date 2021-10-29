#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: mainpage.py
@time: 2021/10/27 13:57
@desc:
"""
import time

import allure

from pageObject.basepage import BasePage


class MainPage(BasePage):
    @allure.step("点击我的客户Tab")
    def cilck_my_custom(self):
        locator=("xpath","//android.view.View[@text='我的客户']")
        self.element_click(locator,is_elements=1,element_index=0)

    @allure.step("点击工作台Tab")
    def cilck_my_work_table(self):
        locator=("xpath","//android.view.View[@text='工作台']")
        self.element_click(locator,is_elements=1,element_index=0)
    @allure.step("点击抵押审核Tab")
    def click_diya(self):
        locator = ('xpath', '//android.view.View[@text="抵押审核"]')
        self.element_click(locator)

    @allure.step("点击第一个代办业务")
    def click_bussiness(self):
        locator = ('xpath', '//android.view.View[contains(@text,"汽车担保流")]')
        self.element_click(locator)