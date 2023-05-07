# 全部作品
from selenium.webdriver.common.by import By
from Work.Common.base_page import basePage


class allbooksPage(basePage):
    book_channel1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[1]/a[1]')
    book_channel2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[1]/a[2]')
    book_classification1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[3]/a[1]')
    book_classification2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[3]/a[2]')
    book_classification3 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[3]/a[3]')
    book_classification4 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[3]/a[4]')
    book_classification5 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[3]/a[5]')
    book_classification6 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[3]/a[6]')
    book_classification_female1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[2]/a[1]')
    book_classification_female2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[2]/a[2]')
    book_classification_female3 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/span[2]/a[3]')
    book_isend1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[3]/a[1]')
    book_isend2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[3]/a[2]')
    book_isend3 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[3]/a[3]')
    book_wordnum1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[4]/a[1]')
    book_wordnum2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[4]/a[2]')
    book_wordnum3 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[4]/a[3]')
    book_wordnum4 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[4]/a[4]')
    book_wordnum5 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[4]/a[5]')
    update_time1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[5]/a[1]')
    update_time2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[5]/a[2]')
    update_time3 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[5]/a[3]')
    update_time4 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[5]/a[4]')
    update_time5 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[5]/a[5]')
    sort_order1 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[6]/a[1]')
    sort_order2 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[6]/a[2]')
    sort_order3 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[6]/a[3]')
    sort_order4 = (By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[6]/a[4]')

    previousPage = (By.CSS_SELECTOR, '.layui-laypage-prev')
    nextPage = (By.XPATH, '.layui-laypage-next')
    firstPageButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/a[2]')
    secondPageButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/a[3]')
    thirdPageButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/a[4]')
    fourthPageButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/a[5]')
    fifthPageButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/a[6]')
    sixthPageButton = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div/a[7]')

    book1_classification = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a')
    book1_name = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/a')
    book1_chapter = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/a')
    book1_author = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/a')

    book8_classification = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[8]/td[2]/a')
    book8_name = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[8]/td[3]/a')
    book8_chapter = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[8]/td[4]/a')
    book8_author = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[8]/td[5]/a')

    def getWordNumList(self):
        wordNumList = []
        n = self.getLens((By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr'))
        for i in range(n):
            text = self.getText((By.XPATH, f'/html/body/div[2]/div[2]/div/table/tbody/tr[{i + 1}]/td[6]'))
            num = float(text.split('万')[0])
            wordNumList.append(num)
        return wordNumList

    def getBookList(self):
        bookList = []
        n = self.getLens((By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr'))
        for i in range(n):
            text = self.getText((By.XPATH, f'/html/body/div[2]/div[2]/div/table/tbody/tr[{i + 1}]/td[3]'))
            bookList.append(text)
        return bookList
