# basePage.py代码如下
# _*_ coding:utf-8 _*_

import sys


# pages基类
class Page(object):
    def __init__(self, driver, base_url=u"http://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title
