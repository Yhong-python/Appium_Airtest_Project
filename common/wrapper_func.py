#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: wrapper_func.py
@time: 2021/10/12 16:54
@desc:装饰器定义
"""

import json
import time
from functools import wraps

from common.log import logger


def wrapper_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 把参数以x=1这种形式打印在日志里
        kwargs_string = ''
        for k, v in kwargs.items():
            temp = str(k) + '=' + json.dumps(v)
            kwargs_string += temp + ' '
        start_time = time.time()
        logger.info("== method [%s] input kwargs: %s" % (func.__name__, kwargs_string))
        result = func(*args, **kwargs)
        logger.info("== [%s] run time is %.3f ms ==" % (func.__name__, (time.time() - start_time) * 1000))
        logger.info("== method [%s] return: %s ==" % (func.__name__, result))
        return result
    return wrapper
