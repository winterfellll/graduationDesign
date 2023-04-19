# 注册
import os
from selenium.webdriver.common.by import By
from Work.Common.base_page import basePage
from Work.PageObject.topBar import topBar
import ddddocr
from faker import Faker
from time import sleep


class registerPage(basePage):
    username = (By.XPATH, '//*[@id="txtUName"]')
    password = (By.XPATH, '//*[@id="txtPassword"]')
    codeInput = (By.XPATH, '//*[@id="TxtChkCode"]')
    codeImg = (By.XPATH, '//*[@id="chkd"]')
    registerButton = (By.XPATH, '//*[@id="btnRegister"]')
    loginButton = (By.XPATH, '/html/body/div[2]/div/div/a')

    def do_register(self):
        fake = Faker('zh_CN')
        phone = fake.phone_number()
        imgelement = self.locator(self.codeImg)
        imgelement.screenshot('captcha.jpg')
        ocr = ddddocr.DdddOcr()
        with open('captcha.jpg', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        os.remove('captcha.jpg')

        self.send_key(self.username, phone)
        self.send_key(self.password, 'admin123')
        self.send_key(self.codeInput, res)
        sleep(2)
        self.click(self.registerButton)
        sleep(3)

        text = self.getText(topBar.login_button)
        assert '登录' != text, '注册成功'
