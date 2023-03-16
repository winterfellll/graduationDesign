import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver


class Test():
    def test_01(self, driver):
        text = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[112]/ul/li[7]/div/div[2]/div[4]/ul[1]/li[8]/a').text
        assert text == '1'
