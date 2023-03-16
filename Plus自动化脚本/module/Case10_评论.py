from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('评论')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''评论设置页面功能验证'''
        el = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(el).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/label[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/label[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/label[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/label[2]/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[1]/div/input-number/div/span/i[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[2]/div/input-number/div/span/i[2]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[3]/button')  # 保存
        sleep(3)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[1]/div/input-number/div/input').text
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[2]/div/input-number/div/input').text
        self.plus.driver.refresh()
        sleep(5)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[1]/div/input-number/div/input').text
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[2]/div/input-number/div/input').text

        self.assertEqual(text1, text3, '保存功能异常')
        self.assertEqual(text2, text4, '保存功能异常')

    def test_02(self):
        '''左侧分类按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[3]/div/div[1]/div/div')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[1]/span')
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[3]/div').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[2]/input', '频\n')
        sleep(2)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[3]/div').text

        self.assertNotEqual(text1, text2, '左侧分类按钮失效')
        self.assertNotEqual(text3, text4, '左侧分类搜索框失效')

    def test_03(self):
        '''筛选框验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/div/a[3]')
        sleep(3)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div'))
        for i in range(3, length):
            text = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[{i}]/div/div/div[8]/span').text
            self.assertEqual(text, '已审核', '筛选功能异常')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/div/a[1]')

    def test_04(self):
        '''搜索框验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[2]/search-box/div[1]/input', '评论\n')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[2]/search-box/div[1]/i[1]')  # 取消搜索按钮
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div').text

        self.assertNotEqual(text1, text2, '搜索功能异常')
        self.assertNotEqual(text2, text3, '取消搜索按钮异常')

    def test_05(self):
        '''翻页按钮验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[13]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div').text

        self.assertNotEqual(before1, after1, '翻页按钮失效')

    def test_06(self):
        '''跳至输入框验证'''
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div').text
        self.plus.fc("[ng-model='vm.options.jump']").send_keys('1\n')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div').text
        self.assertNotEqual(after1, after2, '跳至输入框失效')

    def test_07(self):
        '''每页条数按钮验证'''
        len1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div'))
        self.plus.fc('.change-btn').click()
        self.plus.fc('.dropup a:nth-of-type(2)').click()
        sleep(2)
        len2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div'))
        self.plus.fc('.change-btn').click()
        self.plus.fc('.dropup a:nth-of-type(1)').click()
        sleep(3)
        self.assertNotEqual(len1, len2, '每页条数按钮失效')

    def test_08(self):
        '''评论点击验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div/div/div[3]/span')  # 评论对象
        sleep(3)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[2]/button'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[2]/button')
        sleep(3)

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[8]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[8]/span')  # 状态
        sleep(2)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[8]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[8]/span')  # 状态
        sleep(3)

        if self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[8]/span').text != '已审核':
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[8]/span')
            sleep(3)
        for i in range(10):
            if self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[{i + 3}]/div/div/div[2]/div[2]/div/small').text == '回复一下':
                self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[{i + 3}]/div/div/div[13]/i').click()
                self.plus.fc(".btn-sure").click()

        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[2]/div[2]/div/small').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[10]/i')  # 回复
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/div[2]/div/div/textarea', '回复一下')
        self.plus.click('/html/body/div[3]/div/div/div[3]/button[1]')
        sleep(2)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[2]/div[2]/div/small').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[13]/i')  # 删除
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text7 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[2]/div[2]/div/small').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[3]/div/div/div[12]/span')  # 日志
        sleep(2)
        length2 = self.plus.finds('/html/body/div[3]/div/div/div[2]/div/div/div/div[2]/div')
        self.plus.click('/html/body/div[3]/div/div/span')
        sleep(1)

        self.assertNotEqual(length1, 0, '评论对象点击失效')
        self.assertNotEqual(text3, text4, '状态按钮点击失效')
        self.assertNotEqual(text5, text6, '回复功能失效')
        self.assertNotEqual(text7, text6, '右侧删除按钮失效')
        self.assertNotEqual(length2, 0, '评论的日志为空')

    def test_09(self):
        '''底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[13]/div[1]/label/input')
        for i in range(3, 13):
            checked = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[{i}]/div/div/div[1]/label/input').get_attribute('checked')
            self.assertEqual(checked, 'true', '全选按钮失效')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[13]/div[1]/label/input')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div/div/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[13]/div[2]/div[1]/button')  # 审核
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div/div/div[8]/span').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div/div/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[13]/div[2]/div[2]/button')  # 打回
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div/div/div[8]/span').text

        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div/div/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[13]/div[2]/div[3]/button')  # 删除
        sleep(1)
        self.plus.fc("[ng-click='close()']").click()
        sleep(2)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div[3]/div/div/div/div[12]/div').text

        self.assertEqual('已审核', text2, '审核按钮异常')
        self.assertNotEqual(text3, text2, '打回按钮异常')
