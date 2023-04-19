from time import sleep

from selenium.webdriver.common.by import By

PRPORE_SCREEN_DIR = 'Users/hoge/downloads'
import os
import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='module', autouse=True)
def driver():
    global driver
    driver = webdriver.Chrome()
    driver.get('http://demo-xingyun.hogeos.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/form/div[2]/div/input').send_keys('liujifeng')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/form/div[3]/div/div/input').send_keys('ljfHoge@2022\n')
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div/div[2]/div[1]/div/img').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    sleep(5)
    return driver


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # rep.when可选参数有call、setup、teardown， call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    if rep.when == "call" and rep.failed:
        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
