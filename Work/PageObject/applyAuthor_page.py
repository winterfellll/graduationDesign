# 作家专区
from time import sleep
from selenium.webdriver.common.by import By
from Work.Common.base_page import basePage


class applyAuthorPage(basePage):
    inviteCode = (By.XPATH, '//*[@id="TxtGetCode"]')
    nickName = (By.XPATH, '//*[@id="TxtNiceName"]')
    mobile = (By.XPATH, '//*[@id="TxtMobile"]')
    QQ = (By.XPATH, '//*[@id="TxtQQ"]')
    mail = (By.XPATH, '//*[@id="TxtEmail"]')
    direction1 = (By.XPATH, '/html/body/div[1]/form/div/table/tbody/tr[7]/td[2]/div/ul/a[1]')
    direction2 = (By.XPATH, '/html/body/div[1]/form/div/table/tbody/tr[7]/td[2]/div/ul/a[2]')
    start = (By.XPATH, '//*[@id="btnSubmit"]')
    errorMessage = (By.XPATH, '//*[@id="LabErr"]')

    def applyToAuthor(self):
        self.send_key(self.inviteCode, '123456')
        self.send_key(self.nickName, 'gabbiii')
        self.send_key(self.mobile, '13212344321')
        self.send_key(self.QQ, '2312750867')
        self.send_key(self.mail, '2312750867@qq.com')
        self.click(self.direction1)
        self.click(self.start)
        sleep(2)
        text = self.getText(self.errorMessage)
        assert '邀请码无效' in text, '申请成为作者失败'
