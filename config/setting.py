#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
DATA_DIR = 'D:\先临三维\项目\云平台\APIDiff'

# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR, "ApiData", "config.ini")
# 测试用例模板文件
# SOURCE_FILE = os.path.join(BASE_DIR,"ApiData","DemoAPITestCase.xlsx")
SOURCE_FILE = os.path.join(DATA_DIR, "ApiData", "cloudAPIdental.xlsx")
# SOURCE_FILE_dental = os.path.join(DATA_DIR,"ApiData","cloudAPIdental.xlsx")
# excel测试用例结果文件
TARGET_FILE = os.path.join(DATA_DIR, "report", "excelReport", "cloudAPIdental_result.xlsx")
# TARGET_FILE_dental = os.path.join(BASE_DIR,"report","excelReport","cloudAPIdental.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR, "testcase")
