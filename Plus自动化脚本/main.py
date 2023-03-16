import os
import unittest
from time import strftime
from XTestRunner import HTMLTestRunner

if __name__ == '__main__':
    loader = unittest.TestLoader()
    test_dir = './module'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
    now = strftime("%m-%d %H:%M:%S")
    filename = './reports/' + now + '.html'
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='自动化测试报告', description='自动化测试报告')
        runner.run(discover)
    if not os.path.getsize(filename):
        os.remove(filename)

    # runner = unittest.TextTestRunner()
    # runner.run(discover)
