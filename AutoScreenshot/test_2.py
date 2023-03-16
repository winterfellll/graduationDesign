import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def test_01(self, driver):
        text = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a').text
        assert text == '文稿'
