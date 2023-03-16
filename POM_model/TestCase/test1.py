import time

from selenium import webdriver

from POM_model.PageObject.main_page import SearchPage


class Test():
    def test_01(self):
        driver = webdriver.Chrome()
        SearchPage(driver).gotoBaiduHomePage()
        time.sleep(2)
