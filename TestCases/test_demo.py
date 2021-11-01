#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: test_demo.py
@time: 2021/10/12 17:00
@desc:
'''
from pageObject.welcomepage import WelcomePage
from pageObject.mainpage import MainPage
from pageObject.mycustompage import MyPage
from pageObject.businesspage import BusinessPage

import time
import allure

# class TestDemo():
#     @allure.story("已注册账号登录")
#     @allure.description("账号密码正确")
#     def test_1(self,connect_airtest):
#         page=WelcomePage()
#         page.click_skip_button()
#         page.swipe_left_3_times()
#         page.click_start_use()
#         page.select_protocol()
#         page.click_agree_button()
#         page.input_userinfo()
    # time.sleep(30)
# def test_2():
    # mp=MainPage()
    # my=MyPage()
    # mp.cilck_my_custom()
    # time.sleep(1)
    # my.swipe_down_common()
    # time.sleep(1)
    # my.jietu('1.png')
# def test_3():
#     mp=MainPage()
#     mp.cilck_my_work_table()
#     mp.click_diya()
#     my=MyPage()
#     my.swipe_down_common()
#     my.jietu('2.png')
# page.driver.start_activity('com.door.qp.hjproject','com.qp.LaunchActivity')
    # page.click_skip_button()

# def test_4():
#     mp=MainPage()
#     mp.cilck_my_custom()
#     my=MyPage()
#     time.sleep(1)
#     my.swipe_down_common()
#     time.sleep(1)
#     my.jietu('1.png')

def test_5():
    w=WelcomePage()
    w.click_skip_button()
    m=MainPage()
    m.click_bussiness()
    b=BusinessPage()
    b.click_first_order()
    b.click_custom_info_tab()
    b.click_custom_info()
    b.sfz_front_upload()
    b.sfz_back_upload()
