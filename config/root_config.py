#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: root_config.py
@time: 2021/7/1 13:43
@desc:
"""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(ROOT_DIR, "log")
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
DEVICE_INFO_PATH = os.path.join(CONFIG_DIR, "desired_caps.yml")
APPIUM_LOG_PATH = os.path.join(ROOT_DIR, "log")
