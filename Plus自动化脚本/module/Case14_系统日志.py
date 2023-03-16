from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('系统日志')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''验证导出日志按钮'''
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[4]/a')  # 导出日志
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        self.assertNotEqual(file1, file2, '导出日志按钮失效')

    def test_02(self):
        '''验证时间选择器'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[1]/input')
        self.plus.click('/html/body/div[2]/div[3]/ul/li[2]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[1]/input')
        self.plus.click('/html/body/div[2]/div[3]/ul/li[6]')  # 自定义
        sleep(2)
        self.plus.find('/html/body/div[2]/div[1]/div[1]/input').click()
        self.plus.find('/html/body/div[2]/div[1]/div[1]/input').clear()
        self.plus.send_key('/html/body/div[2]/div[1]/div[1]/input', '2022-10-15')
        sleep(1)
        self.plus.find('/html/body/div[2]/div[2]/div[1]/input').click()
        self.plus.find('/html/body/div[2]/div[2]/div[1]/input').clear()
        self.plus.send_key('/html/body/div[2]/div[2]/div[1]/input', '2022-10-30')
        sleep(1)
        self.plus.click('/html/body/div[2]/div[3]/div/button[1]')
        sleep(10)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[1]/input')
        self.plus.click('/html/body/div[2]/div[3]/ul/li[1]')
        sleep(3)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text

        self.assertNotEqual(text1, text2, '时间选择器失效')
        self.assertNotEqual(text3, text2, '时间选择器失效')
        self.assertNotEqual(text3, text4, '时间选择器失效')

    def test_03(self):
        '''验证筛选框'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[2]/div/div/div/div[2]/span')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[2]/div/div/div[2]/div[2]/span')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[2]/div/div/div[2]/div[1]/span[2]')
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[2]/div/div/div/div[1]/span')
        sleep(3)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[3]/div/a[5]')
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[3]/div/a[1]')
        sleep(3)

        self.assertNotEqual(text1, text2, '用户筛选框失效')
        self.assertNotEqual(text3, text2, '模块筛选框失效')

    def test_04(self):
        '''验证搜索框'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[5]/search-box/div[1]/input', 'test\n')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/nav/div[5]/search-box/div[1]/i[1]')
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text

        self.assertNotEqual(text1, text2, '搜索框失效')
        self.assertEqual(text3, text1, '搜索框取消按钮失效')

    def test_05(self):
        '''验证加载更多按钮'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[2]/span')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/section/div[1]').text

        self.assertNotEqual(text1, text2, '加载更多按钮失效')
