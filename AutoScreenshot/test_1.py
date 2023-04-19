import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def test_01(self, driver):
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a').click()

    def test_02(self, driver):
        text = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[2]').text
        print(text)
