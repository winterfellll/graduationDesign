from selenium import webdriver

from POM.PageObject.main_page import mainPage
from time import sleep


class Test():
    def test_01(self, driver):
        a = mainPage(driver)
        a.click()
        sleep(2)
