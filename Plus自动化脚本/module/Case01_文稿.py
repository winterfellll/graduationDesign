from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    '''2F'''

    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('文稿')

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
        '''文稿页面分类按钮、筛选框、搜索框验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        sleep(3)
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[2]/div/div[2]/div/div')
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[1]/span')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[2]')  # 我的稿件按钮
        sleep(3)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/button')  # 全部状态按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a[6]')
        sleep(2)
        after4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/button')  # 全部级别按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/div/a[2]')
        sleep(2)
        after3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/div/a[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/button')  # 全部时间按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/div/a[2]')
        sleep(2)
        after5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/div/a[1]')

        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[5]/div[1]')
        self.plus.send_key('//*[@id="label-search-box"]', '123')
        sleep(2)

        self.assertNotEqual(before1, after1, '左侧分类按钮切换失败')
        self.assertNotEqual(before1, after2, '我的稿件按钮切换失败')
        self.assertNotEqual(before1, after3, '类型按钮切换失败')
        self.assertNotEqual(before1, after4, '状态按钮切换失败')
        self.assertNotEqual(before1, after5, '时间按钮切换失败')

    def test_04(self):
        '''搜索功能验证'''
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/search-box/div[1]/input', '国家\n')  # 搜索框
        sleep(2)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/search-box/div[1]/i[1]')
        sleep(4)
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
            checked = [0] * 10
            checked[i - 1] = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[' + str(i) + ']/div[1]/div[1]/label/input').get_attribute('checked')
            self.assertEqual(checked[i - 1], 'true', '全选按钮失效')

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input')
        check1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[10]/div[1]/div[1]/label/input').get_attribute('checked')
        check2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[1]/label/input').get_attribute('checked')  # 全选按钮
        self.assertNotEqual(check2, 'true', '全选按钮失效')
        self.assertNotEqual(check1, 'true', '选择按钮失效')

    def test_06(self):
        '''翻页按钮验证'''
        before1 = self.plus.find(base.first_).text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find(base.first_).text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/page-nation/div/div[2]/div[1]/button[6]')  # 翻页按钮
        sleep(3)
        after2 = self.plus.find(base.first_).text

        self.assertNotEqual(before1, after1, '翻页按钮失效')
        self.assertNotEqual(after1, after2, '翻页按钮失效')

    def test_07(self):
        '''跳至输入框验证'''
        after2 = self.plus.find(base.first_).text
        self.plus.fc(
            '#view > ui-view > div > div.mxu_side_wrapper.mxu_content_wrapper.ng-scope > div.member-cont.second-view > div > div > div > div.hoge-flex > div > div.list.white.border-bottom-radius.ng-pristine.ng-untouched.ng-valid.ng-not-empty > div.list_bottom.hoge-table-bottom.border-bottom-radius > page-nation > div > div.list_page > div.goTo-group.btn-group > input').send_keys(
            '1\n')
        sleep(2)
        after3 = self.plus.find(base.first_).text
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
        '''新增通稿-返回按钮和取消按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div')
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/nav/div/div/div[2]/span')  # 返回按钮
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[4]')  # 取消按钮
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div')
        sleep(3)
        if len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[1]/div[1]/span[2]')) == 1:
            self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[1]/div[1]/span[2]')  # 撤销按钮
            sleep(5)

    def test_10(self):
        '''新增通稿-标题和正文输入框验证'''
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[1]/div[1]/div/textarea', '美国洛杉矶仇恨犯罪达近20年最高水平')
        self.plus.driver.switch_to.frame('ueditor_2')
        self.plus.send_key('/html/body', '''    中新社洛杉矶12月7日电 美国加利福尼亚州洛杉矶郡人际关系委员会12月7日发布《2021年仇恨犯罪报告》。报告显示，2021年洛杉矶郡仇恨犯罪增长约23%，仇恨犯罪中74%具暴力性质，均为2002年以来最高数据。

        　　根据这份年度报告，2021年洛杉矶郡仇恨犯罪从前一年的641起增至786起。各种动机的仇恨犯罪都有所增长，但源于种族歧视的仇恨犯罪增加最多，从前一年的406起增至473起，增幅约17%。
        
        　　其中，2021年洛杉矶郡发生针对亚裔的仇恨犯罪77起，是该报告自发布以来最高纪录，同比增长约67%。相对2020年反亚裔仇恨犯罪同比猛增84%，2021年增幅有所降低。但报告同时指出，2021年针对亚裔的仇恨犯罪在全部种族歧视仇恨犯罪中占比达16%，首次超过亚裔在洛杉矶郡居民总人口中的比例。
        
        　　另据美国媒体报道，疫情期间，由于亚裔美国人被当作COVID-19病毒传播的替罪羊，受到更多暴力袭击。洛杉矶郡发生的反亚裔仇恨犯罪中，有23%的犯罪嫌疑人因疫情而怪罪受害人。
        
        　　此外，2021年洛杉矶郡发生的针对非裔、拉丁裔和中东裔的仇恨犯罪也有所增加。反移民仇恨犯罪增长48%，从56起增至83起，是该报告发布以来记录的最高数字。
        
        　　《洛杉矶时报》等美国媒体称，有专家表示，仇恨犯罪持续增长的趋势目前没有改变的迹象。加州圣伯纳迪诺仇恨和极端主义研究中心分析指出，2022年前10个月，洛杉矶发生的仇恨犯罪比去年同期增加12%，预计2023年仍会增加。''')
        self.plus.driver.switch_to.default_content()
        sleep(1)

    def test_11(self):
        '''新增通稿-左侧按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[1]/div/label[2]/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[1]/div/label[1]/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[1]')
        sleep(1)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[2]/div[2]/div/i')
        sleep(2)
        self.plus.fc("[data-target='#tab4']").click()  # 资源库
        self.plus.click('/html/body/div[5]/div/div/div/div[2]/div[2]/div[4]/div[2]/div[4]/div/div[1]/div/img')
        self.plus.click('/html/body/div[5]/div/div/div/div[2]/div[2]/div[4]/div[3]/page-nation/div/div[2]/div[1]/button[3]')
        sleep(2)
        self.plus.click('/html/body/div[5]/div/div/div/div[2]/div[2]/div[4]/div[3]/page-nation/div/div[2]/div[1]/button[7]')
        sleep(2)
        self.plus.click('/html/body/div[5]/div/div/div/div[3]/button[1]')  # 确定
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[1]/div[1]/i')
        sleep(2)
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[2]')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[5]')  # 下载按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[6]')  # 编辑按钮
        sleep(2)
        self.plus.click('/html/body/div[5]/div/div/div/div[3]/button[2]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[8]')  # 裁剪按钮
        sleep(2)
        self.plus.click('/html/body/div[5]/div/div/div/div[3]/button[1]')
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[4]')  # 删除按钮
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[1]/div/div/div[1]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[2]/div[2]/div[2]/div[2]/div[1]/i')
        sleep(2)
        self.plus.send_key('/html/body/div[5]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/input', picture_path)
        sleep(3)
        self.plus.click('/html/body/div[5]/div/div/div/div[3]/button[1]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[1]/div[1]/i')
        sleep(2)

        self.plus.fc(".md-input").click()  # 分类
        self.plus.fc(".list-group > li:nth-of-type(3) > .group-item").click()
        self.plus.fc(".select-color").click()  # 栏目
        self.plus.fc("[data='5']").click()
        self.plus.fc("[ng-click='vm.save()']").click()
        sleep(2)
        self.plus.fc("[title='点击添加到专题']").click()  # 专题
        sleep(2)
        self.plus.fc(".btn[ng-click='vm.close()']").click()
        self.plus.fc("[ng-show='vm.commentsShow'] .switch-close").click()  # 评论
        # if len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[11]/div/div/span')):
        #     self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[1]/div/div/div/div[2]/div[1]/div/content-attr/div/div[11]/div/div/span')  # 媒体号
        #     sleep(2)
        #     self.plus.click('/html/body/div[5]/div/div/div/div/div[2]/div[1]/div/div')
        #     self.plus.click('/html/body/div[5]/div/div/div/div/div[3]/button[1]')

        self.plus.send_key('//*[@id="subtitle"]', 'subtitle')
        self.plus.send_key('//*[@id="author"]', 'author')
        self.plus.send_key('//*[@id="source"]', 'source')
        self.plus.send_key('//*[@id="originalLink"]', 'https://baidu.com')
        sleep(2)

    def test_12(self):
        '''新增通稿-右侧按钮验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[1]/div[2]/i')  # 新增关键词
        self.plus.send_key('//*[@id="input-keyword-add"]', 'keyword\n')
        sleep(2)
        list = []
        for i in range(len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[2]/div'))):
            list.append(self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[2]/div[{i + 1}]/div/span').text)  # 所有关键词放入list

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[1]/div[3]/i')  # 清空
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[2]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[1]/div[2]/i')
        self.plus.send_key('//*[@id="input-keyword-add"]', 'keyword\n')
        sleep(2)
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[2]/div[1]/div')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[2]/div[1]/div/i')  # 删除
        sleep(2)
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[2]/div').text
        keyword1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/key-words/div/div[1]/div[1]/i')  # 匹配关键词
        sleep(3)
        keyword2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]').text

        before1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[1]/div[1]/div[2]/i')  # 新增相关推荐
        sleep(2)
        self.plus.click('/html/body/div[5]/div/div/div/div[2]/div[4]/div[2]/div[2]/div[3]/span')
        self.plus.click('/html/body/div[5]/div/div/div/div[2]/div[4]/div[2]/div[3]/div[3]/span')
        self.plus.click('/html/body/div[5]/div/div/div/div[1]/i')
        after4 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div[1]/div/span')
        after5 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[1]/div[1]/div[1]/i')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[1]/content-relevant/div/div[1]/div[2]/button[2]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/aside[2]/div/div/div[3]/div[1]/img')  # 屏蔽词检测
        sleep(2)

        self.assertIn('keyword', list, '关键词新增失败')
        self.assertEqual('暂无内容', text2, '清空按钮失效')
        self.assertEqual('暂无内容', text3, '删除按钮失效')
        self.assertEqual(before1, after4 - 2, '相关推荐新增失败')
        self.assertEqual(after4, after5 + 1, '删除失败')
        self.assertNotEqual(keyword2, keyword1, '关键词匹配按钮失效')

    def test_13(self):
        '''新增页面底部按钮验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[1]')  # 预览
        sleep(3)
        length = len(self.plus.driver.find_elements(By.CSS_SELECTOR, "[ng-click='vm.goCopy()']"))
        if len(self.plus.finds("//span[.='退出版本预览']")) == 1:
            self.plus.click("//span[.='退出版本预览']")
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[3]')  # 保存
        sleep(5)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.assertEqual(text, '美国洛杉矶仇恨犯罪达近20年最高水平', '新增失败')
        self.assertEqual(length, 1, '新增页面预览功能失效')

    def test_14(self):
        '''更多按钮验证F'''
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[2]')  # 编辑
        sleep(5)
        self.plus.fc('#view > ui-view > div > main > div.form-content.hoge-flex > div.edit-bg > div > div.content > div.content-form-title > div > textarea').send_keys('1')
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[1]/div[1]/div/textarea').get_attribute('value')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[2]')  # 另存为
        sleep(5)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[3]')  # 预览链接
        sleep(2)
        text3 = self.plus.find('//*[@id="copy-text"]').get_attribute('value')
        sleep(2)
        self.plus.fc('.fa-remove').click()

        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[4]')  # 预览
        sleep(5)
        flag = 1
        for i in range(10):
            if len(self.plus.finds(f'/html/body/div[{i}]/div/div/div/button')) == 1:
                flag = 0
        self.plus.fc('.close > span').click()

        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[6]')  # 操作记录
        sleep(2)
        text4 = self.plus.find('//*[@id="history-version"]').text
        self.plus.click('/html/body/div[6]/div/div/div/div[1]/div[1]/div/i')

        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/div[4]')  # 定时发布
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.content-time-modal.in > div > div > div > div:nth-child(2) > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide-active > div > div:nth-child(6) > input[type=checkbox]').click()
        self.plus.find('/html/body/div[6]/div/div/div/div[3]/div[2]/div/div/div/div/div[2]/input').clear()
        self.plus.find('/html/body/div[6]/div/div/div/div[3]/div[2]/div/div/div/div/div[2]/input').send_keys((datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M"))
        sleep(2)
        self.plus.fc("[ng-click='vm.save()']").click()  # 保存
        sleep(3)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/span[2]'))

        text5 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[13]')  # 审核
        sleep(3)
        text6 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text

        text7 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[12]')  # 打回
        self.plus.click('/html/body/div[6]/div/div/div/div/div[3]/button[1]')
        sleep(5)
        text8 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text

        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[14]')  # 下载
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        if len(self.plus.finds('/html/body/pre')):  # 下载可能报错
            self.plus.driver.back()

        text9 = self.plus.find(base.first_).text
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[13]')  # 删除
        sleep(2)
        self.plus.fc("[ng-click='save()']").click()
        sleep(3)
        text10 = self.plus.find(base.first_).text

        self.assertEqual(text1, text2, '另存为按钮失效')
        self.assertNotEqual('', text4, '操作记录为空')
        self.assertEqual(length1, 1, '定时发布按钮失效')
        self.assertNotEqual(text5, text6, '审核按钮失效')
        self.assertNotEqual(text7, text8, '打回按钮失效')
        self.assertNotEqual(text9, text10, '删除按钮失效')
        self.assertNotEqual(file1, file2, '下载功能失效')
        self.assertNotEqual('', text3, '预览链接按钮失效')
        self.assertNotEqual(1, flag, '预览失败')

    def test_15(self):
        '''文稿底部按钮验证F'''
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[2]')
        sleep(8)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[2]')  # 另存为
        sleep(5)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[1]')  # 审核
        sleep(5)
        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[4]')  # 发布
        sleep(2)
        self.plus.click('/html/body/div[6]/div/div/div/div[3]/button[1]')
        self.plus.click('/html/body/div[7]/div/div/div/div[2]/div[1]/div[2]/ks-swiper-container/div/div[2]/div[1]/div/div[1]/input')
        self.plus.click('/html/body/div[7]/div/div/div/div[4]/button[2]')
        sleep(3)
        length = len(self.plus.finds(base.wengao_lanmu + '/span/a'))

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[2]')  # 打回
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(4)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        before = self.plus.find(base.first_).text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[5]')  # 移动
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.bulkCopy-contentmodal.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide-active > div > div:nth-child(3) > input[type=checkbox]').click()
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.bulkCopy-contentmodal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-binding.ng-isolate-scope').click()
        sleep(4)
        after = self.plus.find(base.first_).text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        text3 = self.plus.find(base.first_).text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(2)
        self.plus.click('/html/body/div[6]/div/div/div/div/div[3]/button[1]')
        sleep(5)
        text4 = self.plus.find(base.first_).text

        self.assertNotEqual(text1, '待审核', '底部审核按钮失效')
        self.assertEqual(text2, '已打回', '底部打回按钮失效')
        self.assertNotEqual(before, after, '底部移动功能失效')
        self.assertNotEqual(text3, text4, '底部删除按钮失效')
        self.assertEqual(length, 1, '文稿另存为后审核发布，发布的栏目未出现')

    def test_16(self):
        '''文稿底部按钮验证'''
        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click(base.more_button11)
        self.plus.click(base.more_button11 + '/div/div/div/button[2]')
        sleep(8)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div[2]/div[1]/div/div[2]/button[2]')  # 另存为
        sleep(5)

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[9]')  # 选择栏目
        sleep(2)
        self.plus.fc("[type='submit']").click()
        sleep(2)
        self.plus.click('/html/body/div[7]/div/div/div/div[2]/div[1]/div[2]/ks-swiper-container/div/div[2]/div/div/div[5]/input')
        self.plus.click('/html/body/div[7]/div/div/div/div[3]/button[1]')
        sleep(2)
        text1 = self.plus.find(base.wengao_lanmu + '/span/a').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[8]')  # 提审
        sleep(4)
        self.plus.click('/html/body/div[6]/div/div/div/div[2]/div[2]/button[2]')
        sleep(4)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[5]/div/span').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[10]')  # 设置标签
        sleep(2)
        self.plus.click('/html/body/div[6]/div/div/div/div[2]/div[1]/div[2]/div[1]/input')
        self.plus.click('/html/body/div[6]/div/div/div/div[3]/button[1]')
        sleep(2)
        length = len(self.plus.finds(base.status))

        self.assertEqual(text1, '发现', '选择栏目按钮失效')
        self.assertEqual(text2, '审核中', '提审按钮失效')
        self.assertEqual(length, 1, '设置标签按钮失效')
