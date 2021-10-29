#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: welcomepage.py
@time: 2021/10/21 14:40
@desc:
'''
import time

import allure

from pageObject.basepage import BasePage


class WelcomePage(BasePage):

    @allure.step("点击跳过按钮")
    def click_skip_button(self):
        locator = ('id', 'com.door.qp.hjproject:id/iv_jump')
        self.element_click(locator)

    @allure.step("向左滑动引导页3次")
    def swipe_left_3_times(self):
        self.skip_welcome_page(direction='left', num=3)

    @allure.step("点击立即使用按钮")
    def click_start_use(self):
        # 立即使用元素定位
        element1 = ('id', 'com.door.qp.hjproject:id/guide_ib_start')
        self.element_click(element1)

        # 权限设置
        with allure.step("点击权限确认按钮"):
            self.agree_authority()

        time.sleep(2)
        # 2次滑动到协议底部
        with allure.step("向下滑动2次页面到底部"):
            for i in range(2):
                self.swipe_up()
                time.sleep(0.5)

    @allure.step("点击勾选服务协议")
    def select_protocol(self):
        # 用airtest来定位同意协议
        self.airtest_click(r"E:\UI_Auto\airtest图片库\服务协议勾选.png")

    @allure.step("点击同意协议按钮")
    def click_agree_button(self):
        # 用airtest来定位按钮
        self.airtest_click(r"E:\UI_Auto\airtest图片库\服务协议同意按钮.png")

    def input_userinfo(self):
        elements = self.find_element(("classname", 'android.widget.EditText'), is_elements=1)
        username, pwd = elements[0], elements[1]
        with allure.step("账号输入框输入"):
            self.element_input(username, '19999999999')
        self.element_click(pwd)
        self.adb_input_text("999999")

        # self.element_input(pwd,'999999')
        # self.element_click(("classname",'android.widget.EditText'),1,2)
        # import time
        # username.clear()
        # time.sleep(0.1)
        # username.send_keys('19999999999')
        # time.sleep(0.1)
        # pwd.send_keys('999999')

