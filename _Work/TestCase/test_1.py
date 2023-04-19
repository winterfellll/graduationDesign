from _Work.PageObject.home_page import homePage
from _Work.PageObject.allworks_page import allbooksPage
from _Work.PageObject.applyAuthor_page import applyAuthorPage
from _Work.PageObject.bottomBar import bottomBar
from _Work.PageObject.login_page import loginPage
from _Work.PageObject.ranking_page import rankingPage
from _Work.PageObject.recharge_page import rechargePage
from _Work.PageObject.register_page import registerPage
from _Work.PageObject.topBar import topBar
from _Work.PageObject.detail_page import detailPage
from time import sleep
import allure
from _Work.Common.read_file import url


class Test():
    @allure.title('未登录时进入书架')
    def test_01(self, driver):
        homePage(driver).myShelf_click()
        url = driver.current_url
        assert 'login' not in url, '未登录时进入书架未跳转到登录页面'

    @allure.title('未登录时进入充值模块')
    def test_02(self, driver):
        homePage(driver).goto_chongzhi()
        url = driver.current_url
        assert 'login' in url, '未登录时进入充值未跳转到登录页面'

    # @allure.title('未登录时进入作家专区模块')
    # def test_03(self, driver):
    #     homePage(driver).goto_zuojiazhuanqu()
    #     url = driver.current_url
    #     assert 'login' in url, '未登录时进入作家专区未跳转到登录页面'
    #
    # @allure.title('未登录时点击加入书架')
    # def test_04(self, driver, myurl=url):
    #     driver.get(myurl)
    #     homePage(driver).book_click()
    #     detailPage(driver).addToBookShelf()
    #     url = driver.current_url
    #     assert 'login' in url, '未登录时点击加入书架未跳转到登录页面'
    #
    # @allure.title('未登录时点击反馈留言')
    # def test_05(self, driver):
    #     homePage(driver).leaveMessage_click()
    #     url = driver.current_url
    #     assert 'login' in url, '未登录时点击反馈留言未跳转到登录页面'
    #
    # @allure.title('点击左上角logo')
    # def test_06(self, driver):
    #     homePage(driver).goto_paihangbang()
    #     homePage(driver).logo_click()
    #
    # @allure.title('搜索')
    # def test_07(self, driver):
    #     homePage(driver).do_search()
    #
    # @allure.title('注册')
    # def test_08(self, driver):
    #     homePage(driver).register_click()
    #     registerPage(driver).do_register()
    #
    # @allure.title('退出登录')
    # def test_09(self, driver):
    #     homePage(driver).logout_click()
    #     text = homePage(driver).getText(topBar.login_button)
    #     assert text == '登录', '退出登录失败'
    #
    # @allure.title('登录')
    # def test_10(self, driver):
    #     homePage(driver).login_click()
    #     loginPage(driver).do_login()

    @allure.title('全部作品-按字数排序')
    def test_11(self, driver):
        homePage(driver).goto_quanbuzuopin()
        allbooksPage(driver).click(allbooksPage.sort_order3)
        sleep(2)
        list = allbooksPage(driver).getWordNumList()
        for i in range(len(list) - 1):
            assert list[i] > list[i + 1], '按字数排序异常'
