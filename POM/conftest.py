from time import sleep

from selenium.webdriver.common.by import By

PRPORE_SCREEN_DIR = 'Users/hoge/downloads'
import os
import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='module', autouse=True)
def driver():
    # global driver
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(5)
    # return driver

    global driver
    driver = webdriver.Chrome()
    driver.get('http://demo-xingyun.hogeos.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/form/div[2]/div/input').send_keys('liujifeng')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/form/div[3]/div/div/input').send_keys('ljfHoge@2022\n')
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div/div[3]/div[1]/div/img').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    sleep(5)
    return driver


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # 以下为实现异常截图的代码：
    # rep.when可选参数有call、setup、teardown，
    # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
    # 这里只针对用例执行且失败的用例进行异常截图
    if rep.when == "call" and rep.failed:
        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

        # mode = "a" if os.path.exists("failures") else "w"
        # with open("failures", mode) as f:
        #     if "tmpdir" in item.fixturenames:
        #         extra = " (%s) " % item.funcargs["tmpdir"]
        #     else:
        #         extra = ""
        #     f.write(rep.nodeid + extra + "\n")
        # item.name = item.name.encode("utf-8").decode("unicode-escape")
        #
        # file_name = '{}.png'.format(str(round(time.time() * 1000)))
        # path = os.path.join(PRPORE_SCREEN_DIR, file_name)
        #
        # driver.save_screenshot(path)
        # if hasattr(driver, "get_screenshot_as_png"):
        #     with allure.step("添加失败截图"):
        #         # get_screenshot_as_png实现截图并生成二进制数据
        #         # allure.attach直接将截图二进制数据附加到allure报告中
        #         allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
