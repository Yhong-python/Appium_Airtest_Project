#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: log.py
@time: 2021/7/16 13:56
@desc:
"""
import os
import time
import sys
from loguru import logger
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(project_path, 'log')
t = time.strftime("%Y-%m-%d")


# class PropogateHandler(logging.Handler):
#     def emit(self, record):
#         logger.info(record.name)
#         logging.getLogger(record.name).handle(record)


class Loggings:
    """日志定义"""
    __instance = None

    logger.add(f"{log_path}/ui_log_{t}.log", rotation="100MB", encoding="utf-8", enqueue=True,
               retention="10 days", backtrace=False)
    # 让日志在allure报告中的log中展示，否则展示在stderr中
    # logger.add(PropogateHandler())

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


loggings = Loggings()
if __name__ == '__main__':
    logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    n1 = "cool"
    n2 = [1, 2, 3]
    logger.info(f'If you are using Python {n1}, prefer {n2} of course!')
    logger.info('345345345345345')
    try:
        1 / 0
    except Exception as e:
        logger.error(e)
