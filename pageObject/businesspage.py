#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: businesspage.py
@time: 2021/10/28 13:40
@desc:
"""
import allure
import time
from pageObject.basepage import BasePage
class BusinessPage(BasePage):
    @allure.step("点击第一个订单")
    def click_first_order(self):
        locator=("xpath","//android.view.View[@text='16171831538348487']")
        self.element_click(locator)
    @allure.step("点击客户信息tab页")
    def click_custom_info_tab(self):
        locator=("xpath","//android.view.View[@text='客户信息']")
        self.element_click(locator)
    @allure.step("点击主借人信息")
    def click_custom_info(self):
        locator=("xpath","//android.widget.Button[contains(@text,'身份证')]")
        self.element_click(locator)
        time.sleep(1)
    @allure.step("身份证正面上传,取相册第一张")
    def sfz_front_upload(self):
        locator=("classname","android.view.View")
        self.upload_album_picture(locator,0,1,6)
    @allure.step("身份证反面上传,取相册第二张")
    def sfz_back_upload(self):
        locator=("classname","android.view.View")
        self.upload_album_picture(locator,1,1,14)

        # //android.view.View[@text="保存"]