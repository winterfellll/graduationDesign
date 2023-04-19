import unittest
from time import strftime
from UIAutomator2 import Test
from XTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTests([Test('test_18'), Test('test_19'), Test('test_20')])

    suite = unittest.makeSuite(Test)
    now = strftime("%m-%d %H:%M:%S")
    filename = './reports/' + now + '.html'
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='自动化测试报告', description='自动化测试报告')
        runner.run(suite)

