from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    '''2F'''

    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('审稿')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''左侧分类验证F'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/classify-sidebar/div/div[2]/div/div[1]/div/div')
        sleep(3)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/classify-sidebar/div/div[1]/span')
        sleep(2)

        self.assertNotEqual(before1, after1, '左侧分类按钮切换失败')

    def test_02(self):
        '''排序按钮、筛选框、搜索框验证'''
        self.plus.tishen()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/button[2]')  # 创建时间按钮
        sleep(2)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/button[2]')  # 创建时间按钮
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/button[1]')  # 最新提审按钮
        sleep(2)

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/button')  # 审核筛选框
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/a[2]')  # 我已审核
        sleep(2)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/a[1]')
        sleep(2)

        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/button')  # 级别筛选框
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/div/a[4]')  # 3级审核
        sleep(2)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/div/a[1]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[5]/button')  # 类型筛选框
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[5]/div/div/div/div/div[7]/a')  # 军事政法
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[5]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[5]/div/div/div/div/div[1]/a')
        sleep(2)

        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/search-box/div[1]/input', 'test\n')  # 搜索框
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/search-box/div[1]/i[1]')  # 取消搜索按钮
        sleep(2)

        self.assertNotEqual(text1, text2, '创建时间排序按钮失效')
        self.assertNotEqual(text3, text4, '审核筛选框失效')
        self.assertNotEqual(length, length1, '级别筛选框失效')
        self.assertNotEqual(length, length2, '类型筛选框失效')

    def test_03(self):
        '''稿件点击验证F'''
        text1 = self.plus.fc(".pull-pages").text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div[1]')
        sleep(2)
        length = len(self.plus.finds('/html/body/div[5]/div/div/div/span'))
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.showPreviews.in > div > div > div > div.review-info-op.hoge-flex.hoge-flex-center.ng-scope > div.audit-op-wrap.hoge-flex.hoge-flex-center > button.btn.del-btn.comment-btn-dahui.ng-scope').click()  # 打回
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        text3 = self.plus.fc('body > div.modal.fade.ng-isolate-scope.showPreviews.in > div > div > div > div.review-info-op.hoge-flex.hoge-flex-center.ng-scope > div.audit-op-wrap.hoge-flex.hoge-flex-center > div > span').text
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.showPreviews.in > div > div > div > div.modal-header > div.close > span').click()  # 退出预览
        sleep(1)
        text2 = self.plus.fc(".pull-pages").text

        self.plus.tishen()

        self.assertEqual(text3, '已打回', '预览-打回按钮失效')
        self.assertNotEqual(text1, text2, '预览-打回按钮失效')
        self.assertNotEqual(length, 1, '审稿预览功能失效')

    def test_04(self):
        '''右侧按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[7]/span[3]')  # 编辑按钮
        sleep(5)
        self.plus.click("//span[@class='return-tip']")  # 返回
        sleep(3)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]').text

        text2 = self.plus.fc(".pull-pages").text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[7]/span[2]')  # 打回
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(3)
        text3 = self.plus.fc(".pull-pages").text

        self.plus.tishen()

        text4 = self.plus.fc(".pull-pages").text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[7]/span[1]')  # 审核
        sleep(2)
        text5 = self.plus.fc(".pull-pages").text

        self.assertNotEqual(text2, text3, '打回按钮失效')
        self.assertNotEqual(text4, text5, '审核按钮失效')
        self.assertEqual(text1, '审稿', '点击编辑按钮返回后 左上方模块名称有误')

    def test_05(self):
        '''底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '文稿').click()
        sleep(5)
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[9]')
        sleep(3)

        self.plus.tishen()

        text1 = self.plus.fc(".pull-pages").text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[1]/label/input')
        self.plus.fc('#view > ui-view > div > div > div.second-view > div > div > div.row-col > div > div > div > div.list_bottom > div.btn-toolbar.list_bar.flex-one.btn-box > div:nth-child(2) > button').click()  # 打回
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        text2 = self.plus.fc(".pull-pages").text

        self.plus.tishen()

        text3 = self.plus.fc(".pull-pages").text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[1]/label/input')
        self.plus.fc('#view > ui-view > div > div > div.second-view > div > div > div.row-col > div > div > div > div.list_bottom > div.btn-toolbar.list_bar.flex-one.btn-box > div:nth-child(1) > button').click()  # 审核
        sleep(2)
        text4 = self.plus.fc(".pull-pages").text

        self.assertNotEqual(text1, text2, '打回按钮失效')
        self.assertNotEqual(text3, text4, '审核按钮失效')

    def test_06(self):
        '''流程配置-左侧分类验证'''
        ele = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(ele).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')  # 流程配置
        sleep(3)

        length1 = self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[3]/div/span/span')
        sleep(2)
        length2 = self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[1]/span')
        sleep(2)

        self.assertNotEqual(length1, length2, '左侧分类按钮失效')

    def test_07(self):
        '''流程配置-筛选、排序按钮验证'''
        length1 = self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[1]/button[3]')
        sleep(2)
        length2 = self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[1]/button[1]')
        sleep(2)

        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/span')  # 排序按钮
        ele = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]')
        ac(self.plus.driver).drag_and_drop_by_offset(ele, 0, 200).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[3]/button[1]')  # 取消
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/span')  # 排序按钮
        ele = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]')
        ac(self.plus.driver).drag_and_drop_by_offset(ele, 0, 200).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[3]/button[2]')  # 保存
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]').text

        self.assertNotEqual(length1, length2, '筛选按钮失效')
        self.assertEqual(text1, text2, '取消按钮失效')
        self.assertNotEqual(text1, text3, '排序功能失效')

    def test_08(self):
        '''新增流程验证'''
        length1 = self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/button')  # 新增流程
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[1]/div/span')  # 返回
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/button')  # 新增流程
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/button[2]')  # 取消
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/button')  # 新增流程
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/div[1]/i')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/div[1]/input', 'test')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/span[2]')
        sleep(3)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-body > div.classify-part > div.user-all > div.other-item > div:nth-child(1) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-footer > button.btn.primary-btn').click()
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/button[1]')
        sleep(3)
        length2 = self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div')

        self.assertNotEqual(length1, length2, '新增按钮失效')

    def test_09(self):
        '''更多按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div/button[1]')  # 编辑
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/div[1]/i')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/div[1]/input', '1')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/button[1]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]').text

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/span[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div/button[2]')  # 停用
        sleep(2)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/span[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div/button[2]')
        sleep(2)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/span[1]').text

        length1 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div/button[3]')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div'))

        self.assertNotEqual(text1, text2, '编辑按钮失效')
        self.assertNotEqual(text3, text4, '停用按钮失效')
        self.assertNotEqual(text5, text4, '启用按钮失效')
        self.assertNotEqual(length1, length2, '删除按钮失效')
