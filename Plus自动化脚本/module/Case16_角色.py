from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('角色')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''验证搜索框'''
        length1 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div'))
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[1]/search-box/div[1]/input', '员\n')
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[1]/search-box/div[1]/i[1]')
        sleep(2)
        length3 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div'))

        self.assertNotEqual(length1, length2, '搜索功能失效')
        self.assertEqual(length1, length3, '取消搜索按钮失效')

    def test_02(self):
        '''添加角色验证F'''
        length1 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/button')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div/div/span')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div[2]/button')
        sleep(2)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[1]/input', 'test')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[2]/textarea', 'test1')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div/label[2]/input')
        sleep(2)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/label/input')
        sleep(1)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/label/input')
        sleep(1)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div').text

        flag = 0
        if text1 != text2 or text1 != text3:
            flag = 1
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[4]/div[2]/div[1]/div/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[5]/button[1]')  # 保存
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div'))

        self.assertNotEqual(length1, length2, '无法正常新增角色')
        self.assertNotEqual(flag, 0, '新增角色-权限的选中情况无法实时更新')

    def test_03(self):
        '''更多-编辑按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/a').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/div/div/button[1]')  # 编辑
        sleep(2)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[1]/input', '1')
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[5]/button[1]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/a').text

        self.assertNotEqual(text1, text2, '编辑功能异常')

    def test_04(self):
        '''更多-查看人员列表页面验证F'''
        length1 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/div/div/button[3]')  # 查看人员列表
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div/div[2]/button')  # 选择用户
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-body > div.classify-part > div.user-all > div.other-item > div:nth-child(1) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-body > div.classify-part > div.user-all > div.other-item > div:nth-child(2) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-body > div.classify-part > div.user-all > div.other-item > div:nth-child(3) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-footer > button.btn.primary-btn').click()
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div'))

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div/div[2]/button')  # 选择用户
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-body > div.classify-part > div.user-all > div.other-item > div:nth-child(1) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-body > div.classify-part > div.user-all > div.other-item > div:nth-child(2) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.user-modal.in > div > div > user-chose > div > div.modal-footer > button.btn.primary-btn').click()
        sleep(3)
        length3 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div'))

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div[1]/div[8]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div[1]/div[8]/div/div/div/button[2]')  # 删除
        sleep(2)
        length4 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div'))

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.fc('#view > ui-view > div > div > div.box > div > div.list.white > div.list_bottom.white.hoge-table-bottom > div.btn-toolbar.list_bar.flex-one.btn-box > div:nth-child(3) > button').click()
        sleep(2)
        length5 = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div'))

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div/div[1]/span')  # 返回
        sleep(3)

        self.assertNotEqual(length1, length2, '添加用户失败')
        self.assertNotEqual(length3, length4, '更多-删除按钮失效')
        self.assertNotEqual(length4, length5, '底部删除按钮失效')
        self.assertNotEqual(length2, length3, '选择用户页面取消用户无法正常删除用户')

    def test_05(self):
        '''删除按钮验证'''
        length1 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/div/div/button[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(1)
        length = len(self.plus.finds('/html/body/div[2]/div/div/div/span'))

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/div/div/button[3]')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[3]/div[2]/div[2]/div[3]/button')  # 删除
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div/div[1]/span')  # 返回
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div[1]/div[5]/div/div/div/button[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        length2 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div/div[3]/div')

        self.assertEqual(length, 1, '角色有用户时删除缺少提示')
        self.assertNotEqual(length1, length2, '删除角色功能异常')
