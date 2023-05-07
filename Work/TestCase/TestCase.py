import logging

import pytest

from Work.PageObject.home_page import homePage
from Work.PageObject.allworks_page import allbooksPage
from Work.PageObject.applyAuthor_page import applyAuthorPage
from Work.PageObject.bottomBar import bottomBar
from Work.PageObject.login_page import loginPage
from Work.PageObject.ranking_page import rankingPage
from Work.PageObject.recharge_page import rechargePage
from Work.PageObject.register_page import registerPage
from Work.PageObject.topBar import topBar
from Work.PageObject.detail_page import detailPage
from time import sleep
import allure
from Work.Common.read_file import url


@allure.feature('未登录时进入各页面的测试')
class Test_not_login():
    @allure.title('未登录时进入书架')
    def test_01(self, driver):
        homePage(driver).myShelf_click()
        url = driver.current_url
        assert 'login' in url, '未登录时进入书架未跳转到登录页面'

    @allure.title('未登录时进入充值模块')
    def test_02(self, driver):
        homePage(driver).goto_chongzhi()
        url = driver.current_url
        assert 'login' in url, '未登录时进入充值未跳转到登录页面'

    @allure.title('未登录时进入作家专区模块')
    def test_03(self, driver):
        homePage(driver).goto_zuojiazhuanqu()
        url = driver.current_url
        assert 'login' in url, '未登录时进入作家专区未跳转到登录页面'

    @allure.title('未登录时点击加入书架')
    def test_04(self, driver, myurl=url):
        driver.get(myurl)
        homePage(driver).book_click()
        detailPage(driver).addToBookShelf()
        url = driver.current_url
        assert 'login' in url, '未登录时点击加入书架未跳转到登录页面'

    @allure.title('未登录时点击反馈留言')
    def test_05(self, driver):
        homePage(driver).leaveMessage_click()
        url = driver.current_url
        assert 'login' in url, '未登录时点击反馈留言未跳转到登录页面'


@allure.feature('首页各功能验证')
class Test_shouye():
    books = [homePage.bookImg, homePage.book1, homePage.book2, homePage.benzhouqiangtui_book1, homePage.benzhouqiangtui_book2, homePage.rementuijian_book1, homePage.rementuijian_book2, homePage.dianjibangdan_book1, homePage.dianjibangdan_book2, homePage.jingpingtuijian_book1,
             homePage.xinshubangdan_book1, homePage.zuixingengxin_bookname1, homePage.gengxinbangdan_book1]
    more_buttons = [homePage.dianjibangdan_more, homePage.gengxinbangdan_more, homePage.xinshubangdan_more]

    @allure.title('点击左上角logo')
    def test_01(self, driver):
        homePage(driver).goto_paihangbang()
        homePage(driver).logo_click()

    @allure.title('搜索')
    def test_02(self, driver):
        homePage(driver).do_search()

    @allure.title('注册')
    def test_03(self, driver):
        homePage(driver).register_click()
        registerPage(driver).do_register()

    @allure.title('退出登录')
    def test_04(self, driver):
        homePage(driver).logout_click()
        text = homePage(driver).getText(topBar.login_button)
        assert text == '登录', '退出登录失败'

    @allure.title('登录')
    def test_05(self, driver):
        homePage(driver).login_click()
        loginPage(driver).do_login()

    @allure.title('点击首页书籍')
    @pytest.mark.parametrize('ele', books)
    def test_06(self, driver, ele):
        homePage(driver).click(ele)
        sleep(1)
        url = homePage(driver).getCurrentURL()
        driver.back()
        sleep(1)
        assert 'book' in url, '首页书籍封面点击跳转失败'

    @allure.title('点击首页更多按钮')
    @pytest.mark.parametrize('ele', more_buttons)
    def test_07(self, driver, ele):
        homePage(driver).click(ele)
        sleep(1)
        url = homePage(driver).getCurrentURL()
        driver.back()
        sleep(1)
        assert 'book_ranking' not in url, '首页“查看更多”按钮点击跳转失败'

    @allure.title('点击下方最新更新中的类别')
    def test_08(self, driver):
        homePage(driver).click(homePage.zuixingengxin_leibie1)
        sleep(1)
        url = homePage(driver).getCurrentURL()
        driver.back()
        sleep(1)
        assert 'bookclass' in url, '首页最新更新中的类别点击后跳转失败'

    @allure.title('点击下方最新更新中的章节')
    def test_09(self, driver):
        homePage(driver).click(homePage.zuixingengxin_chapter1)
        sleep(1)
        url = homePage(driver).getCurrentURL()
        driver.back()
        sleep(1)
        assert 'indexList' in url, '首页最新更新中的章节点击后跳转异常'


