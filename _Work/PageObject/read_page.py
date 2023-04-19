# 阅读
from time import sleep
from selenium.webdriver.common.by import By
from _Work.Common.base_page import basePage


class readPage(basePage):
    leftButton = (By.CSS_SELECTOR, '#showDetail > div.readBody.cf > div > div.read_menu > div.menu_left')
