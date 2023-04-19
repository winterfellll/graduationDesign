# 排行榜
from time import sleep
from selenium.webdriver.common.by import By
from _Work.Common.base_page import basePage


class rankingPage(basePage):
    rankingMethod1 = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[1]/a')
    rankingMethod2 = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[2]/a')
    rankingMethod3 = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[3]/a')
    rankingMethod4 = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[4]/a')

    def getBookList(self):
        bookList = []
        for i in range(30):
            text = self.getText((By.XPATH, f'/html/body/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[{i + 1}]'))
            bookList.append(text)
        return bookList

    def rankingMethodSwitch(self):
        list1 = self.getBookList()
        self.click(self.rankingMethod2)
        sleep(2)
        list2 = self.getBookList()
        assert list1 != list2, '排行榜按钮切换异常'

        list1 = self.getBookList()
        self.click(self.rankingMethod3)
        sleep(2)
        list2 = self.getBookList()
        assert list1 != list2, '排行榜按钮切换异常'

        list1 = self.getBookList()
        self.click(self.rankingMethod4)
        sleep(2)
        list2 = self.getBookList()
        assert list1 != list2, '排行榜按钮切换异常'

        list1 = self.getBookList()
        self.click(self.rankingMethod1)
        sleep(2)
        list2 = self.getBookList()
        assert list1 != list2, '排行榜按钮切换异常'
