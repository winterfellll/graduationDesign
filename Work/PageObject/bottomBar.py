from selenium.webdriver.common.by import By
from Work.Common.base_page import basePage


class bottomBar(basePage):
    shoujizhan = (By.XPATH, '/html/body/div[4]/div/div/ul/li[1]/a[1]')
    wangzhanshouye = (By.XPATH, '/html/body/div[4]/div/div/ul/li[1]/a[2]')
    guanyuwomen = (By.XPATH, '/html/body/div[4]/div/div/ul/li[1]/a[3]')
    lianxiwomen = (By.XPATH, '/html/body/div[4]/div/div/ul/li[1]/a[4]')
    fankuiliuyan = (By.CSS_SELECTOR, "[href='/user/feedback.html']")
    zuojiazhuanqu = (By.XPATH, '/html/body/div[4]/div/div/ul/li[1]/a[6]')
    kehuduan = (By.XPATH, '/html/body/div[4]/div/div/ul/li[1]/a[7]')
