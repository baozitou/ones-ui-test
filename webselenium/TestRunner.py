# coding=utf-8
from BeautifulReport import BeautifulReport
from htmlTestRunner import ClassicHTMLTestRunner
from config import settings
import unittest
import time


# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

if __name__ =='__main__':
    # 开始执行测试套件
    suite = unittest.defaultTestLoader.discover(settings.CASE_PATH,pattern='test*.py')
    # file_name = now+".html"
    # runner = BeautifulReport(suite)
    # runner.report(description="test_scan", filename=file_name, report_dir=settings.REPORT_PATH)
    # runner = unittest.TextTestRunner()
    runner = unittest.TextTestRunner()
    runner.run(suite)

