import os
import unittest
from time import strftime
from XTestRunner import HTMLTestRunner
from module.Case01_文稿 import test

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([test('test_13'), test('test_14'), test('test_15'), test('test_16')])

    test_dir = './module'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
    now = strftime("%m-%d %H:%M:%S")
    filename = './reports/' + now + '.html'
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='自动化测试报告', description='自动化测试报告')
        runner.run(discover)  # 传参discover则执行module下所有用例，传参suite则执行配置的用例
