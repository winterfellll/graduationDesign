from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('会员')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''会员列表-筛选框验证'''
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[1]/div/a[4]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[1]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[1]/div/a[1]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[2]/div/a[3]')
        sleep(2)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[1]/div/p'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[2]/div/a[1]')
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[3]/div/a[3]')
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[1]/div/p'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/div[3]/div/a[1]')
        sleep(2)
        self.assertNotEqual(text1, text2, '分组筛选框失效')
        self.assertNotEqual(length1, 0, '状态筛选框失效')
        self.assertNotEqual(length2, 0, '来源筛选框失效')

    def test_02(self):
        '''搜索框验证F'''
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/search-box/div[1]/input', '185\n')
        sleep(2)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div'))
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]').text
        flag = 0
        for i in range(length):
            text = self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[{i + 1}]/div[5]/span')
            if text == '18571137076':
                flag = 1

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[1]/search-box/div[1]/i[1]')  # 取消按钮
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]').text

        self.assertNotEqual(text1, text2, '搜索功能异常，未返回正确的搜索结果')
        self.assertEqual(flag, 1, '搜索功能异常，未返回正确的搜索结果')

    def test_03(self):
        '''会员点击查看详情验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]')
        sleep(1)
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[3]/div[2]/div[1]/span'))

        self.assertEqual(length, 1, '点击会员不能查看详情')

    def test_04(self):
        '''新增会员验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/nav/div/div/div/button')
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/div/input', 'hello1')
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[2]/div/input', 'hello')
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[6]/div/input', '13212345679')
        sleep(1)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(3)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[5]/span').text

        self.assertEqual(text, '13212345679', '新增会员功能异常')

    def test_05(self):
        '''分组按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[6]/div/div/button/span[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[6]/div/div/div/a[1]')
        sleep(1)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[6]/div/div/button/span[1]').text
        self.plus.driver.refresh()
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[6]/div/div/button/span[1]').text

        self.assertEqual(text1, text2, '选择分组功能异常')

    def test_06(self):
        '''更多按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[7]/div/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[7]/div/div/div/div/button[1]')  # 锁定
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[7]/div/div/div/div/button[1]')  # 解锁

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[7]/div/div/div/div/button[2]')  # 编辑
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[9]/textarea', '0')
        text1 = self.plus.find('/html/body/div[3]/div/div/form/div[2]/div[9]/textarea').get_attribute('value')
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[7]/div/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[7]/div/div/div/div/button[2]')  # 编辑
        sleep(2)
        text2 = self.plus.find('/html/body/div[3]/div/div/form/div[2]/div[9]/textarea').get_attribute('value')
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[2]')
        sleep(1)

        self.assertNotEqual(text1, text2, '编辑功能异常')

    def test_07(self):
        '''底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[2]/button')  # 锁定
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[1]/button')  # 解锁
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[3]/button')
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[3]/div/a[1]')
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[6]/div/div/button/span[1]').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[4]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[4]/div/a')
        sleep(2)
        length = self.plus.finds('/html/body/div[2]/div/div/div/span')

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(1)
        before = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[3]/div[2]/div[5]/button')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(2)
        after = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div[1]/div[2]/div[2]/div[1]').text

        self.assertEqual(text1, '已锁定', '底部锁定功能异常')
        self.assertEqual(text2, '', '底部解锁功能异常')
        self.assertEqual(text3, '一般会员', '底部更改分组功能异常')
        self.assertNotEqual(before, after, '底部删除按钮异常')
        self.assertNotEqual(length, 1, '底部更改角色功能弹出报错提示')

    def test_08(self):
        '''分组管理验证'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')  # 分组管理
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[1]/div[2]/span')
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', '测试分类' + str(random.randint(0, 100)))
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)

        ele = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        before = ele[-1].text
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[2]/i[1]')  # 编辑按钮
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', Keys.BACK_SPACE)
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        after = ele[-1].text
        elements1 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.plus.driver).move_to_element(ele[-1]).perform()
        self.plus.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[2]/i[2]')  # 删除按钮
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')  # 确认删除
        sleep(2)
        elements2 = self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')

        self.assertNotEqual(before, after, '修改失败')
        self.assertNotEqual(len(elements1), len(elements2), '删除成功')

    def test_09(self):
        '''会员设置页面验证F'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[3]')
        sleep(3)
        length = len(self.plus.finds('/html/body/div[2]/div/div/div/span'))
        sleep(2)

        self.assertNotEqual(length, 1, '进入会员设置页面弹出报错提示')

    def test_10(self):
        '''会员设置页面验证F'''
        before1 = self.plus.find('/html/body/div/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[1]/h3/label/input').get_attribute('class')
        before2 = self.plus.find('/html/body/div/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[2]/h3/label/input').get_attribute('class')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[1]/h3/label/span[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[2]/h3/label/span[1]')
        sleep(1)
        self.plus.driver.refresh()
        sleep(3)
        after1 = self.plus.find('/html/body/div/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[1]/h3/label/input').get_attribute('class')
        after2 = self.plus.find('/html/body/div/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[2]/h3/label/input').get_attribute('class')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/div/div[2]/div/div[1]/h3/label/span[1]')

        self.assertNotEqual(before1, after1, '开启手机号注册按钮修改失败')
        self.assertNotEqual(before2, after2, '强制绑定按钮修改失败')

    def test_11(self):
        '''审核列表验证'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[4]')
        sleep(3)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/nav/div/div/em').text

        self.assertEqual(text, '审核列表', '审核列表无法进入')

    def test_12(self):
        '''会员等级页面验证'''
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[5]')
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/nav/div/div/div/button')  # 新增等级
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/div/input', 'level2')
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[2]/div/input', '999999')
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(3)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[2]/span').text

        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[5]/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[6]/div/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[6]/div/div/div/a[1]')  # 编辑
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/form/div[2]/div[2]/div/input', Keys.BACKSPACE)
        self.plus.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(3)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[5]/span').text

        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[6]/div/div/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div[1]/div[6]/div/div/div/a[2]')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
        sleep(3)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div'))

        self.assertEqual(text, 'level2', '新增等级功能异常')
        self.assertNotEqual(text1, text2, '编辑功能异常')
        self.assertNotEqual(length1, length2, '编辑功能异常')
