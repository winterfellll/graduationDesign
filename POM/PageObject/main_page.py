from selenium.webdriver.common.by import By
from selenium import webdriver
from POM.BasePage.base_page import basePage
from time import sleep


class mainPage(basePage):
    video = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/d1iv[1]/div[2]/ul[1]/li[6]/a')

    def click(self):
        self.find(self.video).click()
