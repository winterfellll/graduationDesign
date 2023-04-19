from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase):
    '''1F'''

    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('音频')

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
        '''音频页面分类按钮、筛选框、搜索框验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        sleep(3)
        before1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[2]/div/div[2]/div/div')
        sleep(3)
        after1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[1]/classify-sidebar/div/div[1]/span')  # 全部
        sleep(2)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[2]')
        sleep(2)
        after2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button[1]')
        sleep(3)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/button')  # 全部状态按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a[5]')
        sleep(4)
        after4 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/button')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a[1]')
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
        self.assertNotEqual(before1, after4, '状态按钮切换失败')
        self.assertNotEqual(before1, after5, '时间按钮切换失败')

    def test_04(self):
        '''搜索功能验证'''
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div'))
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/search-box/div[1]/input', '国家\n')  # 搜索框
        sleep(2)
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/search-box/div[1]/i[1]')
        sleep(2)
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
        sleep(3)

        self.assertNotEqual(length1, length2, '搜索功能无法正常使用')
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
        before1 = self.plus.find(base.first_).text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/page-nation/div/div[2]/div[1]/button[3]')  # 翻页按钮
        sleep(2)
        after1 = self.plus.find(base.first_).text

        self.assertNotEqual(before1, after1, '翻页按钮失效')

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
        '''新增音频-返回按钮和取消按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button[2]')
        sleep(5)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/nav/div/div/div[1]/span')  # 返回按钮验证
        sleep(2)
        if len(self.plus.finds('/html/body/div[3]/div/div/div/div/div[3]/button[1]')) == 1:
            self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
            sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button[2]')
        sleep(3)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/content-save/div/div/div/button[2]')  # 取消按钮验证
        sleep(2)
        if len(self.plus.finds('/html/body/div[3]/div/div/div/div/div[3]/button[1]')) == 1:
            self.plus.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')
            sleep(2)

    def test_10(self):
        '''新增音频-标题和图片'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button[2]')
        sleep(3)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[1]/div/input', 'test')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div/div[1]/div/div/div/div/img')
        self.plus.send_key('//*[@id="audioInput"]', music_path)
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.contentUpload-Model.in > div > div > div > div.modal-footer > button.btn.primary-btn').click()  # 确认
        length = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div/div[1]/div/div/span[2]'))

        self.assertNotEqual(length, 0, '文件选择失败')

    def test_11(self):
        '''新增音频-左侧按钮验证'''
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
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[1]/div/content-attr/div/div[2]/div[2]/div/div/div/div[7]')  # 裁剪按钮
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

        self.plus.fc(".md-input").click()  # 分类
        self.plus.fc(".list-group > li:nth-of-type(3) > .group-item").click()
        self.plus.fc(".select-color").click()  # 栏目
        self.plus.fc("[data='5']").click()
        self.plus.fc("[ng-click='vm.save()']").click()
        sleep(2)
        self.plus.fc("[title='点击添加到专题']").click()  # 专题
        sleep(2)
        self.plus.fc(".btn[ng-click='vm.close()']").click()
        self.plus.fc('.switch-close').click()  # 评论
        self.plus.send_key('//*[@id="subtitle"]', 'subtitle')
        self.plus.send_key('//*[@id="edit"]', 'edit')
        self.plus.send_key('//*[@id="source"]', 'source')
        self.plus.send_key('//*[@id="originalLink"]', 'https://baidu.com')
        sleep(2)

    def test_12(self):
        '''新增音频-右侧按钮验证F'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[1]/div[2]/i')  # 新增关键词
        self.plus.send_key('//*[@id="input-keyword-add"]', 'keyword\n')
        sleep(2)
        list = []
        for i in range(len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]/div'))):
            list.append(self.plus.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]/div[{i + 1}]/div/span').text)  # 所有关键词放入list

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[1]/div[3]/i')  # 清空
        sleep(2)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]/div').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[1]/div[2]/i')
        self.plus.send_key('//*[@id="input-keyword-add"]', 'keyword\n')
        sleep(2)
        ac(self.plus.driver).move_to_element(self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]/div/div')).perform()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]/div/div/i')  # 删除
        text3 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]/div').text
        keyword1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[1]/div[1]/i')  # 匹配关键词
        sleep(2)
        keyword2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/key-words/div/div[2]').text

        before1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div[1]/content-relevant/div/div[1]/div[1]/div[2]/i')  # 新增相关推荐
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.relevant-modal.in > div > div > div > div.modal-body > div.form-group.ng-isolate-scope > div.modal-list.ng-scope > div:nth-child(2) > div.icon-box > span').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.relevant-modal.in > div > div > div > div.modal-body > div.form-group.ng-isolate-scope > div.modal-list.ng-scope > div:nth-child(3) > div.icon-box > span').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.relevant-modal.in > div > div > div > div.modal-header > i').click()
        after4 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div'))
        self.plus.click('/html/body/div/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div/content-relevant/div/div[2]/div/div/div/span')
        after5 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div[1]/content-relevant/div/div[2]/div/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div[1]/content-relevant/div/div[1]/div[1]/div[1]/i')  # 排序
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/aside[2]/div/div/div[1]/content-relevant/div/div[1]/div[2]/button[2]')

        self.assertIn('keyword', list, '关键词新增失败')
        self.assertEqual('暂无内容', text2, '清空按钮失效')
        self.assertEqual('暂无内容', text3, '关键词删除按钮失效')
        self.assertEqual(before1, after4 - 2, '相关推荐新增失败')
        self.assertEqual(after4, after5 + 1, '相关推荐删除失败')
        self.assertNotEqual(keyword1, keyword2, '匹配关键词按钮失效')

    def test_13(self):
        '''新增音频内部功能验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div/div[1]/div/div/span[2]/span[2]')  # 删除按钮
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div/div[1]/div/div/div/div/img')
        self.plus.send_key('//*[@id="audioInput"]', music_path)
        sleep(3)
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/content-save/div/div/div/button[1]')  # 保存
        sleep(8)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.assertEqual(text, '丰收电台', '新增失败')

    def test_14(self):
        '''更多按钮验证'''

        text1 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text
        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[4]')  # 编辑
        sleep(5)
        self.plus.fc('.attrChange').send_keys('1')
        sleep(2)
        self.plus.fc('#vm\.audioId > div > div > div > button.btn.primary-btn.save-btn.ng-isolate-scope').click()  # 保存
        sleep(5)
        text2 = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/a/span').text

        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[5]')  # 预览链接
        sleep(2)
        text3 = self.plus.find('//*[@id="copy-text"]').get_attribute('value')
        sleep(2)
        self.plus.fc('.fa-remove').click()

        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[8]')  # 操作记录
        sleep(2)
        text4 = self.plus.find('//*[@id="history-version"]').text
        self.plus.fc('.close-btn').click()

        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/div[4]')  # 定时发布
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.content-time-modal.in > div > div > div > div:nth-child(2) > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide-active > div > div:nth-child(4) > input[type=checkbox]').click()
        self.plus.find('/html/body/div[4]/div/div/div/div[3]/div[2]/div/div/div/div/div[2]/input').clear()
        self.plus.find('/html/body/div[4]/div/div/div/div[3]/div[2]/div/div/div/div/div[2]/input').send_keys((datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M"))
        sleep(2)
        self.plus.fc("[ng-click='vm.save()']").click()  # 保存
        sleep(2)
        length1 = len(self.plus.finds(base.qita_lanmu + '/span[2]'))

        text5 = self.plus.find(base.status).text
        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[15]')  # 审核
        sleep(3)
        text6 = self.plus.find(base.status).text

        text7 = self.plus.find(base.status).text
        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[14]')  # 打回
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(5)
        text8 = self.plus.find(base.status).text

        text9 = self.plus.find(base.first_).text
        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[15]')  # 删除
        self.plus.fc('div.modal-footer:nth-child(3) > button:nth-child(1)').click()
        sleep(3)
        text10 = self.plus.find(base.first_).text

        self.assertNotEqual(text1, text2, '编辑按钮失效')
        self.assertNotEqual('', text4, '操作记录为空')
        self.assertEqual(length1, 1, '定时发布按钮失效')
        self.assertNotEqual(text5, text6, '审核按钮失效')
        self.assertNotEqual(text7, text8, '打回按钮失效')
        self.assertNotEqual(text9, text10, '删除按钮失效')
        self.assertNotEqual(text3, '', '预览链接按钮失效')
        self.assertNotEqual(text3, '加载中...', '预览链接按钮失效')

    def test_15(self):
        '''更多-下载按钮验证'''
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[2]')  # 下载
        sleep(10)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        self.assertNotEqual(file1, file2, '下载失败')

    def test_16(self):
        '''更多-预览按钮验证'''
        self.plus.click(base.more_button10)
        self.plus.click(base.more_button10 + '/div/div/div/button[6]')  # 预览
        sleep(5)
        length = len(self.plus.driver.find_elements(By.CSS_SELECTOR, "[ng-click='vm.goCopy()']"))  # 复制链接按钮
        self.plus.fc('.close > span').click()
        sleep(3)

        self.assertNotEqual(0, length, '预览失败')

    def test_17(self):
        '''批量上传验证'''
        text1 = self.plus.fc(
            '#view > ui-view > div > div.mxu_side_wrapper.mxu_content_wrapper.ng-scope > div.member-cont.second-view > div > div > div > div.hoge-flex > div > div.list.white.border-bottom-radius.ng-pristine.ng-untouched.ng-valid.ng-not-empty > div.list_bottom.hoge-table-bottom.border-bottom-radius > page-nation > div > span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button[1]')  # 批量上传
        self.plus.send_key('//*[@id="input-inner"]', music_path)
        sleep(2)
        length1 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[3]/div/div/div/div[3]/div[2]/div'))
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[3]/div/div/div/div[3]/div[2]/div/div[7]/i')  # 删除
        length2 = len(self.plus.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[3]/div/div/div/div[3]/div[2]/div'))
        self.plus.send_key('//*[@id="input-inner"]', music_path)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[3]/div/div/div/div[4]/button')  # 上传
        sleep(5)
        text = self.plus.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[3]/div/div/div/div[3]/div[2]/div/div[3]/span/span').text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[3]/div/div/div/div[1]/i[2]')
        sleep(3)
        text2 = self.plus.fc(
            '#view > ui-view > div > div.mxu_side_wrapper.mxu_content_wrapper.ng-scope > div.member-cont.second-view > div > div > div > div.hoge-flex > div > div.list.white.border-bottom-radius.ng-pristine.ng-untouched.ng-valid.ng-not-empty > div.list_bottom.hoge-table-bottom.border-bottom-radius > page-nation > div > span').text

        self.assertNotEqual(length1, length2, '批量上传页面删除按钮失效')
        self.assertNotEqual(text, '上传失败', '批量上传功能异常')

    def test_18(self):
        '''音频底部按钮验证'''
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button[2]')
        sleep(5)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[1]/div/input', '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div/div[1]/div/div/div/div/img')
        sleep(2)
        self.plus.send_key('//*[@id="audioInput"]', music_path)
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/content-save/div/div/div/button[1]')  # 保存
        sleep(5)

        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[1]')  # 审核
        sleep(5)
        text1 = self.plus.find(base.status).text

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
        text2 = self.plus.find(base.status).text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        before = self.plus.find(base.first_).text
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[5]')  # 移动
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.bulkCopy-contentmodal.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide-active > div > div:nth-child(2) > input[type=checkbox]').click()
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
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.conformModal.in > div > div > div > div > div.modal-footer > button.btn.btn-sure.p-x-md.ng-binding').click()
        sleep(5)
        text4 = self.plus.find(base.first_).text

        self.assertEqual(text1, '已审核', '底部审核按钮失效')
        self.assertEqual(text2, '已打回', '底部打回按钮失效')
        self.assertNotEqual(before, after, '底部移动功能失效')
        self.assertNotEqual(text3, text4, '底部删除按钮失效')
        self.assertEqual(length, 1, '发布的栏目未出现')

    def test_19(self):
        '''音频底部按钮验证'''
        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[1]/div[2]/button[2]')
        sleep(5)
        self.plus.send_key('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[1]/div/input', '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/div[2]/div/div[1]/div/div/div/div/img')
        sleep(2)
        self.plus.send_key('//*[@id="audioInput"]', music_path)
        sleep(2)
        self.plus.click('/html/body/div[3]/div/div/div/div[3]/button[2]')
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/main/div/div/div/content-save/div/div/div/button[1]')  # 保存
        sleep(5)

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        file1 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[7]')  # 下载
        sleep(3)
        file2 = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[10]')  # 选择栏目
        sleep(2)
        self.plus.fc("[type='submit']").click()
        sleep(2)
        self.plus.fc(
            'body > div.modal.fade.ng-isolate-scope.content-publish-modal.in > div > div > div > div.modal-body > div.column-wrap > div.column_content.ng-isolate-scope > ks-swiper-container > div > div.swiper-wrapper > div.swiper-slide.list_box.swiper-slide.swiper-slide-active > div > div:nth-child(5) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.content-publish-modal.in > div > div > div > div.modal-footer > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)
        text1 = self.plus.find(base.qita_lanmu + '/span/a').text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[9]')  # 提审
        sleep(4)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.showAudit.in > div > div > div > div.body-audit.ng-scope > div.modal-footer > button.btn.btn-primary.button.ng-scope').click()
        sleep(4)
        text2 = self.plus.find(base.status).text

        ac(self.plus.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[11]')  # 设置标签
        sleep(2)
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.setLabel-modal.in > div > div > div > div.modal-body > div.column-wrap > div.item-content > div:nth-child(1) > input[type=checkbox]').click()
        self.plus.fc('body > div.modal.fade.ng-isolate-scope.setLabel-modal.in > div > div > div > div.modal-footer.flex-item > button.btn.primary-btn.ng-isolate-scope').click()
        sleep(2)
        length = len(self.plus.finds(base.status))

        self.assertNotEqual(file1, file2, '下载按钮失效')
        self.assertEqual(text1, '发现', '选择栏目按钮失效')
        self.assertEqual(text2, '审核中', '提审按钮失效')
        self.assertEqual(length, 1, '设置标签按钮失效')
