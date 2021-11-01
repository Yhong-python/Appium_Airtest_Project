#!/usr/bin/env python
# encoding: utf-8
"""
@author: yanghong
@file: file_utils.py
@time: 2021/11/1 11:53
@desc:
"""
import json
import os

from ruamel import yaml


class FileUtils(object):
    @staticmethod
    def read_yaml(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read().strip()
            content = yaml.load(stream=content, Loader=yaml.SafeLoader)
            return content
        else:
            raise Exception(f"{file_path}文件不存在")

    @staticmethod
    def update_yaml(file_path, content):
        if os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                yaml.dump(content, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)
        else:
            raise Exception(f"{file_path}文件不存在")

    @staticmethod
    def read_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
            return content
        else:
            raise FileNotFoundError(f"{file_path}文件不存在")

    @staticmethod
    def update_json(file_path, content):
        if os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False)
        else:
            raise FileNotFoundError(f"{file_path}文件不存在")


if __name__ == '__main__':
    # print(FileUtils.read_yaml("E:\\UI_Auto\\config\\desired_caps.yml"))
    pass
