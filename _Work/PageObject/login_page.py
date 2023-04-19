# 登录
from time import sleep
from selenium.webdriver.common.by import By
from _Work.Common.base_page import basePage
from _Work.PageObject.topBar import topBar
from _Work.Common.read_file import username, password


class loginPage(basePage):
    username = (By.XPATH, '//*[@id="txtUName"]')
    password = (By.XPATH, '//*[@id="txtPassword"]')
    autoLogin = (By.XPATH, '//*[@id="autoLogin"]')
    loginButton = (By.XPATH, '//*[@id="btnLogin"]')
    registerButton = (By.XPATH, '/html/body/div[2]/div/div[2]/a')

    def do_login(self):
        self.send_key(self.username, username)
        self.send_key(self.password, password)
        sleep(1)
        self.click(self.loginButton)
        sleep(2)

        text = self.getText(topBar.login_button)
        assert '登录' != text, '登录成功'
