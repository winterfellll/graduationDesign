from selenium import webdriver


class basePage():
    def __init__(self, driver):
        self.driver = driver

    def find(self, args):
        return self.driver.find_element(*args)

    def send_key(self, args, keyword):
        self.find(args).send_keys(keyword)
