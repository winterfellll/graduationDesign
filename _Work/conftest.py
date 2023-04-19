from time import sleep
import os
import allure
import pytest
from selenium import webdriver
from _Work.Common.read_file import browser, url


@pytest.fixture(scope='module', autouse=True)
def driver():
    global driver
    if browser == 'Chrome' or browser == 'chrome':
        driver = webdriver.Chrome()
    if browser == 'Firefox' or browser == 'firefox':
        driver = webdriver.Firefox()
    if browser == 'Edge' or browser == 'edge':
        driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    sleep(3)
    return driver


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # rep.when可选参数有call、setup、teardown， call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    if rep.when == "call" and rep.failed:
        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
