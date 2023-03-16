from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('回收站')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''左侧分类按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[1]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div/div/div/div[3]/div')  # 图集
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[1]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div/div/div/div[7]/div')  # 外链
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[1]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div/div/div/div[2]/div')
        sleep(2)

        self.assertNotEqual(text1, text2, '左侧按钮失效')
        self.assertNotEqual(text3, text2, '左侧按钮失效')

    def test_02(self):
        '''搜索框、取消搜索按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[1]/search-box/div[1]/input', '123\n')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[1]/search-box/div[1]/i[1]')
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text

        self.assertNotEqual(text1, text2, '搜索框失效')
        self.assertEqual(text1, text3, '取消搜索按钮失效')

    def test_03(self):
        '''翻页按钮验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]').text

        self.assertNotEqual(before1, after1, '翻页按钮失效')

    def test_04(self):
        '''跳至输入框验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]').text
        self.plus.fc("[ng-model='vm.options.jump']").send_keys('1\n')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]').text
        self.assertNotEqual(text1, text2, '跳至输入框失效')

    def test_05(self):
        '''删除稿件进入回收站验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a')  # 文稿
        sleep(5)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text  # 稿件1
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[3]/div[2]/div[1]/a/span').text  # 稿件2
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        self.plus.driver.back()
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[1]/a/span').text
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/a/span').text

        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '外链').click()  # 外链
        sleep(5)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text  # 稿件1
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[3]/div[2]/div[1]/a/span').text  # 稿件2
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '回收站').click()  # 回收站
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div/div/div/div[7]/div')
        sleep(3)
        text7 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[1]/a/span').text
        text8 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/a/span').text

        self.assertEqual(text1, text3, '删除的稿件未进入回收站')
        self.assertEqual(text2, text4, '删除的稿件未进入回收站')
        self.assertEqual(text5, text7, '删除的稿件未进入回收站')
        self.assertEqual(text6, text8, '删除的稿件未进入回收站')

    def test_06(self):
        '''底部按钮验证'''
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        count1 = int(text.split('条')[0].split('共')[1])  # 稿件条数
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/div[2]/div/button[1]')  # 恢复
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        self.plus.driver.refresh()
        sleep(5)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        count2 = int(text.split('条')[0].split('共')[1])  # 稿件条数

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/div[2]/div/button[2]')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        self.plus.driver.refresh()
        sleep(5)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        count3 = int(text.split('条')[0].split('共')[1])  # 稿件条数

        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '外链').click()  # 外链
        sleep(4)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.assertEqual(text1, text2, '底部恢复按钮失效')
        self.assertEqual(count1, count2 + 1, '底部恢复按钮失效')
        self.assertEqual(count2, count3 + 1, '底部删除按钮失效')

    def test_07(self):
        '''更多按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '回收站').click()  # 回收站
        sleep(3)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[4]/div/div/div/button[1]')  # 还原
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[4]/div/div/div/button[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div'))

        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a')  # 文稿
        sleep(4)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text
        self.plus.driver.back()
        self.assertEqual(length1, 10, '更多-还原按钮失效')
        self.assertEqual(length2, 9, '更多-删除按钮失效')
        self.assertEqual(text1, text2, '更多-还原按钮失效')

    def test_08(self):
        '''操作后条数变化情况验证F'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/div[2]/div/button[2]')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(3)
        text2 = self.plus.find('/html/body/div/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[10]/page-nation/div/span').text
        self.plus.driver.refresh()
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text

        self.assertNotEqual(text2, text3, '操作并刷新后回收站-文稿条数仍未变化')
        self.assertNotEqual(text1, text2, '操作后回收站-文稿条数未变化')

    def test_09(self):
        '''操作后条数变化情况验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div/div/div/div[4]/div')
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/div[2]/div/button[1]')  # 恢复
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[10]/page-nation/div/span').text
        self.plus.driver.refresh()
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text

        self.assertNotEqual(text2, text3, '操作并刷新后回收站-视频条数仍未变化')
        self.assertNotEqual(text1, text2, '操作后回收站-视频条数未变化')
