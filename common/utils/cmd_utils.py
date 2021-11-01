#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: appium_serve.py
@time: 2021/10/27 15:00
@desc:
"""
import os
import socket
import subprocess
import time

from common.log import logger
from config.root_config import APPIUM_LOG_PATH


class AppiumServe(object):
    @staticmethod
    def check_port(host, port):
        """检测指定的端口是否被占用"""
        # 创建socket对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.shutdown(2)
        except OSError:
            # print('port %s is available! ' % port)
            logger.info('port %s is available! ' % port)
            return True
        except Exception as e:
            logger.error(e)
            raise
        else:
            # print('port %s already be in use !' % port)
            logger.warning('port %s already be in use ! please release it' % port)
            return False

    @staticmethod
    def release_port(port):
        # 查看端口对应的pid的命令
        cmd_find = 'netstat -aon | findstr {}'.format(port)

        # 返回命令执行后的结果
        result = os.popen(cmd_find).read().strip()
        # TCP    127.0.0.1:4723         0.0.0.0:0              LISTENING       276
        if str(port) in result and "LISTENING" in result:
            # 取LISTENING+7个空格之后的值就是pid
            index = result.index("LISTENING") + len("LISTENING") + 7
            pid = result[index:]

            # 关闭被占用端口的pid
            cmd_kill = "taskkill -f -pid %s" % pid
            os.popen(cmd_kill)
            logger.info('port %s was released' % port)
        else:
            # print('port %s is available !' % port)
            logger.info('port %s is not used !' % port)
        logger.info('appium serve start success,listen port at %s' % port)

    @staticmethod
    def start_appium_server(ip='127.0.0.1', port=4723, bport=62001):
        appium_log_name = "appium_log_" + time.strftime("%Y_%m_%d") + ".log"
        appium_log_path = os.path.join(APPIUM_LOG_PATH, appium_log_name)
        if not os.path.exists(appium_log_path):
            with open(appium_log_path, 'w')as f:
                f.close()
        cmd = f"start appium -a {ip} -p {port} -bp {bport} --local-timezone --log={appium_log_path}"
        # print('%s at %s' % (cmd, time.ctime()))
        logger.info('run {%s} command at %s' % (cmd, time.ctime()))
        if not AppiumServe.check_port(ip, port):
            AppiumServe.release_port(port)
            time.sleep(2)
        subprocess.Popen(cmd, shell=True)
