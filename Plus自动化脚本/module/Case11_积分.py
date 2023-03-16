import random

from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('积分')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''积分管理页面验证F'''
        sleep(5)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div[2]/div/img'))

        self.assertNotEqual(length, 1, '积分管理页面一直加载中')

    def test_02(self):
        '''任务管理-筛选框验证'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/div/a[2]')
        sleep(4)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div'))
        for i in range(4, length):
            text = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[{i}]/div/div[3]/span').text
            self.assertEqual(text, '每日任务', '筛选框失效')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/div/a[1]')
        sleep(2)

    def test_03(self):
        '''任务管理-按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[7]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[7]/span')  # 启用
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[7]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[7]/span')
        sleep(2)

        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[2]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[8]/div/i')  # 编辑
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[3]/input', 1)
        sleep(2)
        text3 = self.plus.find('/html/body/div[3]/div/div/form/div[2]/div[3]/input').get_attribute('value')
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[2]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[4]/div/div[8]/div/i')
        sleep(1)
        text4 = self.plus.find('/html/body/div[3]/div/div/form/div[2]/div[3]/input').get_attribute('value')
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[3]/input', Keys.BACKSPACE)
        sleep(1)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)

        self.assertNotEqual(text1, text2, '启用按钮失效')
        self.assertEqual(text3, text4, '编辑按钮失效')

    def test_04(self):
        '''积分日志-筛选框验证'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[3]')
        sleep(3)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[13]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/div/div/a[4]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[13]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/div/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[1]/div/div/a[1]')
        sleep(3)

        self.assertNotEqual(text1, text2, '筛选框失效')

    def test_05(self):
        '''积分日志-导出按钮验证'''
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div/div/div/div[13]/div/a')  # 导出
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        self.assertNotEqual(file1, file2, '导出功能异常')

    def test_06(self):
        '''积分设置验证'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[4]')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[4]/label/span[2]')
        sleep(1)

        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]').text
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[5]/div/i[1]')
        sleep(2)
        self.plus.fc("[ng-model='vm.brief']").clear()
        self.plus.fc("[ng-model='vm.brief']").send_keys(random.randint(0, 1000))
        sleep(1)
        self.plus.fc("[ng-click='vm.save()']").click()
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]').text

        self.assertNotEqual(text1, text2, '积分设置编辑功能异常')

    def test_07(self):
        '''积分统计验证F'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[5]')
        sleep(8)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div/div/div/div[2]/div[2]/div[2]/div/img'))

        self.assertNotEqual(length, 1, '积分统计页面一直在加载中')
