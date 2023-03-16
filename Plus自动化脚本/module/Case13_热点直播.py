from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('热点直播')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        '''左侧分类栏验证'''
        self.plus.driver.switch_to.frame('communityFrame')
        text1 = self.plus.find('/html/body/section/section/div/div[2]').text
        self.plus.click('/html/body/section/section/div/div[1]/div/ul/li[2]/a[1]/div')
        sleep(3)
        text2 = self.plus.find('/html/body/section/section/div/div[2]').text
        self.plus.click('/html/body/section/section/div/div[1]/div/ul/li[3]/a[1]/div')
        sleep(3)
        text3 = self.plus.find('/html/body/section/section/div/div[2]').text
        self.plus.click('/html/body/section/section/div/div[1]/div/ul/li[1]/a[1]/div')
        sleep(3)

        self.assertNotEqual(text1, text2, '左侧分类按钮失效')
        self.assertNotEqual(text3, text2, '左侧分类按钮失效')

    def test_02(self):
        '''筛选框、搜索框验证'''
        text1 = self.plus.find('/html/body/section/section/div/div[2]').text
        select = Select(self.plus.find('/html/body/section/section/div/div[2]/div[2]/div[1]/div[1]/select'))
        sleep(1)
        select.select_by_visible_text("待审核")
        sleep(2)
        text2 = self.plus.find('/html/body/section/section/div/div[2]').text
        select.select_by_visible_text("审核状态")

        text3 = self.plus.find('/html/body/section/section/div/div[2]').text
        select = Select(self.plus.find('/html/body/section/section/div/div[2]/div[2]/div[1]/div[2]/select'))
        sleep(1)
        select.select_by_visible_text("已推荐")
        sleep(2)
        text4 = self.plus.find('/html/body/section/section/div/div[2]').text
        select.select_by_visible_text("推荐状态")

        text5 = self.plus.find('/html/body/section/section/div/div[2]').text
        select = Select(self.plus.find('/html/body/section/section/div/div[2]/div[2]/div[1]/div[3]/select'))
        sleep(1)
        select.select_by_visible_text("直播中")
        sleep(2)
        text6 = self.plus.find('/html/body/section/section/div/div[2]').text
        select.select_by_visible_text("直播状态")

        text9 = self.plus.find('/html/body/section/section/div/div[2]').text
        self.plus.send_key('/html/body/section/section/div/div[2]/div[2]/div[2]/input', '小孩\n')
        sleep(2)
        text10 = self.plus.find('/html/body/section/section/div/div[2]').text
        self.plus.find('/html/body/section/section/div/div[2]/div[2]/div[2]/input').clear()
        sleep(2)

        text7 = self.plus.find('/html/body/section/section/div/div[2]').text
        self.plus.send_key('//*[@id="start-time"]', '2022-09-01 00:00:00')
        self.plus.send_key('//*[@id="end-time"]', '2022-11-30 00:00:00')
        sleep(2)
        text8 = self.plus.find('/html/body/section/section/div/div[2]').text

        self.assertNotEqual(text1, text2, '筛选框失效')
        self.assertNotEqual(text3, text4, '筛选框失效')
        self.assertNotEqual(text5, text6, '筛选框失效')
        self.assertNotEqual(text7, text8, '时间筛选框失效')
        self.assertNotEqual(text9, text10, '搜索框失效')

    def test_03(self):
        '''点击播放验证'''
        self.plus.driver.refresh()
        sleep(3)
        self.plus.driver.switch_to.frame('communityFrame')
        if self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[1]/div[2]/div[1]/p').text == 'test':
            self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span').click()
            self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[9]').click()  # 删除
            self.plus.find('/html/body/div[3]/div/div/div/div[3]/button[2]').click()
            sleep(2)

        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[1]/div[1]/img[2]')
        sleep(3)
        self.plus.click('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[4]')  # 暂停
        text1 = self.plus.find('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[5]/span').text
        sleep(1)
        self.plus.click('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[4]')
        sleep(3)
        self.plus.click('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[4]')
        sleep(1)
        text2 = self.plus.find('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[5]/span').text
        self.plus.click('/html/body/div[3]/div/div/div[1]/span')
        print(text1, text2)
        self.assertNotEqual(text1, text2, '视频预览无法播放')

    def test_04(self):
        '''新建直播功能验证'''
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/div/div/a')
        self.plus.click('/html/body/section/div/div[3]/a')
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/div/div/a')
        self.plus.click('/html/body/section/div/div[1]/div/a')
        sleep(3)
        text1 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul')
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/div/div/a')
        sleep(3)
        self.plus.send_key('/html/body/section/div/div[2]/div[1]/div/div[1]/input', 'test')
        self.plus.click('/html/body/section/div/div[2]/div[1]/div/div[5]/div/div/input')
        self.plus.click('/html/body/section/div/div[2]/div[1]/div/div[5]/div/div/div/div/li[3]/a[2]/div')
        self.plus.send_key('//*[@id="starttime"]', '2022-11-01 00:00:00')
        self.plus.send_key('//*[@id="stoptime"]', '2022-11-30 00:00:00')
        self.plus.click('/html/body/section/div/div[3]/div')
        sleep(3)
        text2 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul')

        self.assertNotEqual(text1, text2, '新建直播功能异常')

    def test_05(self):
        '''查看按钮验证'''
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/a[4]')
        sleep(3)
        text1 = self.plus.find('/html/body/section/div/div/div[1]/span[2]').text
        text2 = self.plus.find('/html/body/section/div/div/div[2]/div/div[1]/div[2]').text

        self.assertEqual(text1, '直播详情', '直播详情页展示有误')
        self.assertNotEqual(text2, '', '直播详情页展示有误')

    def test_06(self):
        '''直播详情页验证'''
        self.plus.send_key('/html/body/section/div/div/div[4]/div[1]/div[1]/textarea', 'test message')
        self.plus.click('/html/body/section/div/div/div[4]/div[1]/div[2]/div[4]/div/span')
        sleep(2)
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[8]')).perform()
        self.plus.click('/html/body/div[3]/div/div/div[2]/div/div[2]/div[3]/div/div[8]/div[3]/span')
        sleep(1)
        self.plus.click('/html/body/section/div/div/div[4]/div[1]/div[2]/div[6]/span')
        sleep(3)
        text = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]/div[1]/div').text
        length = len(self.plus.finds('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]/div[1]/ul/div[2]/li/video-play/span'))

        self.assertEqual(text, 'test message', '发布现场报道功能异常')
        self.assertEqual(length, 1, '发布现场报道选取视频功能异常')

    def test_07(self):
        '''直播详情页-现场报道验证'''
        before = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div/div[3]/a').text
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div/div[3]/a')
        sleep(2)
        after = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div/div[3]/a').text

        text1 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]').text
        self.plus.send_key('/html/body/section/div/div/div[4]/div[1]/div[1]/textarea', '123')
        self.plus.click('/html/body/section/div/div/div[4]/div[1]/div[2]/div[5]/span')
        sleep(3)
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[2]/div[5]/div[1]/a')  # 置顶
        sleep(2)
        text2 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]').text
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]/div[5]/div[3]/a')  # 编辑
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div/div[1]/textarea', '1')
        self.plus.click('/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/span')
        sleep(2)
        text3 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]').text

        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[2]/div[5]/div[4]')  # 更多
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[2]/div[5]/div[4]/div/div[4]/a')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        sleep(2)
        length = len(self.plus.finds('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div'))

        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div[1]/div[5]/div[4]')  # 更多
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div/div[5]/div[4]/div/div[1]/a')  # 修改发布时间
        sleep(2)
        self.plus.fc("[ng-model='time_vm.time']").send_keys('2022-11-01 00:00:00')
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body > div').click()
        sleep(2)
        text5 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[3]/div/div[4]/p[2]').text

        self.assertNotEqual(before, after, '审核按钮失效')
        self.assertNotEqual(text1, text2, '置顶按钮失效')
        self.assertNotEqual(text3, text2, '编辑按钮失效')
        self.assertNotEqual(length, 2, '删除按钮失效')
        self.assertIn(text5, '2022-11-01 00:00:00', '修改发布时间失败')

    def test_08(self):
        '''直播详情页-聊天室验证'''
        self.plus.click('/html/body/section/div/div/div[3]/ul/li[2]/a')  # 聊天室
        self.plus.send_key('/html/body/section/div/div/div[4]/div[2]/div[1]/textarea', '123')
        self.plus.click('/html/body/section/div/div/div[4]/div[2]/div[2]/div/span')
        sleep(2)
        text = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div/div[1]/div').text

        text1 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[1]/div[2]/a').text
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[1]/div[2]/a')
        sleep(2)
        text2 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[1]/div[2]/a').text

        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[1]/div[5]/div[2]/a')  # 回复
        sleep(1)
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/div/div[1]/textarea', 'response')
        self.plus.click('/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/span')
        sleep(2)

        text3 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[2]/div[1]/div')
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[2]/div[5]/div[3]/a')  # 编辑
        sleep(1)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.text-center.p-lg > div > div.publish-content > textarea').send_keys('1')
        sleep(1)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-body.text-center.p-lg > div > div.comment-op.sys-flex > div.sys-flex-one > span').click()
        sleep(2)
        text4 = self.plus.find('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[2]/div[1]/div')

        length1 = self.plus.finds('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div')
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[1]/div[5]/div[4]')
        sleep(1)
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div[1]/div[5]/div[4]/div/div[4]/a')  # 删除
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(2)
        length2 = self.plus.finds('/html/body/section/div/div/div[4]/div[3]/div/div[4]/div')

        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[2]/a[1]')  # 导出会员信息
        sleep(1)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        file3 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/section/div/div/div[4]/div[3]/div/div[2]/a[2]')  # 导出聊天内容
        sleep(1)
        file4 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/section/div/div/div[1]/a')
        sleep(2)

        self.assertEqual(text, '123', '发布聊天功能异常')
        self.assertNotEqual(text1, text2, '审核按钮失效')
        self.assertNotEqual(text3, text4, '编辑按钮失效')
        self.assertNotEqual(length1, length2, '删除按钮失效')
        self.assertNotEqual(file1, file2, '导出会员信息按钮失效')
        self.assertNotEqual(file3, file4, '导出聊天内容按钮失效')

    def test_09(self):
        '''编辑功能验证'''
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/a[1]')
        self.plus.click('/html/body/section/div/div[3]/a')
        sleep(2)
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/a[1]')
        self.plus.click('/html/body/section/div/div[1]/div/a')
        sleep(2)

        text1 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[1]/div[2]/div[1]/p').text
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/a[1]')
        sleep(1)
        self.plus.send_key('/html/body/section/div/div[2]/div[1]/div/div[1]/input', '123')
        self.plus.click('/html/body/section/div/div[3]/div')
        sleep(3)
        text2 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[1]/div[2]/div[1]/p').text

        self.assertNotEqual(text1, text2, '编辑功能异常')

    def test_10(self):
        '''更多按钮验证'''
        text1 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[4]').text
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span')
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[7]')  # 状态按钮
        sleep(2)
        text2 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[4]').text
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span')
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[7]')  # 状态按钮
        sleep(2)
        text3 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[4]').text

        text4 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[5]').text
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span')
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[8]')  # 推荐按钮
        sleep(2)
        text5 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[5]').text
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span')
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[8]')  # 推荐按钮
        sleep(2)
        text6 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[5]').text

        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span')
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[3]/a')  # 查看日志
        sleep(3)
        self.plus.click('/html/body/section/div/div/div/a')

        text8 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]').text
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/span')
        self.plus.click('/html/body/section/section/div/div[2]/div[3]/div/div[2]/ul/li[1]/div[11]/ul/li[9]')  # 删除按钮
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        sleep(3)
        text9 = self.plus.find('/html/body/section/section/div/div[2]/div[3]/div/div[2]').text

        self.assertNotEqual(text1, text2, '状态按钮失效')
        self.assertNotEqual(text2, text3, '状态按钮失效')
        self.assertNotEqual(text4, text5, '推荐按钮失效')
        self.assertNotEqual(text5, text6, '推荐按钮失效')
        self.assertNotEqual(text8, text9, '删除按钮失效')

    def test_11(self):
        '''顶部按钮验证'''
        sleep(2)
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/a[1]')  # 直播监控
        sleep(2)
        window = self.plus.driver.window_handles
        self.plus.driver.switch_to.window(window[2])
        sleep(1)
        length = self.plus.finds('/html/body/section/div/ul/li')
        self.plus.driver.switch_to.window(window[1])
        self.plus.driver.switch_to.frame('communityFrame')

        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/a[3]')  # 导出活动
        sleep(2)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/a[4]')  # 更新记录
        sleep(2)
        window = self.plus.driver.window_handles
        self.plus.driver.switch_to.window(window[3])
        text1 = self.plus.find('/html/body/section/div[2]').text
        self.plus.driver.switch_to.window(window[1])
        self.plus.driver.switch_to.frame('communityFrame')

        self.assertNotEqual(length, 1, '直播监控页面为空')
        self.assertNotEqual(file1, file2, '导出按钮失效')
        self.assertNotEqual(text1, '', '更新记录页面展示有误')

    def test_12(self):
        '''配置内部功能验证'''
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/a[2]')  # 配置
        sleep(2)
        text1 = self.plus.find('/html/body/section/div/div[1]/div').text
        self.plus.click('/html/body/section/div/div[2]/div[1]/div/span[2]')  # 返回上级
        sleep(2)
        self.plus.click('/html/body/section/section/div/div[2]/div[1]/div/a[2]')  # 配置

        self.plus.click('/html/body/section/div/div[2]/div[1]/div/span[1]')  # 添加分类
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/form/div[1]/div/input', 'class1')
        self.plus.click('/html/body/div[3]/div/div/div/div[2]/form/div[3]')
        sleep(3)

        i = len(self.plus.finds('/html/body/section/div/div[2]/div[3]/ul/li'))
        self.plus.click(f'/html/body/section/div/div[2]/div[3]/ul/li[{i}]/div[4]')  # 创建子分类
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/form/div[1]/div/input', 'child')
        self.plus.click('/html/body/div[3]/div/div/div/div[2]/form/div[3]')
        sleep(3)
        self.plus.click(f'/html/body/section/div/div[2]/div[3]/ul/li[{i}]/div[4]')  # 查看子分类
        sleep(1)
        length = len(self.plus.finds('/html/body/section/div/div[2]/div[3]/ul/li/div[2]'))

        text2 = self.plus.find('/html/body/section/div/div[2]/div[3]/ul/li/div[2]').text
        self.plus.click('/html/body/section/div/div[2]/div[3]/ul/li/div[5]/span[1]')  # 编辑
        sleep(2)
        self.plus.send_key('/html/body/div[3]/div/div/div/div[2]/form/div[1]/div/input', '1')
        self.plus.click('/html/body/div[3]/div/div/div/div[2]/form/div[3]')
        sleep(3)
        text3 = self.plus.find('/html/body/section/div/div[2]/div[3]/ul/li/div[2]').text

        self.plus.click('/html/body/section/div/div[2]/div[3]/ul/li/div[5]/span[2]/img')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        self.plus.click(f'/html/body/section/div/div[2]/div[3]/ul/li[{i}]/div[5]/span[2]/img')  # 删除
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        sleep(2)
        j = len(self.plus.finds('/html/body/section/div/div[2]/div[3]/ul/li'))

        self.assertNotEqual(text1, '', '配置页面进入失败')
        self.assertEqual(length, 1, '创建子分类失败')
        self.assertNotEqual(text2, text3, '编辑按钮失效')
        self.assertNotEqual(i, j, '删除按钮失效')
