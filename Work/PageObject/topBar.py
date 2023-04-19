from time import sleep

from selenium.webdriver.common.by import By
from Work.Common.base_page import basePage


class topBar(basePage):
    logo = (By.XPATH, '/html/body/div[1]/div[2]/div/a/img')
    login_button = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/span/a[1]')
    register_button = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/span/a[2]')
    search_input = (By.XPATH, '//*[@id="searchKey"]')
    search_button = (By.XPATH, '//*[@id="btnSearch"]')
    myBookshelf = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/a')
    # 登录后出现我的和退出按钮
    mine_button = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/span/a[1]')
    logout_button = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/span/a[2]')

    shouye = (By.XPATH, '/html/body/div[1]/div[3]/div/ul/li[1]/a')
    quanbuzuopin = (By.XPATH, '/html/body/div[1]/div[3]/div/ul/li[2]/a')
    paihangbang = (By.XPATH, '/html/body/div[1]/div[3]/div/ul/li[3]/a')
    chongzhi = (By.XPATH, '/html/body/div[1]/div[3]/div/ul/li[4]/a')
    zuojiazhuanqu = (By.XPATH, '/html/body/div[1]/div[3]/div/ul/li[5]/a')