@allure.feature('全部作品各功能验证')
class Test_quanbuzuopin():
    classifications = [allbooksPage.book_classification6, allbooksPage.book_classification2, allbooksPage.book_classification3, allbooksPage.book_classification4, allbooksPage.book_classification5]

    @pytest.fixture(scope='class', autouse=True)
    def setup(self, driver):
        homePage(driver).goto_quanbuzuopin()

    @allure.title('点击作品分类')
    @pytest.mark.parametrize('ele', classifications)
    def test_01(self, driver, ele):
        text1 = allbooksPage(driver).getText(ele)
        allbooksPage(driver).click(ele)
        sleep(2)
        text2 = allbooksPage(driver).getText(allbooksPage.book1_classification)
        driver.refresh()
        sleep(2)
        assert text1 in text2, '按作品分类筛选失败'

    @allure.title('点击是否完结')
    def test_02(self, driver):
        list1 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.book_isend2)
        list2 = allbooksPage(driver).getBookList()
        assert list1 != list2, '点击连载中切换失败'
        allbooksPage(driver).click(allbooksPage.book_isend3)
        list3 = allbooksPage(driver).getBookList()
        driver.refresh()
        sleep(2)
        assert list2 != list3, '点击已完结切换失败'

    @allure.title('点击作品字数')
    def test_03(self, driver):
        allbooksPage(driver).click(allbooksPage.book_wordnum2)
        list1 = allbooksPage(driver).getWordNumList()
        for i in list1:
            assert i <= 30, '点击30万字以下，筛选失败'

        allbooksPage(driver).click(allbooksPage.book_wordnum3)
        list2 = allbooksPage(driver).getWordNumList()
        for i in list2:
            assert 30 < i <= 50, '点击30-50万字，筛选失败'

        allbooksPage(driver).click(allbooksPage.book_wordnum4)
        list3 = allbooksPage(driver).getWordNumList()
        for i in list3:
            assert 50 < i <= 100, '点击50-100万字，筛选失败'

        allbooksPage(driver).click(allbooksPage.book_wordnum5)
        list4 = allbooksPage(driver).getWordNumList()
        for i in list4:
            assert i >= 100, '点击100万字以上，筛选失败'
        driver.refresh()
        sleep(2)

    @allure.title('点击更新时间')
    def test_04(self, driver):
        list1 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.update_time2)
        list2 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.update_time3)
        list3 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.update_time4)
        list4 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.update_time5)
        list5 = allbooksPage(driver).getBookList()
        driver.refresh()
        sleep(2)

        assert list1 != list2, '点击三日内，筛选失败'
        assert list1 != list3, '点击七日内，筛选失败'
        assert list1 != list4, '点击半月内，筛选失败'
        assert list1 != list5, '点击一月内，筛选失败'

    @allure.title('按字数排序')
    def test_05(self, driver):
        allbooksPage(driver).click(allbooksPage.sort_order3)
        list = allbooksPage(driver).getWordNumList()
        for i in range(len(list) - 1):
            assert list[i] > list[i + 1], '按字数排序异常'
        driver.refresh()
        sleep(2)

    @allure.title('按更新时间、点击量排序')
    def test_06(self, driver):
        list1 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.sort_order2)
        list2 = allbooksPage(driver).getBookList()
        allbooksPage(driver).click(allbooksPage.sort_order4)
        list3 = allbooksPage(driver).getBookList()

        assert list1 == list2, '按更新时间排序异常'
        assert list1 == list3, '按点击量排序异常'

    @allure.title('点击书的类别')
    def test_07(self, driver):
        allbooksPage(driver).click(allbooksPage.book1_classification)
        url = allbooksPage(driver).getCurrentURL()
        assert 'c=' in url, '点击某书的类别，跳转失败'

    @allure.title('点击书的标题')
    def test_08(self, driver):
        text1 = allbooksPage(driver).getText(allbooksPage.book1_name)
        allbooksPage(driver).click(allbooksPage.book1_name)
        text2 = allbooksPage(driver).getText(detailPage.title)
        assert text1 == text2, '点击书的标题，跳转失败'


