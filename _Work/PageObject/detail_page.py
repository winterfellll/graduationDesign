# 书籍详情
from time import sleep
from selenium.webdriver.common.by import By
from _Work.Common.base_page import basePage
from _Work.PageObject.read_page import readPage


class detailPage(basePage):
    crumb1 = (By.XPATH, '/html/body/div[2]/div[1]/a[1]')
    crumb2 = (By.XPATH, '/html/body/div[2]/div[1]/a[2]')
    crumb3 = (By.XPATH, '/html/body/div[2]/div[1]/a[3]')
    crumb4 = (By.XPATH, '/html/body/div[2]/div[1]/a[4]')
    title = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/h1')
    readButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/a')
    addToBookShelfButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/span/a')
    content = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div[1]/div/div/a')
    commentButton = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div[1]/a')
    allComment = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div[4]/a')
    commentInput = (By.XPATH, '//*[@id="txtComment"]')
    commentSubmit = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div[5]/div[2]/span[2]/a')

    def beginRead(self):
        self.click(self.readButton)
        sleep(2)
        lens = self.getLens(readPage.leftButton)
        assert lens == 1, '点击开始阅读按钮跳转失败'

    def addToBookShelf(self):
        self.click(self.addToBookShelfButton)
        sleep(1)

    def contentClick(self):
        self.click(self.content)
        sleep(2)
        lens = self.getLens(self.crumb4)
        assert lens == 1, '目录跳转异常'
