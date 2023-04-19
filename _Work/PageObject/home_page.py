# 首页
from time import sleep
from selenium.webdriver.common.by import By
from _Work.Common.base_page import basePage
from _Work.PageObject.topBar import topBar
from _Work.PageObject.bottomBar import bottomBar


class homePage(basePage):
    bookImg = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/dl/dd[1]/a/img')
    bookSwitch = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/div/ul/li[2]/img')
    book1 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/dl[1]/dd[1]/a[1]')
    book2 = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/dl[2]/dd[1]/a[1]')
    notice = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/dl[3]/dd[1]/a')

    benzhouqiangtui_book1 = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/a')
    benzhouqiangtui_book2 = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/ul/li[2]/div[1]/a')

    rementuijian_book1 = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/h4/a')
    rementuijian_book2 = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[5]/div/h4/a')

    dianjibangdan_book1 = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[2]/ul/li[1]/div[1]/a')
    dianjibangdan_book2 = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[2]/ul/li[9]/div[1]/a')
    dianjibangdan_more = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[2]/div/a')

    jingpingtuijian_book1 = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/div/h4/a')
    jingpingtuijian_book2 = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[5]/div/h4/a')

    xinshubangdan_book1 = (By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[1]/div[1]/a')
    xinshubangdan_book2 = (By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div[2]/ul/li[8]/div[1]/a')
    xinshubangdan_more = (By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div[2]/div/a')

    zuixingengxin_leibie1 = (By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a')
    zuixingengxin_leibie2 = (By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[2]/table/tbody/tr[5]/td[1]/a')
    zuixingengxin_bookname1 = (By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a')
    zuixingengxin_bookname2 = (By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[2]/table/tbody/tr[5]/td[2]/a')
    zuixingengxin_chapter1 = (By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[2]/table/tbody/tr[1]/td[3]/a')
    zuixingengxin_chapter2 = (By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[2]/table/tbody/tr[5]/td[3]/a')

    gengxinbangdan_book1 = (By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div[2]/ul/li[1]/div[1]/a')
    gengxinbangdan_book2 = (By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div[2]/ul/li[6]/div[1]/a')
    gengxinbangdan_more = (By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div[2]/div/a')

    searchResults = (By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr')

    def book_click(self):
        self.click(homePage.book1)
        sleep(2)

    def register_click(self):
        self.click(topBar.register_button)
        sleep(2)

    def login_click(self):
        self.click(topBar.login_button)
        sleep(2)

    def myShelf_click(self):
        self.click(topBar.myBookshelf)
        sleep(2)

    def mine_click(self):
        self.click(topBar.mine_button)
        sleep(2)

    def logout_click(self):
        self.click(topBar.logout_button)
        sleep(2)

    def goto_shouye(self):
        self.click(topBar.shouye)
        sleep(2)

    def goto_quanbuzuopin(self):
        self.click(topBar.quanbuzuopin)
        sleep(2)

    def goto_paihangbang(self):
        self.click(topBar.paihangbang)
        sleep(2)

    def goto_chongzhi(self):
        self.click(topBar.chongzhi)
        sleep(2)

    def goto_zuojiazhuanqu(self):
        self.click(topBar.zuojiazhuanqu)
        self.switchHandler(1)
        sleep(2)

    def logo_click(self):
        self.click(topBar.logo)
        sleep(2)
        lens = self.getLens(self.bookImg)
        assert lens == 1, '点击logo首页跳转失败'

    def do_search(self):
        self.send_key(topBar.search_input, '你')
        self.click(topBar.search_button)
        sleep(3)
        lens = self.getLens(self.searchResults)
        for i in range(lens):
            text = self.getText((By.XPATH, f'/html/body/div[2]/div[2]/div/table/tbody/tr[{i + 1}]/td[3]/a'))
            assert '你' in text, '搜索结果异常'

    # 底部
    def viewSwitch_click(self):
        self.click(bottomBar.shoujizhan)
        sleep(2)

    def home_click(self):
        self.click(bottomBar.wangzhanshouye)
        sleep(2)

    def about_click(self):
        self.click(bottomBar.guanyuwomen)
        sleep(2)

    def contact_click(self):
        self.click(bottomBar.lianxiwomen)
        sleep(2)

    def leaveMessage_click(self):
        self.click(bottomBar.fankuiliuyan)
        sleep(2)

    def author_click(self):
        self.click(bottomBar.zuojiazhuanqu)
        sleep(2)

    def client_click(self):
        self.click(bottomBar.kehuduan)
        sleep(2)
