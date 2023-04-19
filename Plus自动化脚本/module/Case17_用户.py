from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('用户')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''用户-分类管理跳转'''
        ele = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(ele).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')
        text = self.plus.find('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]').text
        self.assertNotEqual(text, None, '分类为空')

    def test_02(self):
        '''用户-分类管理功能验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[1]/div[2]/span')
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', '测试分类' + str(random.randint(0, 100)))
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[2]/div[1]/div[2]/span')
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[2]')
        sleep(3)
        ele = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        before = ele[-1].text
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[3]/i[1]')  # 编辑按钮
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', Keys.BACK_SPACE)
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(3)
        after = ele[-1].text

        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div'))
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[3]/i[2]')  # 删除按钮
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')  # 确认删除
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div'))

        self.assertNotEqual(before, after, '用户架构修改失败')
        self.assertNotEqual(length1, length2, '用户架构删除失败')

    def test_03(self):
        '''左侧分类验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        sleep(3)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/classify-sidebar/div/div[2]/div/div[2]/div/div')
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/classify-sidebar/div/div[1]/span')
        sleep(2)

        self.assertNotEqual(length1, length2, '左侧分类按钮失效')

    def test_04(self):
        '''筛选框和搜索框验证'''
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[1]/div/button')  # 筛选框
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/a[3]')
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[1]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/a[1]')

        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[1]/search-box/div[1]/input', 'hoge\n')  # 输入框
        sleep(2)
        length3 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[1]/search-box/div[1]/i[1]')  # 取消搜索按钮
        sleep(2)
        length4 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div'))

        self.assertNotEqual(length1, length2, '筛选框失效')
        self.assertNotEqual(length1, length3, '搜索框失效')
        self.assertEqual(length1, length4, '取消搜索按钮失效')

    def test_05(self):
        '''导入用户验证'''
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        flag = 0
        for i in range(1, 11):
            text = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[{i}]/div[2]/div[2]/span').text
            if text == '示例账户':
                flag = 1

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[1]/div[2]/button[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button')  # 下载模版
        sleep(2)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        if flag == 0:  # 确保账户未重复
            self.plus.send_key('/html/body/div/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div/div[2]/input', user_import_path)
            sleep(1)
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[4]/button[1]')
            sleep(2)
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[4]/button[3]')  # 确定导入
            sleep(5)
            text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
            self.assertNotEqual(text1, text2, '导入功能失效')
        else:
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[1]/div/div/span')
            sleep(2)

        self.assertNotEqual(file1, file2, '下载模版按钮失效')
        self.assertNotEqual(flag, 1, '有重复账户，重试')

    def test_06(self):
        '''添加用户验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[1]/div[2]/button[2]')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[1]/div[2]/div[1]/input', 'name')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[1]/div[2]/div[2]/input', 'name')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[1]/div[2]/div[3]/div/label[6]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[1]/div[2]/div[4]/div/div/div')
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.departments-Column.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide.swiper-slide-active > div > div:nth-child(2) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.departments-Column.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-binding.ng-isolate-scope').click()
        sleep(1)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[2]/div[2]/div[1]/input', 'Hogepassword1')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[2]/div[2]/div[4]/input', '13277191919')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[4]/button[1]')  # 保存
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text

        self.assertNotEqual(text1, text2, '添加用户失败')

    def test_07(self):
        '''更多按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[8]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[8]/div/div/div/button[1]')  # 编辑
        sleep(1)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[1]/div[2]/div[1]/input', '1')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/form/div[4]/button[1]')
        sleep(5)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/span').text

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[7]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[8]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[8]/div/div/div/button[4]')  # 锁定
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[7]/span').text

        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[8]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[8]/div/div/div/button[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text

        self.assertNotEqual(text1, text2, '编辑功能失效')
        self.assertNotEqual(text3, text4, '锁定功能失效')
        self.assertNotEqual(text5, text6, '删除功能失效')

    def test_08(self):
        '''底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/div[2]/div[1]/button')  # 解锁
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[7]/span').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/div[2]/div[2]/button')  # 锁定
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[7]/span').text

        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/div[2]/div[4]/button')  # 导出
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/div[2]/div[3]/button')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div/div[2]/div/div[3]/div[11]/page-nation/div/span').text

        self.assertEqual(text1, '正常', '底部解锁按钮失效')
        self.assertEqual(text2, '已锁定', '底部锁定按钮失效')
        self.assertNotEqual(file1, file2, '底部导出按钮失效')
        self.assertNotEqual(text3, text4, '底部删除按钮失效')
