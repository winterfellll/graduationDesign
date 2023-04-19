from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase, base):
    '''2F'''

    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('发布库')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''左侧分类验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[1]/classify-sidebar/div/div[2]/div/div[2]/div/div')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[1]/classify-sidebar/div/div[1]/span')
        sleep(3)

        self.assertNotEqual(text1, text2, '左侧分类按钮失效')

    def test_02(self):
        '''筛选框验证'''
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/a[2]')
        sleep(2)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/a[1]')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/a[3]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/a[1]')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[2]')
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[1]')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[5]/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]')
        sleep(2)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[5]/div[1]/span[1]/i')

        self.assertNotEqual(text, text1, '状态筛选框失效')
        self.assertNotEqual(text, text2, '类型筛选框失效')
        self.assertNotEqual(text, text3, '时间筛选框失效')
        self.assertNotEqual(text, text5, '标签筛选框失效')

    def test_03(self):
        '''验证搜索框'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/search-box[1]/div[1]/input', '作品\n')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/search-box[1]/div[1]/i[1]')  # 叉号
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text

        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/search-box[2]/div[1]/input', 'hogesoft\n')
        sleep(2)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/search-box[2]/div[1]/i[1]')  # 叉号
        sleep(2)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text

        self.assertNotEqual(text1, text2, '标题搜索框失效')
        self.assertEqual(text1, text3, '标题搜索框取消按钮失效')
        self.assertNotEqual(text4, text5, '发布人搜索框失效')
        self.assertEqual(text4, text6, '发布人搜索框取消按钮失效')

    def test_04(self):
        '''排序按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/i')
        sleep(2)
        ele = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]')
        ac(self.plus.driver).drag_and_drop_by_offset(ele, 0, 530).pause(1).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/button[2]')  # 保存
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text

        self.assertNotEqual(text1, text2, '排序按钮失效')

    def test_05(self):
        '''翻页按钮验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[5]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[5]/page-nation/div/div[2]/div[1]/button[7]')  # 翻页按钮
        sleep(3)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text

        self.assertNotEqual(before1, after1, '翻页按钮失效')
        self.assertNotEqual(after1, after2, '翻页按钮失效')

    def test_06(self):
        '''跳至输入框验证'''
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.fc("[ng-model='vm.options.jump']").send_keys('1\n')
        sleep(2)
        after3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.assertNotEqual(after3, after2, '跳至输入框失效')

    def test_07(self):
        '''每页条数按钮验证'''
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div'))
        self.plus.fc(".change-btn").click()
        self.plus.fc(".dropup a:nth-of-type(7)").click()
        sleep(5)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div'))
        self.assertNotEqual(length1, length2, '每页条数按钮失效')

    def test_08(self):
        '''全选按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[5]/div[1]/label/input')  # 全选
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div'))
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div'))
        for i in range(1, length1 + 1):
            text = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[{i}]/div[1]/label/input').get_attribute('checked')
            self.assertEqual(text, 'true', '全选按钮失效')

        for i in range(1, length2 + 1):
            text = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[{i}]/div[1]/label/input').get_attribute('checked')
            self.assertEqual(text, 'true', '全选按钮失效')

    def test_09(self):
        '''底部按钮验证F'''
        self.plus.fabu()  # 发布一条文稿
        self.plus.driver.back()  # 回到发布库
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/label/input')
        self.plus.click("//button[.='复制']")  # 复制
        sleep(2)
        self.plus.fc("[data='17']").click()
        self.plus.fc("[ng-click='vm.save()']").click()
        sleep(3)
        length1 = len(self.plus.finds("//h5[@class='modal-title ng-binding']"))
        self.plus.driver.refresh()
        sleep(5)

        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/span[3]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/label/input')
        self.plus.click("//button[.='移动']")  # 移动
        sleep(2)
        self.plus.fc("[data='1']").click()
        self.plus.fc("[ng-click='vm.save()']").click()
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/span[3]').text

        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[5]/div[2]/div[4]/a')  # 导出
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        if self.plus.find('/html').text == '{"error_code":1009,"error_message":"\u8eab\u4efd\u4fe1\u606f\u9a8c\u8bc1\u5931\u8d25","data":[]}':
            text3 = self.plus.find('/html').text
            self.plus.driver.back()
            sleep(3)
            self.assertNotEqual(text3, '{"error_code":1009,"error_message":"\u8eab\u4efd\u4fe1\u606f\u9a8c\u8bc1\u5931\u8d25","data":[]}', '导出失败')

        before = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[5]/div[2]/div[1]/button')  # 删除
        sleep(2)
        self.plus.fc("[type='submit']").click()
        sleep(3)
        after = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text

        self.assertNotEqual(text1, text2, '移动按钮失效')
        self.assertNotEqual(before, after, '删除按钮失效')
        self.assertEqual(file1 + 1, file2, '导出失败')
        self.assertNotEqual(length1, 1, '复制后无反应')

    def test_10(self):
        '''发布库稿件点击验证F'''
        # 待完善
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span')
        sleep(5)
        windows = self.plus.driver.window_handles
        self.plus.driver.switch_to.window(windows[2])
        sleep(2)
        if len(self.plus.finds('/html/body/div[2]/span/span')) != 0:  # 错误页面
            text = self.plus.find('/html/body/div[2]/span/span[1]').text
            self.plus.driver.switch_to.window(windows[1])
            self.assertNotEqual(text, '融合媒体运营平台', '点击无法跳转到发布的平台')
        self.plus.driver.switch_to.window(windows[1])
        sleep(2)

    def test_11(self):
        '''更多按钮验证F'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/div/div/button[1]')  # 编辑
        sleep(5)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[1]/div[1]/div/textarea', '0')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[4]')  # 保存
        sleep(5)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text
        self.plus.driver.refresh()
        sleep(5)

        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/div/div/button[2]')  # 置顶
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[4]/div/div/div/button[2]')
        sleep(3)

        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/div/div/button[5]')  # 修改标题
        sleep(2)
        self.plus.send_key('/html/body/div[4]/div/div/div/div[2]/div/div[1]/input', '1')
        self.plus.send_key('/html/body/div[4]/div/div/div/div[2]/div/div[2]/input', '1')
        self.plus.click('/html/body/div[4]/div/div/div/div[3]/button[1]')
        sleep(2)
        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span').text

        text8 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/span[7]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/div/div/button[7]')  # 修改发布时间
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/div/div[2]/div/div[2]/input')
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[4]/td[3]/button/span')
        self.plus.click('/html/body/div[4]/div/div/div/div[3]/button[1]')
        sleep(2)
        text9 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/span[7]').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/div/div/button[13]')  # 操作记录按钮
        sleep(3)
        if len(self.plus.finds('/html/body/div[4]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[3]/span[1]')) != 1:
            self.assertEqual(len(self.plus.finds('/html/body/div[4]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[3]/span[1]')), 1, '操作记录展示异常')
        text10 = self.plus.find('/html/body/div[4]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[3]/span[2]').text
        self.plus.click('/html/body/div[4]/div/div/div/div[1]/div[1]/div/i')
        sleep(2)

        text11 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]/div[4]/div/div/div/button[11]')  # 删除按钮
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/div/div[3]/button[1]')
        sleep(3)
        text12 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[4]/div[1]').text

        self.assertEqual(text3, text, '置顶功能异常')
        self.assertNotEqual(text4, text5, '修改标题功能异常')
        self.assertNotEqual(text8, text9, '修改发布时间功能异常')
        self.assertEqual(text10, '修改发布时间', '操作记录展示异常')
        self.assertNotEqual(text11, text12, '删除功能异常')
        self.assertNotEqual(text1, text2, '编辑后标题未修改')

    def test_12(self):
        '''发布库-栏目管理跳转'''
        ele = self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.plus.driver).move_to_element(ele).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[4]')
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]').text
        self.assertNotEqual(text, '', '分类为空')

    def test_13(self):
        '''发布库-栏目管理页面功能验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[1]/div[2]/span')
        sleep(2)
        self.plus.fc("body > div.modal.fade.ng-isolate-scope.edit-column-publish.in > div > div > form > div.modal-body > div > input").send_keys('测试分类' + str(random.randint(0, 100)))
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.edit-column-publish.in > div > div > form > div.modal-footer > button.btn.primary-btn.ng-binding.ng-isolate-scope').click()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]/div[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[2]/div[1]/div[2]/span')
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.edit-column-publish.in > div > div > form > div.modal-footer > button.btn.cancel-btn.ng-binding').click()
        sleep(2)
        ele = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        before = ele[-1].text
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[4]/i[1]')  # 编辑按钮
        sleep(1)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[3]/div/div/div/div[1]/div[2]/div[1]/input', Keys.BACK_SPACE)
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[3]/div/div/div/div[6]/button')
        sleep(5)
        ele = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        after = ele[-1].text

        elements1 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[4]/i[2]')  # 删除按钮
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')  # 确认删除
        sleep(3)
        elements2 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')

        self.assertNotEqual(before, after, '修改失败')
        self.assertNotEqual(len(elements1), len(elements2), '删除成功')
