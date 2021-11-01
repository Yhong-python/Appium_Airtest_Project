#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: basepage.py
@time: 2021/10/15 14:27
@desc:
"""

import os
import threading
import time

import airtest.core.api as air_test
import allure
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from common.log import logger


class BasePage:
    _instance_lock = threading.Lock()
    driver = None
    timeout = 10
    air_test = None

    def __new__(cls, *args, **kwargs):
        # 可被继承的单例类
        if not hasattr(cls, "instance_dict"):
            cls.instance_dict = {}
        if str(cls) not in cls.instance_dict.keys():
            with cls._instance_lock:
                _instance = super().__new__(cls)
                cls.instance_dict[str(cls)] = _instance
        return cls.instance_dict[str(cls)]

    @classmethod
    def set_driver(cls, driver: WebDriver) -> WebDriver:
        cls.driver = driver
        return cls.driver

    @property
    def get_phone_size(self):
        """获取屏幕的大小"""
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def agree_authority(self):
        locator = ('xpath', '//*[@text="始终允许"]')
        element = self.find_element(locator)
        if element:
            self.element_click(locator)

    @staticmethod
    def get_element_size_location(element):
        width = element.rect["width"]
        height = element.rect["height"]
        start_x = element.rect["x"]
        start_y = element.rect["y"]
        return width, height, start_x, start_y

    def swipe_left(self, duration=300):
        """左滑"""
        width, height = self.get_phone_size
        start = width * 0.9, height * 0.5
        end = width * 0.1, height * 0.5
        return self.driver.swipe(*start, *end, duration)

    def swipe_right(self, duration=300):
        """右滑"""
        width, height = self.get_phone_size
        start = width * 0.1, height * 0.5
        end = width * 0.9, height * 0.5
        return self.driver.swipe(*start, *end, duration)

    def swipe_up(self, duration=300):
        """上滑"""
        width, height = self.get_phone_size
        start = width * 0.5, height * 0.9
        end = width * 0.5, height * 0.1
        return self.driver.swipe(*start, *end, duration)

    def swipe_down(self, duration=300):
        """下滑"""
        width, height = self.get_phone_size
        start = width * 0.5, height * 0.1
        end = width * 0.5, height * 0.9
        return self.driver.swipe(*start, *end, duration)

    def skip_welcome_page(self, direction, duration=300, num=3):
        """
        滑动页面跳过引导动画
        :param direction:  str 滑动方向，left, right, up, down
        :param duration:  滑动持续时间
        :param num: 滑动次数
        :return:
        """
        direction_dic = {
            "left": "swipe_left",
            "right": "swipe_right",
            "up": "swipe_up",
            "down": "swipe_down"
        }
        import time
        time.sleep(3)
        if hasattr(self, direction_dic[direction]):
            for _ in range(num):
                getattr(self, direction_dic[direction])(duration)  # 使用反射执行不同的滑动方法
        else:
            raise ValueError("参数{}不存在, direction可以为{}任意一个字符串".
                             format(direction, direction_dic.keys()))

    @classmethod
    def select_locate_method(cls, method, element, is_elements=0):
        if not is_elements:
            if method == "id":  # resource-id定位
                return cls.driver.find_element_by_id(element)
            elif method == 'content-desc':  # 以accessibility_id进行定位，对Android而言，就是content-description属性
                return cls.driver.find_element_by_accessibility_id(element)
            elif method == 'classname':  # className定位
                return cls.driver.find_element_by_class_name(element)
            elif method == 'xpath':
                return cls.driver.find_element_by_xpath(element)
            else:
                pass
        else:
            if method == "id":  # resource-id定位
                return cls.driver.find_elements_by_id(element)
            elif method == 'content-desc':  # 以accessibility_id进行定位，对Android而言，就是content-description属性
                return cls.driver.find_elements_by_accessibility_id(element)
            elif method == 'classname':  # className定位
                return cls.driver.find_elements_by_class_name(element)
            elif method == 'xpath':
                return cls.driver.find_elements_by_xpath(element)
            else:
                raise KeyError(f'暂只支持id,content-desc,classname,xpath定位。当前选择的定位方式为：{method}')

    def find_element(self, locator: tuple, is_elements=0, poll_frequency=0.5):
        """
        use: find_element(locator=("id","id_value"))
        :param locator:  元组形式，如("id","id_value")
        :param is_elements:  是否为一组元素，默认为0，定位单个元素
        :param poll_frequency:
        :return:
        """
        if len(locator) != 2:
            logger.error("元素数据有误:{}".format(tuple))
            return None
        by, element = locator
        message = f"element:({by},{element}) not found in {self.timeout} seconds"
        try:
            element_result = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=poll_frequency).until(
                lambda x: self.select_locate_method(method=by, element=element, is_elements=is_elements),
                message=message)
            return element_result
        except (NoSuchElementException, TimeoutException) as e:
            logger.error(e)
            raise

    def _get_element(self, locator: tuple or WebElement, is_elements=0, element_index=0, poll_frequency=0.5):
        element = None
        if isinstance(locator, WebElement):
            element = locator
        elif isinstance(locator, tuple):
            if not is_elements:  # 定位单个元素时
                element = self.find_element(locator, is_elements, poll_frequency)
            else:  # 定位一组元素，返回指定下标的元素
                element = self.find_element(locator, is_elements, poll_frequency)[element_index]
        return element

    def element_click(self, locator: tuple or WebElement, is_elements=0, element_index=0, poll_frequency=0.5):
        """
        use: 定位的元素为单一元素：element_click(locator=("id","id_value"))
        :param locator:
        :param is_elements:是否为一组元素
        :param element_index:元素下标
        :param poll_frequency:
        """
        pic = self.driver.get_screenshot_as_png()
        allure.attach(pic, f'截图：定位元素：{locator}', allure.attachment_type.PNG)
        self._get_element(locator, is_elements, element_index, poll_frequency).click()
        time.sleep(0.8)

    def element_input(self, locator: tuple or WebElement, input_value, is_elements=0, element_index=0,
                      poll_frequency=0.5):
        """
        use: 定位的元素为单一元素：element_input(locator=("id","id_value"))
        :param locator:
        :param input_value:输入内容
        :param is_elements:是否为一组元素
        :param element_index:元素下标
        :param poll_frequency:
        """
        element = self._get_element(locator, is_elements, element_index, poll_frequency)
        element.click()
        time.sleep(0.1)
        element.clear()
        time.sleep(0.1)
        element.send_keys(input_value)
        time.sleep(0.5)
        pic = self.driver.get_screenshot_as_png()
        allure.attach(pic, f'截图：定位元素：{locator}', allure.attachment_type.PNG)

    def upload_album_picture(self, locator: tuple, pic_index=0, is_elements=0, element_index=0):
        """
        图片上传方法，以华为手机UI为例
        :param is_elements:
        :param element_index:
        :param locator: 需要上传图片的元素定位
        :param pic_index: 被上传图片在相册中的下标，从0开始，左往右递加
        """
        # 先点击需要上传图片的元素
        self.element_click(locator, is_elements, element_index)
        # 在选择拍照和打开相册弹框中选择打开相册并点击
        open_album_locator = ("xpath", "//android.widget.TextView[@text='打开相册']")
        self.element_click(open_album_locator)
        # 在相册选择图片并勾选
        select_pic_locator = ("id", "com.door.qp.hjproject:id/check_view")  # 这里点位的是选择图片的圆圈
        self.element_click(select_pic_locator, is_elements=1, element_index=pic_index)
        time.sleep(0.8)
        pic = self.driver.get_screenshot_as_png()
        allure.attach(pic, f'截图：定位元素：{locator}', allure.attachment_type.PNG)
        # 点击确定图片按钮
        confirm_button_locator = ("xpath", "//*[contains(@text,'确定')]")
        confirm_button_element = self.find_element(confirm_button_locator)
        if confirm_button_element.is_enabled():  # 判断确定按钮enabled的状态
            confirm_button_element.click()
        else:
            logger.error("上传图片时未选中图片")
            raise Exception("图片上传异常")
        time.sleep(5)
        pic = self.driver.get_screenshot_as_png()
        allure.attach(pic, f'截图：定位元素：{locator}', allure.attachment_type.PNG)

    def quit(self):
        self.driver.quit()

    # 以下为airtest相关操作封装
    @classmethod
    @allure.step("初始化连接airtest")
    def connect_airtest(cls, device_info="Android:///7XBRX18A16002686?cap_method=javacap&touch_method=adb"):
        """
        :param device_info: Android:///7XBRX18A16002686?cap_method=javacap&touch_method=adb
        :return: 返回重新命名后的airtest包
        """
        cls.air_test = air_test
        # 连接方式一，用init_device()
        # cls.air_test.init_device(platform="Android",uuid="7XBRX18A16002686")
        # 连接方式二，用connect_device()
        cls.air_test.connect_device(device_info)
        # 连接方式三，用auto_setup()
        # cls.air_test.auto_setup(__file__,devices=["Android://127.0.0.1:5037/7XBRX18A16002686"])
        return cls.air_test

    @classmethod
    @allure.step("adb输入{text}")
    def adb_input_text(cls, text):
        return os.system("adb shell input text {}".format(text))

    @classmethod
    def adb_input_keyevent(cls, keyevent):
        return os.system("adb shell input keyevent {}".format(keyevent))

    def airtest_click(self, pic_path, times=1):
        """
        airtest的点击方法
        :param pic_path: 需要图片的绝对路径
        :param times: 点击次数
        """
        import time
        time.sleep(0.5)
        self.air_test.touch(self.air_test.Template(pic_path, target_pos=5), times=times)


if __name__ == '__main__':
    pass
