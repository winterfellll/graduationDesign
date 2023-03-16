# searchPage.py 代码如下
# _*_ coding:utf-8 _*_

import sys
from selenium.webdriver.common.by import By
from POM_model.BasePage.base_page import Page


# 百度搜索page
class SearchPage(Page):
    # 搜索输入框
    search_input = (By.ID, u'kw')
    # 百度一下 按钮
    search_button = (By.ID, u'su')

    def gotoBaiduHomePage(self):
        print(u"打开首页: ", self.base_url)
        self.driver.get(self.base_url)

    def input_search_text(self, text=u"百度测试"):
        print(u"输入搜索关键字：百度测试")
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        print(u"点击 百度一下  按钮")
        self.click(self.search_button)
