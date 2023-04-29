class basePage():
    def __init__(self, driver):
        self.driver = driver

    def locator(self, args):
        ele = self.driver.find_element(*args)
        self.driver.execute_script("arguments[0].style.border='2px solid red'", ele)
        return ele

    def send_key(self, args, keyword):
        self.locator(args).send_keys(keyword)

    def click(self, args):
        self.locator(args).click()

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
