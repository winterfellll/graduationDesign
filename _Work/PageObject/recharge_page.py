# 充值
from selenium.webdriver.common.by import By
from _Work.Common.base_page import basePage
from time import sleep


class rechargePage(basePage):
    rechargeMethod1 = (By.XPATH, '/html/body/form/div/div/div/div[2]/ul[1]/li[1]/img')
    rechargeMethod2 = (By.XPATH, '/html/body/form/div/div/div/div[2]/ul[1]/li[2]/img')
    money1 = (By.XPATH, '/html/body/form/div/div/div/div[2]/ul[2]/li[1]')
    money2 = (By.XPATH, '/html/body/form/div/div/div/div[2]/ul[2]/li[4]')
    message = (By.XPATH, '/html/body/form/div/div/div/div[3]/ul/li[4]/a')  # 底部留言
    confirmButton = (By.CSS_SELECTOR, '.layui-layer-btn0')
    alipay = (By.CSS_SELECTOR, 'body > div.topbar > div > span')

    def rechargeMethodSwitch(self):
        self.click(self.rechargeMethod2)
        sleep(1)
        lens = self.getLens(self.confirmButton)
        if lens == 1:
            self.click(self.confirmButton)
            sleep(1)
        assert lens == 1, '微信支付异常'

    def recharge(self):
        self.click(self.money1)
        sleep(3)
        lens = self.getLens(self.alipay)
        if lens == 1:
            self.back()
            sleep(3)
        assert lens == 1, '支付跳转失败'

    def leave_message(self):
        self.click(self.message)
        sleep(1)
        self.switchHandler(1)
        url = self.getCurrentURL()
        assert url == 'http://novel.hctestedu.com/user/feedback.html', '充值页面反馈留言跳转失败'