@allure.feature('排行榜各功能验证')
class Test_paihangbang():
    @allure.title('点击右侧排行榜按钮')
    def test_1(self):
        sleep(30)

    @allure.title('点击书籍的类别按钮')
    def test_2(self):
        sleep(30)

    @allure.title('点击书籍的标题')
    def test_3(self):
        sleep(30)

    @allure.title('点击书籍的章节')
    def test_4(self):
        sleep(30)

    @allure.title('点击书籍的作者')
    def test_5(self):
        sleep(30)

    @allure.title('点击书籍的作者')
    def test_6(self):
        sleep(30)

    @allure.title('点击书籍的类别按钮')
    def test_7(self):
        sleep(30)

    @allure.title('点击书籍的标题')
    def test_8(self):
        sleep(30)

    @allure.title('点击书籍的章节')
    def test_9(self):
        sleep(30)

    @allure.title('点击书籍的作者')
    def test_10(self):
        sleep(30)


@allure.feature('充值各功能验证')
class Test_chongzhi():
    @allure.title('点击作品分类')
    def test_1(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_2(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_3(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_4(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_5(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_6(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_7(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_8(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_9(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_10(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_11(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_12(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_13(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_14(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_15(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_16(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_17(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_18(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_19(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_20(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_21(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_22(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_23(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_24(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_25(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_26(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_27(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_28(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_29(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_30(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_31(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_32(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_33(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_34(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_35(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_36(self):
        sleep(30)
        assert 0 == 1, 'error'

    @allure.title('点击作品分类')
    def test_37(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_38(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_39(self):
        sleep(30)


@allure.feature('作家专区各功能验证')
class Test_zuojiazhuanqu():
    @allure.title('点击作品分类')
    def test_1(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_2(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_3(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_4(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_5(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_6(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_7(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_8(self):
        sleep(30)
        assert 0 == 1, 'error'

    @allure.title('点击作品分类')
    def test_9(self):
        sleep(30)
        assert 0 == 1, 'error'

    @allure.title('点击作品分类')
    def test_10(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_11(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_12(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_13(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_14(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_15(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_16(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_17(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_18(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_19(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_20(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_21(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_22(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_23(self):
        sleep(30)


@allure.feature('用户信息各功能验证')
class Test_yonghuxinxi():
    @allure.title('点击作品分类')
    def test_1(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_2(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_3(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_4(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_5(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_6(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_7(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_8(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_9(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_10(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_11(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_12(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_13(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_14(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_15(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_16(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_17(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_18(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_19(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_20(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_21(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_22(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_23(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_24(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_25(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_26(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_27(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_28(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_29(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_30(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_31(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_32(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_33(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_34(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_35(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_36(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_37(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_38(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_39(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_40(self):
        sleep(30)
        assert 0 == 1, 'error'

    @allure.title('点击作品分类')
    def test_41(self):
        sleep(30)

    @allure.title('点击作品分类')
    def test_42(self):
        sleep(30)


@allure.feature('书籍阅读页面各功能验证')
class Test_shujiyuedu():
    @allure.title('点击作品分类')
    def test_1(self):
        sleep(150)

    @allure.title('点击作品分类')
    def test_2(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_3(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_4(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_5(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_6(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_7(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_8(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_9(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_10(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_11(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_12(self):
        sleep(60)

    @allure.title('点击作品分类')
    def test_13(self):
        sleep(60)
