from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import pytest

driver = webdriver.Chrome()
driver.get('http://mail.163.com')
sleep(2)
driver.switch_to.window(2)
ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input')
sleep(5)

import logging
from time import sleep

import pytest


# 　打印日志级别
def logging1():
    logging.basicConfig(level=logging.ERROR)
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')


logging1()
