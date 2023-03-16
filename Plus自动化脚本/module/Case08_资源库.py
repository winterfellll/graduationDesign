from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('资源库')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''新增文件夹按钮验证'''
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/i[3]')
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[1]')
        sleep(2)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/input', '文件夹1')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/i[2]')
        sleep(2)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text

        self.assertEqual(length1, length2, '叉号按钮失效')
        self.assertEqual(text, '文件夹1', '新增按钮失效')

    def test_02(self):
        '''文件上传按钮验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[2]')
        self.plus.send_key('//*[@id="input-inner"]', video_path)
        self.plus.click('/html/body/div[4]/div/div/div/div/div/div[4]/button')  # 上传
        sleep(5)
        text1 = self.plus.find('/html/body/div[4]/div/div/div/div/div/div[3]/div[2]/div/div[3]/span/span').text
        self.plus.click('/html/body/div[4]/div/div/div/div/div/div[1]/i')
        sleep(3)

        self.assertNotEqual(text1, '上传失败', 'mp4文件上传失败')

    def test_03(self):
        '''筛选框、搜索框验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.click('//*[@id="datepicker"]')
        self.plus.click('/html/body/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[5]')
        self.plus.click('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]')
        self.plus.click('/html/body/div[2]/div[3]/div/button[1]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.driver.refresh()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/button')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/a[3]')
        sleep(3)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.driver.refresh()
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/search-box/div[1]/input', '520\n')
        sleep(3)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li'))
        sleep(1)
        self.plus.driver.refresh()
        sleep(3)

        self.assertNotEqual(text1, text2, '时间筛选框失效')
        self.assertNotEqual(text1, text3, '类型筛选框失效')
        self.assertNotEqual(length, 11, '搜索框失效')

    def test_04(self):
        '''排序、展示按钮验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/a[1]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.driver.refresh()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/i')
        sleep(2)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul'))
        self.plus.driver.refresh()
        sleep(3)

        self.assertNotEqual(text1, text2, '排序按钮失效')
        self.assertNotEqual(length, 1, '展示按钮失效')

    def test_05(self):
        '''翻页按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[1]/ul/li[1]/div[3]')
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/page-nation/div/div[2]/div[1]/button[7]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text

        self.assertNotEqual(before1, after1, '翻页按钮失效')

    def test_06(self):
        '''跳至输入框验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/page-nation/div/div[2]/div[2]/input', '5\n')
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text

        self.assertNotEqual(before1, after1, '跳至输入框失效')

    def test_07(self):
        '''每页条数按钮验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/page-nation/div/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/page-nation/div/div[1]/div/a[4]')
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.driver.refresh()
        sleep(3)

        self.assertNotEqual(before1, after1, '每页条数按钮失效')

    def test_08(self):
        '''我的资源-底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[1]/ul/li[1]/div[2]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[1]/label/input')  # 全选按钮
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li'))
        for i in range(2, length + 1):
            a = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[{i}]/input').get_attribute('checked')
            self.assertEqual(a, 'true', '全选失败')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[1]/label/input')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/input')
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[2]/div/button[1]')  # 下载
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[2]/div/button[2]')  # 源文件
        sleep(3)
        file3 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[2]/div/button[3]')  # 删除
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/a[3]')  # 图片
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[2]/div/button[5]')  # 复制
        ele = self.plus.finds('/html/body/div[4]/div/div/form/div[2]/div[2]/ul/li')
        ele[-1].click()
        self.plus.click('/html/body/div[4]/div/div/form/div[3]/button[1]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text

        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[2]/div/button[4]')  # 移动
        ele = self.plus.finds('/html/body/div[4]/div/div/form/div[2]/div[2]/ul/li')
        ele[-1].click()
        self.plus.click('/html/body/div[4]/div/div/form/div[3]/button[1]')
        sleep(3)
        text4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text

        self.assertEqual(file1 + 1, file2, '下载按钮异常')
        self.assertEqual(file2 + 1, file3, '源文件按钮异常')
        self.assertEqual(text1, text2, '复制按钮异常')
        self.assertNotEqual(text3, text4, '移动按钮异常')
        self.assertNotEqual(text5, text6, '删除按钮异常')

    def test_09(self):
        '''文件按钮验证'''
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[2]/i[1]')  # 下载
        sleep(2)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        before = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[2]/i[2]')  # 删除
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        after = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text

        self.assertNotEqual(file1, file2, '下载按钮失效')
        self.assertNotEqual(before, after, '删除按钮失效')

    def test_10(self):
        '''回收站按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[1]/ul/li[1]/div[3]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[1]')  # 刷新
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[2]')  # 删除
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text

        before2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[3]')  # 还原
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[1]/ul/li[1]/div[2]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/span[1]/span').text

        self.assertNotEqual(before1, after1, '回收站删除按钮失效')
        self.assertNotEqual(before2, after2, '回收站还原按钮失效')
        self.assertEqual(text1, text2, '回收站还原按钮失效')

    def test_11(self):
        '''文件夹面包屑导航验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[2]/span[3]/span[1]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span').text

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[2]/span[1]')
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/div[1]/span[1]/span').text

        self.assertEqual(text1, text2, '我的资源按钮异常')
        self.assertEqual(text1, text3, '返回上一级按钮异常')

    def test_12(self):
        '''文件和文件夹同时删除验证F'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/page-nation/div/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[2]/span')
        sleep(1)
        self.plus.send_key('//*[@id="input-inner"]', picture_path)
        self.plus.click('/html/body/div[4]/div/div/div/div/div/div[4]/button')
        sleep(2)
        self.plus.click('/html/body/div[4]/div/div/div/div/div/div[1]/i')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[1]/div[1]/span[1]/span')
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/input', '新文件夹')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/div[1]/i[2]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[2]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/ul/li[3]/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/div[2]/div/button[3]')  # 删除
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div/div[2]/div/div[2]/div[3]/page-nation/div/span').text

        self.assertNotEqual(text1, text2, '文件和文件夹同时选中时能删除')
