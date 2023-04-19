from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('报料')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''报料-分类管理跳转'''
        ele = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(ele).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]').text
        self.assertNotEqual(text, '', '分类为空')

    def test_02(self):
        '''报料-分类管理功能验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[1]/div[2]/span')
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', '测试分类' + str(random.randint(0, 100)))
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[2]/div[1]/div[2]/span')
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[2]')
        sleep(3)
        ele = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        before = ele[-1].text
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[2]/i[1]')  # 编辑按钮
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', Keys.BACK_SPACE)
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(3)
        after = ele[-1].text
        elements1 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[2]/i[2]')  # 删除按钮
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')  # 确认删除
        sleep(3)
        elements2 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')

        self.assertNotEqual(before, after, '修改失败')
        self.assertNotEqual(len(elements1), len(elements2), '删除成功')

    def test_03(self):
        '''报料设置页面验证'''
        ele = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(ele).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[3]')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[1]/div/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[2]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div[3]/span')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[1]/div/input-number/div/span/i[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[2]/div[2]/div/input-number/div/span/i[2]')
        before = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div[2]/div[3]/button')  # 保存
        sleep(2)
        self.plus.driver.refresh()
        sleep(3)
        after = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]').text
        self.assertEqual(before, after, '保存按钮失效')

    def test_04(self):
        '''话题设置页面验证'''
        ele = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(ele).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[4]')
        sleep(3)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[3]/div/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/button')  # 新增话题
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div/input', 'test')
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[1]')  # 保存
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[3]/div/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/button')
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div/input', 'ttest')
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[1]')  # 保存
        sleep(3)

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/span[1]')  # 编辑
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div/input', '0')
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[1]')  # 保存
        sleep(3)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[2]').text

        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[1]/div/search-box/div[1]/input', 'test\n')  # 搜索框验证
        sleep(2)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[1]/div/search-box/div[1]/i[1]')  # 取消搜索按钮
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div'))

        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/span[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[2]').text

        text7 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[3]/div/div[2]/div/button')  # 底部删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        text8 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div[2]/div[2]/div[1]/div/div[2]').text

        self.assertNotEqual(text1, text2, '新增功能异常')
        self.assertNotEqual(text3, text4, '编辑功能异常')
        self.assertEqual(length1, 2, '搜索功能异常')
        self.assertNotEqual(length1, length2, '取消搜索按钮异常')
        self.assertNotEqual(text5, text6, '删除按钮异常')
        self.assertNotEqual(text7, text8, '底部删除按钮异常')

    def test_05(self):
        '''列表页面分类按钮、筛选框、搜索框验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        sleep(5)
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[2]/div/div[2]/div/div')
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/classify-sidebar/div/div[1]/span')
        sleep(3)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/button')  # 全部状态按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/a[3]')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/a[1]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/button')  # 全部来源按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/div/a[2]')
        sleep(2)
        after3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[3]/div/a[1]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[4]/button')  # 全部话题按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[4]/div/a[2]')
        sleep(2)
        after4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[4]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[4]/div/a[1]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/button')  # 全部时间按钮
        self.plus.click('//*[@id="datepicker"]')
        sleep(2)
        self.plus.click('/html/body/div[2]/div[3]/div/button[1]')
        sleep(2)
        after5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div/a[1]')
        sleep(2)

        self.assertNotEqual(before1, after1, '左侧分类按钮切换失败')
        self.assertNotEqual(before1, after2, '状态按钮切换失败')
        self.assertNotEqual(before1, after3, '来源按钮切换失败')
        self.assertNotEqual(before1, after4, '话题按钮切换失败')
        self.assertNotEqual(before1, after5, '时间按钮切换失败')

    def test_06(self):
        '''搜索功能验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[5]/search-box/div[1]/input', '天气\n')  # 搜索框
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[5]/search-box/div[1]/i[1]')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text

        self.assertNotEqual(before1, after1, '搜索功能无法正常使用')
        self.assertNotEqual(after1, after2, '叉号按钮失效')

    def test_07(self):
        '''选中按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/label/input')  # 全选按钮
        sleep(2)
        checked = []
        for i in range(1, 11):
            checked.append(self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[{i}]/div[1]/div[1]/label/input').get_attribute('checked'))
            self.assertEqual(checked[i - 1], 'true', '全选按钮失效')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        check1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input').get_attribute('checked')
        check2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/label/input').get_attribute('checked')  # 全选按钮
        self.assertNotEqual(check2, 'true', '全选按钮失效')
        self.assertNotEqual(check1, 'true', '选择按钮失效')

    def test_08(self):
        '''翻页按钮验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.assertNotEqual(before1, after1, '翻页按钮失效')

    def test_09(self):
        '''跳至输入框验证'''
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.fc("[ng-model='vm.options.jump']").send_keys('1\n')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.assertNotEqual(after1, after2, '跳至输入框失效')

    def test_10(self):
        '''每页条数按钮验证'''
        before = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.fc('.change-btn').click()
        self.plus.fc('.dropup a:nth-of-type(2)').click()
        sleep(2)
        after = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div').text
        self.plus.fc('.change-btn').click()
        self.plus.fc('.dropup a:nth-of-type(1)').click()
        sleep(3)
        self.assertNotEqual(before, after, '每页条数按钮失效')

    def test_11(self):
        '''新增报料功能验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/p').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[1]/div[2]/button')
        sleep(2)
        self.plus.send_key('/html/body/div[4]/div/div/form/div[2]/div/div[1]/textarea', '女子一家三口发烧用洋葱退热成功')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[2]/div/div[1]')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[2]/div/div[2]/div[2]')
        self.plus.send_key('/html/body/div[4]/div/div/form/div[2]/div/div[8]/input', '张三')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[10]/div/input')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[10]/div/div/table/tbody/tr[2]/td[5]/button/span')
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/form/div[3]/button[1]')  # 保存
        sleep(2)
        self.plus.driver.refresh()
        sleep(5)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/p').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[1]/div[2]/button')
        sleep(2)
        self.plus.send_key('/html/body/div[4]/div/div/form/div[2]/div/div[1]/textarea', '女子一家三口发烧用洋葱退热成功')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[2]/div/div[1]')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[2]/div/div[2]/div[2]')
        self.plus.send_key('/html/body/div[4]/div/div/form/div[2]/div/div[8]/input', '张三')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[10]/div/input')
        self.plus.click('/html/body/div[4]/div/div/form/div[2]/div/div[10]/div/div/table/tbody/tr[2]/td[5]/button/span')
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/form/div[3]/button[1]')  # 保存
        sleep(2)
        self.plus.driver.refresh()
        sleep(5)

        self.assertNotEqual(text1, text2, '新增报料功能正常')

    def test_12(self):
        '''话题编辑按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/i')
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/div/div[2]/div/div/button')
        self.plus.click('/html/body/div[4]/div/div/div/div[2]/div/div/div/div/input')
        self.plus.click('/html/body/div[4]/div/div/div/div[3]/button[1]')  # 保存
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]').text
        self.assertNotEqual(text1, text2, '话题编辑按钮异常')

    def test_13(self):
        '''回复按钮验证'''
        if self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/span').text != '已审核':
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/span')
            sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[6]/span[1]')
        sleep(3)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div/form/textarea', '回复一下')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div/button[1]')
        sleep(2)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[6]/div/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[6]/div/div/span')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[6]/div/div/div/div/div[2]/span[2]')  # 删除
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[6]/span[1]').text
        self.assertEqual(text1, '已回复', '回复按钮异常')
        self.assertEqual(text2, '回复', '删除回复按钮异常')

    def test_14(self):
        '''修改分类按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[7]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[7]/i')
        self.plus.click('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]')
        self.plus.click('/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/div[4]/label')
        self.plus.click('/html/body/div[4]/div/div/div/div[3]/button[1]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[7]/span').text

        self.assertNotEqual(text1, text2, '修改分类功能异常')

    def test_15(self):
        '''审核按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/span')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/span').text
        self.assertNotEqual(text1, text2, '审核按钮失效')

    def test_16(self):
        '''采纳按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[10]/button').get_attribute('class')
        text1 = text1.split(' ')[-1]
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[10]/button')
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.adopt-contribute-box.in > div > div > div > div.modal-body > label:nth-child(2) > input').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.adopt-contribute-box.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[10]/button').get_attribute('class')
        text2 = text2.split(' ')[-1]

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/p').text
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '文稿').click()  # 文稿
        sleep(5)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text
        self.plus.driver.back()
        sleep(5)

        self.assertEqual(text3, text4, '同步创建文稿按钮失效')
        self.assertNotEqual(text1, text2, '采纳按钮状态未变化')

    def test_17(self):
        '''删除按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]').text
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[2]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[11]/i')
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        self.plus.driver.refresh()
        sleep(5)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]').text
        self.assertNotEqual(text1, text2, '删除按钮失效')

    def test_18(self):
        '''底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div[3]/button')  # 审核
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[8]/span').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div[4]/button')  # 打回
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[8]/span').text

        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[10]/button').get_attribute('class')
        text4 = text4.split(' ')[-1]
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div[1]/button')  # 采纳
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.adopt-contribute-box.in > div > div > div > div.modal-body > label:nth-child(2) > input').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.adopt-contribute-box.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(3)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[10]/button').get_attribute('class')
        text5 = text5.split(' ')[-1]

        context1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[2]/div[2]/div[2]/p')
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '文稿').click()  # 文稿
        sleep(5)
        context2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text
        self.plus.driver.back()
        sleep(5)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div[2]/button')  # 不采纳
        sleep(4)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[10]/button').get_attribute('class')
        text6 = text6.split(' ')[-1]

        ac(self.plus.driver).scroll_by_amount(0, -3000).perform()
        sleep(2)
        text7 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/p').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[2]/div[5]/button')  # 删除
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        text8 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/p').text

        self.assertEqual('已审核', text2, '审核按钮异常')
        self.assertNotEqual(text3, text2, '打回按钮异常')
        self.assertNotEqual(text4, text5, '采纳按钮异常')
        self.assertNotEqual(text6, text5, '不采纳按钮异常')
        self.assertNotEqual(text7, text8, '删除按钮异常')
        self.assertNotEqual(context1, context2, '同步创建文稿功能异常')
