from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    '''2F'''

    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('专题')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    # 分类管理
    def test_01(self):
        self.plus.category_1()

        self.assertNotEqual(self.plus.text, '', '分类为空')

    def test_02(self):
        self.plus.category_2()

        self.assertNotEqual(self.plus.before, self.plus.after, '修改失败')
        self.assertNotEqual(self.plus.length1, self.plus.length2, '删除成功')

    def test_03(self):
        '''专题页面分类按钮、筛选框、搜索框验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[3]/div/div[2]/div/div')
        sleep(3)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[1]/span')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[2]')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/button')  # 全部状态按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a[5]')
        sleep(2)
        after4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/button')  # 全部时间按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/div/a[2]')
        sleep(2)
        after5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/div/a[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/div[1]')
        self.plus.send_key('//*[@id="label-search-box"]', '123')
        sleep(2)

        elements1 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[3]/div/div')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[2]/input', '分类\n')  # 分类搜索框
        sleep(2)
        elements2 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[3]/div/div')

        self.assertNotEqual(before1, after1, '左侧分类按钮切换失败')
        self.assertNotEqual(before1, after2, '我的稿件按钮切换失败')
        self.assertNotEqual(before1, after4, '状态按钮切换失败')
        self.assertNotEqual(before1, after5, '时间按钮切换失败')
        self.assertNotEqual(len(elements1), len(elements2), '分类搜索框失效')

    def test_04(self):
        '''搜索功能验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/search-box/div[1]/input', '国家\n')  # 搜索框
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/search-box/div[1]/i[1]')
        sleep(3)
        after3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        before2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/span')  # 高级搜索按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button[1]')  # 重置按钮
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[1]/input').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[1]/input', '123')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[3]/input', 'author')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[7]/input', 'creator')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[5]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[5]/div/classify-preview/div/div[1]/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[9]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/classify-preview/div/div[2]/classify-box/div/div/ul/li[3]/div')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[4]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[4]/div/div/a[2]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[6]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[6]/div/div/a[2]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[8]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button[2]')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/span')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button[1]')  # 重置搜索
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button[2]')
        sleep(2)

        self.assertNotEqual(before1, after1, '搜索功能无法正常使用')
        self.assertNotEqual(before2, after2, '高级搜索功能无法正常使用')
        self.assertNotEqual(after3, after2, '叉号按钮失效')
        self.assertEqual(text, "", '重置按钮失效')

    def test_05(self):
        '''选中按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[1]/label/input')  # 全选按钮
        sleep(2)
        for i in range(1, 11):
            checked = [0] * 11
            checked[i] = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[' + str(i) + ']/div[1]/div[1]/label/input').get_attribute('checked')
            self.assertEqual(checked[i], 'true', '全选按钮失效')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        check1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input').get_attribute('checked')
        check2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[1]/label/input').get_attribute('checked')  # 全选按钮
        self.assertNotEqual(check2, 'true', '全选按钮失效')
        self.assertNotEqual(check1, 'true', '选择按钮失效')

    def test_06(self):
        '''翻页按钮验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/page-nation/div/div[2]/div[1]/button[4]')  # 翻页按钮
        sleep(3)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text

        self.assertNotEqual(before1, after1, '翻页按钮失效')
        self.assertNotEqual(after1, after2, '翻页按钮失效')

    def test_07(self):
        '''跳至输入框验证'''
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text
        self.plus.fc(
            '#view > ui-view > div > div.mxu_side_wrapper.mxu_content_wrapper.ng-scope > div.member-cont.second-view > div > div > div > div.hoge-flex > div > div.list.white.border-bottom-radius.ng-pristine.ng-untouched.ng-valid.ng-not-empty > div.list_bottom.hoge-table-bottom.border-bottom-radius > page-nation > div > div.list_page > div.goTo-group.btn-group > input').send_keys(
            '1\n')
        sleep(2)
        after3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text
        self.assertNotEqual(after3, after2, '跳至输入框失效')

    def test_08(self):
        '''每页条数按钮验证'''
        before2 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div')
        self.plus.fc(
            '#view > ui-view > div > div.mxu_side_wrapper.mxu_content_wrapper.ng-scope > div.member-cont.second-view > div > div > div > div.hoge-flex > div > div.list.white.border-bottom-radius.ng-pristine.ng-untouched.ng-valid.ng-not-empty > div.list_bottom.hoge-table-bottom.border-bottom-radius > page-nation > div > div.btn-group.dropdown.dropup > button').click()
        self.plus.fc(
            '#view > ui-view > div > div.mxu_side_wrapper.mxu_content_wrapper.ng-scope > div.member-cont.second-view > div > div > div > div.hoge-flex > div > div.list.white.border-bottom-radius.ng-pristine.ng-untouched.ng-valid.ng-not-empty > div.list_bottom.hoge-table-bottom.border-bottom-radius > page-nation > div > div.btn-group.dropdown.dropup.open > div > a:nth-child(2)').click()
        sleep(2)
        after4 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div')
        self.assertNotEqual(len(before2), len(after4), '每页条数按钮失效')

    def test_09(self):
        '''新增专题-返回按钮和取消按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button')
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/nav/div/div[1]/span')  # 返回按钮
        sleep(3)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[2]')  # 取消按钮
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span'))
        self.assertNotEqual(length1, 0, '返回按钮失效')
        self.assertNotEqual(length2, 0, '取消按钮失效')

    def test_10(self):
        '''新增专题-内部功能验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button')
        sleep(3)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[1]/div/textarea', '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/button[2]')  # 添加内容
        sleep(3)
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[3]/div[2]/div[5]/div/span')
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[3]/div[1]/div[5]/div/span')
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/div/div[1]/i')  # 叉号
        sleep(2)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div'))

        before1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[3]/div/span')  # 新增栏目
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div[1]/div/input', '1122')
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[1]')
        sleep(5)
        after1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div'))

        before2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[2]/li/div/span').text
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[2]/li/div/span')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[2]/li/div/i[1]')  # 编辑
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div[1]/div/input', '1')
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[1]')
        sleep(5)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[2]/li/div/span').text

        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[2]/li/div/span')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[2]/li/div/i[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        after = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[1]/div[1]/div/i')  # 排序
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[1]/div[2]/div/button[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[1]/div/nav/div/div[2]/div[1]/li/div/span/span')

        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/button[1]')  # 导出
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[3]/div')  # 更多按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[3]/div/div/div/button[2]')  # 置顶
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[3]/div')  # 更多按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div/div/button[3]')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(2)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div'))

        self.assertEqual(length, 2, '添加内容异常')
        self.assertNotEqual(before1, after1, '新增栏目异常')
        self.assertNotEqual(before2, after2, '修改栏目异常')
        self.assertNotEqual(after, after1, '删除栏目异常')
        self.assertNotEqual(file1, file2, '导出异常')
        self.assertNotEqual(text1, text2, '置顶异常')
        self.assertNotEqual(length1, 2, '删除按钮异常')

    def test_11(self):
        '''新增专题验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[1]/div/label[2]/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[1]/div/label[1]/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[2]/div/div/div/div[1]')
        sleep(3)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.cover-imgModel.in > div > div > div > div.modal-body > div:nth-child(1) > ul > li:nth-child(2) > span').click()  # 资源库
        self.plus.fc('#tab4 > div.hoge-table-bottom.ng-scope > page-nation > div > div.list_page > div:nth-child(1) > button:nth-child(5)').click()
        sleep(2)
        self.plus.fc('#tab4 > div.srcListNew.ng-isolate-scope > div:nth-child(5) > div > div.imgClassNew > div').click()
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.cover-imgModel.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-isolate-scope').click()  # 确定
        sleep(2)
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[2]/div/div/div/div[2]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[2]/div/div/div/div[5]')  # 编辑按钮
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.waterCoverModal.in > div > div > div > div.modal-footer.ng-isolate-scope > button.btn.primary-btn').click()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[2]/div/div/div/div[6]')  # 裁剪按钮
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.screen-shotModel.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-binding.ng-isolate-scope').click()
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[2]/div/div/div/div[4]')  # 删除按钮
        sleep(2)
        self.plus.fc('#coverImgs > div > div > div > div.add-img').click()
        sleep(2)
        self.plus.fc('#tab1 > div.upload-cover.ng-scope > div > input[type=file]').send_keys(picture_path)
        sleep(4)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.cover-imgModel.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[3]/div/div/div[1]/div/span')  # 主题色
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[3]/div/div/div[5]/div[12]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[4]/div/div/classify-preview/div/div[1]/div[1]')  # 分类
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[4]/div/div/classify-preview/div/div[2]/classify-box/div/div/ul/li[3]/div/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[6]/div/div/content-publish/div/div/div/div')  # 栏目
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.publishModal.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide.swiper-slide-active > div > div:nth-child(5) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.publishModal.in > div > div > div > div.modal-footer.flex-item > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)
        self.plus.send_key('//*[@id="brief"]', 'brief')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside/div[1]/content-attr/div/div[8]/div/label[2]/span[1]')  # 评论
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside/div[1]/content-attr/div/div[9]/div/label[2]/span[1]')  # 原创
        self.plus.send_key('//*[@id="author"]', 'author')
        self.plus.send_key('//*[@id="source"]', 'source')
        self.plus.send_key('//*[@id="originalLink"]', 'https://baidu.com')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]')  # 保存
        sleep(5)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]'))
        if length == 1:  # 保存无反应
            self.plus.click('/html/body/div/div[2]/div[3]/ui-view/div/main/nav/div/div[1]/span')  # 返回
            sleep(5)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.assertEqual(text, '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐', '新增专题失败')
        self.assertNotEqual(length, 1, '新增专题保存后无法正常跳转')

    def test_12(self):
        '''更多按钮验证F'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/div/div/button[2]')  # 编辑
        sleep(3)
        self.plus.fc('#view > ui-view > div > main > div > div > div.content-form-title > div > textarea').send_keys('1')
        sleep(2)
        self.plus.fc('#vm\.specialId > div > div > div > button.btn.primary-btn.save-btn.ng-isolate-scope').click()  # 保存
        sleep(8)
        length = len(self.plus.finds('/html/body/div/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]'))
        if length == 1:
            self.plus.click('/html/body/div/div[2]/div[3]/ui-view/div/main/nav/div/div[1]/span')  # 返回
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/div/div/button[5]')  # 操作记录
        sleep(2)
        text4 = self.plus.find('//*[@id="history-version"]').text
        self.plus.fc('.close-btn').click()

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/div/div/div[4]')  # 定时发布
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.content-time-modal.in > div > div > div > div:nth-child(2) > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide-active > div > div:nth-child(5) > input[type=checkbox]').click()
        self.plus.find('/html/body/div[4]/div/div/div/div[3]/div[2]/div/div/div/div/div[2]/input').clear()
        self.plus.find('/html/body/div[4]/div/div/div/div[3]/div[2]/div/div/div/div/div[2]/input').send_keys((datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M"))
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.content-time-modal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-binding.ng-isolate-scope').click()  # 保存
        sleep(2)
        length1 = len(self.plus.finds(base.qita_lanmu + '/span[2]'))

        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/div/div/button[11]')  # 审核
        sleep(3)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text

        text7 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/div/div/button[10]')  # 打回
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(5)
        text8 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text

        text9 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[7]/span[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/div/div/div/button[11]')  # 删除
        self.plus.fc('div.modal-footer:nth-child(3) > button:nth-child(1)').click()
        sleep(3)
        text10 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[7]/span[2]').text

        self.assertNotEqual(text1, text2, '编辑按钮失效')
        self.assertNotEqual('', text4, '操作记录为空')
        self.assertEqual(length1, 1, '定时发布按钮失效')
        self.assertNotEqual(text5, text6, '审核按钮失效')
        self.assertNotEqual(text7, text8, '打回按钮失效')
        self.assertNotEqual(text9, text10, '删除按钮失效')
        self.assertNotEqual(length, 1, '编辑专题保存后无法自动跳转')

    def test_13(self):
        '''专题底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button')
        sleep(5)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[1]/div/textarea', '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]')  # 保存
        sleep(5)
        if len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]')) == 1:
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/nav/div/div[1]/span')
            sleep(3)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[1]')  # 审核
        sleep(5)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[4]')  # 发布
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.publish-tip-modal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-scope').click()
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.content-publish-modal.in > div > div > div > div:nth-child(2) > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide.swiper-slide-active > div > div:nth-child(5) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.content-publish-modal.in > div > div > div > div.modal-footer > button:nth-child(2)').click()
        sleep(3)
        length = len(self.plus.finds(base.qita_lanmu + '/span/a'))

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[2]')  # 打回
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(4)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        before = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[5]')  # 移动
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.bulkCopy-contentmodal.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide-active > div > div:nth-child(2) > input[type=checkbox]').click()
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.bulkCopy-contentmodal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-binding.ng-isolate-scope').click()
        sleep(4)
        after = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(5)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]').text

        self.assertEqual(text1, '已审核', '底部审核按钮失效')
        self.assertEqual(text2, '已打回', '底部打回按钮失效')
        self.assertNotEqual(before, after, '底部移动功能失效')
        self.assertNotEqual(text3, text4, '底部删除按钮失效')
        self.assertEqual(length, 1, '发布的栏目未出现')

    def test_14(self):
        '''专题底部按钮验证'''
        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button')
        sleep(5)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div[1]/div/textarea', '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]')  # 保存
        sleep(5)
        if len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/content-save/div/div/div/button[1]')) == 1:
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/nav/div/div[1]/span')
            sleep(3)

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[8]')  # 选择栏目
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.publish-tip-modal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-scope').click()
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.content-publish-modal.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide.swiper-slide-active > div > div:nth-child(5) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.content-publish-modal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)
        text1 = self.plus.find(base.qita_lanmu + '/span/a').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[7]')  # 提审
        sleep(4)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.showAudit.in > div > div > div > div.body-audit.ng-scope > div.modal-footer > button.btn.btn-primary.button.ng-scope').click()
        sleep(4)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[9]')  # 设置标签
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.setLabel-modal.in > div > div > div > div.modal-body > div.column-wrap > div.item-content > div:nth-child(1) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.setLabel-modal.in > div > div > div > div.modal-footer.flex-item > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div[1]/span'))

        self.assertEqual(text1, '发现', '选择栏目按钮失效')
        self.assertEqual(text2, '审核中', '提审按钮失效')
        self.assertEqual(length, 1, '设置标签按钮失效')
