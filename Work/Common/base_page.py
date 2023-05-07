import logging
from time import sleep


class basePage():
    def __init__(self, driver):
        self.driver = driver

    def locator(self, args):
        ele = self.driver.find_element(*args)
        logging.info(f"元素定位 元素文本：{ele.text}  元素定位方式：{args}")
        self.driver.execute_script("arguments[0].style.border='2px solid red'", ele)
        return ele

    def send_key(self, args, keyword):
        logging.info(f"输入{keyword}")
        self.locator(args).send_keys(keyword)

    def click(self, args, time=1):
        logging.info("点击")
        self.locator(args).click()
        sleep(time)

    def back(self):
        self.driver.back()

    def switchWindow(self, i):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[i])

    def getCurrentURL(self):
        return self.driver.current_url

    def getLens(self, args):
        elements = self.driver.find_elements(*args)
        return len(elements)

    def getText(self, args):
        return self.locator(args).text
