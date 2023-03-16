import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.get('http://demo-xingyun.hogeos.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/form/div[2]/div/input').send_keys('liujifeng')
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/form/div[3]/div/div/input').send_keys('ljfHoge@2022\n')
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div/div[1]/div[1]/div/img').click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        sleep(5)

    @classmethod
    def tearDownClass(self) -> None:
        sleep(2)
        driver.quit()

    # 商品管理
    # 供应商
    def test_1_spgl_01(self):
        """ 筛选下拉框校验 """
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div[1]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/a[2]').click()
        sleep(2)
        text1 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div[1]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/a[3]').click()
        sleep(2)
        text2 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div[1]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/a[1]').click()
        sleep(2)

        self.assertNotEqual(text1, '', '筛选为空')
        self.assertNotEqual(text2, '', '筛选为空')

    # 商品类型
    def test_1_spgl_02(self):
        """ 筛选下拉框校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/a[2]').click()
        sleep(2)
        text1 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/a[3]').click()
        sleep(2)
        text2 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/a[1]').click()
        sleep(2)

        self.assertNotEqual(text1, '', '筛选为空')
        self.assertNotEqual(text2, '', '筛选为空')

    # 商品分类
    def test_1_spgl_03(self):
        """ 筛选下拉框校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/div/a[2]').click()
        sleep(2)
        text1 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/div/a[6]').click()
        sleep(2)
        text2 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/div/a[1]').click()
        sleep(2)

        self.assertNotEqual(text1, '', '筛选为空')
        self.assertNotEqual(text2, '', '筛选为空')

    # 商品状态
    def test_1_spgl_04(self):
        """ 筛选下拉框校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/div/a[2]').click()
        sleep(2)
        text1 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/div/a[3]').click()
        sleep(2)
        text2 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/div/a[1]').click()
        sleep(2)

        self.assertNotEqual(text1, '', '筛选为空')
        self.assertNotEqual(text2, '', '筛选为空')

    # 兑换类型
    def test_1_spgl_05(self):
        """ 筛选下拉框校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/div/a[2]').click()
        sleep(2)
        text1 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/div/a[3]').click()
        sleep(2)
        text2 = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/div/a[1]').click()
        sleep(2)

        self.assertNotEqual(text1, '', '筛选为空')
        self.assertNotEqual(text2, '', '筛选为空')

    # 搜索框
    def test_1_spgl_06(self):
        """ 搜索框校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[6]/div/input').send_keys('天')
        sleep(2)
        a = driver.find_element(By.XPATH, '//*[@id="allActivities"]/ul/li[1]/div[2]/div/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[6]/div/input').clear()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[6]/div/span/button').click()
        sleep(1)
        self.assertNotEqual(a, '', '筛选为空')

    # 新增商品按钮
    def test_1_spgl_07(self):
        """ 新增商品按钮校验 """
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[7]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[5]/div[2]/span').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[7]/button').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/input[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/input[1]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/input').send_keys('商品1')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[4]/div[2]/input[2]').click()
        select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[5]/div[2]/select'))
        sleep(1)
        select.select_by_visible_text("玩具")
        sleep(1)
        select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[6]/div[2]/select'))
        sleep(1)
        select.select_by_visible_text("厚建软件公司")
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[7]/div[2]/input').clear()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[7]/div[2]/input').send_keys('10')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[8]/div[2]/div').click()
        sleep(3)
        pyautogui.click(1400, 270)  # 搜索
        sleep(2)
        pyautogui.typewrite('jpg')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        sleep(2)
        pyautogui.click(700, 400)  # 选择图片
        sleep(1)
        pyautogui.click(1400, 850)
        sleep(2)
        driver.switch_to.frame('ueditor_2')
        driver.find_element(By.XPATH, '/html/body').send_keys('111')
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[3]/div[2]/input').send_keys('100')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[4]/div[2]/div[2]/input').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[4]/div[2]/div[1]/input').click()
        sleep(1)
        driver.switch_to.frame('ueditor_3')
        driver.find_element(By.XPATH, '/html/body').send_keys('111')
        sleep(1)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[5]/div[1]/span').click()
        sleep(8)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        self.assertNotEqual(before, after, '新增失败')

    # 按钮
    # 上下架按钮
    def test_1_spgl_08(self):
        """ 上下架按钮校验 """
        before = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[9]/span').text
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[9]/span').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(3)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[9]/span').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(3)
        after = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[9]/span').text
        self.assertEqual(before, after, '状态修改失败')

    # 选择按钮
    def test_1_spgl_09(self):
        """ 单选按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]/label/input').click()
        checked = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]/label/input').get_attribute('checked')
        sleep(2)
        self.assertEqual(checked, 'true', '选中失败')

    # 全选按钮
    def test_1_spgl_10(self):
        """ 全选按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/label/input').click()
        sleep(2)
        list = []
        for i in range(10):
            list.append(driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[{i + 1}]/div[1]/label/input').get_attribute('checked'))
            self.assertEqual(list[i], 'true', '全选失败')
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/label/input').click()
        sleep(2)

    # 上下架按钮
    def test_1_spgl_11(self):
        """ 上下架按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]/label/input').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/button[3]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(3)
        text1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[9]/span').text

        sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]/label/input').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/button[2]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(3)
        text2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[9]/span').text
        self.assertEqual(text1, '已下架', '下架按钮失效')
        self.assertEqual(text2, '已上架', '上架按钮失效')

    def test_1_spgl_12(self):
        """ 每页XXX条记录按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/a[1]').click()
        sleep(2)
        list = driver.find_elements(By.XPATH, '//*[@id="allActivities"]/ul/li[6]/div[2]/div/div[1]')
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/a[2]').click()
        sleep(1)
        self.assertEqual(len(list), 0, '每页XXX条记录按钮失效')

    # 翻页按钮
    def test_1_spgl_13(self):
        """ 翻页按钮校验 """
        product1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[10]/div[2]/div/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/button[2]').click()
        sleep(1)
        product2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[10]/div[2]/div/div[1]').text
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/button[1]').click()
        sleep(1)
        product3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[10]/div[2]/div/div[1]').text
        self.assertNotEqual(product1, product2, '下一页按钮失效')
        self.assertNotEqual(product3, product2, '上一页按钮失效')

    # 编辑按钮
    def test_1_spgl_14(self):
        """ 编辑按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[10]/span[1]').click()
        sleep(1)
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/input').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/input').send_keys('1')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[5]/div[1]/span').click()
        sleep(6)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[10]/span[1]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/input').send_keys(Keys.BACK_SPACE)
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[5]/div[1]/span').click()
        sleep(7)
        self.assertNotEqual(before, after, '编辑按钮失效')

    # 日志按钮
    def test_1_spgl_15(self):
        """ 日志按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[10]/a').click()
        sleep(5)
        a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]').text
        b = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/ul/li/div[1]/a').text
        driver.back()
        sleep(5)
        self.assertNotEqual(a, '', '日志按钮失效')
        self.assertNotEqual(b, '', '日志为空')

    # 删除按钮
    def test_1_spgl_16(self):
        """ 删除按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]/label/input').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/button[1]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-cancel.wd80').click()
        sleep(2)

        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[10]/span[2]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(5)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        self.assertNotEqual(before, after, '删除失败')

    # 排序按钮
    def test_1_spgl_17(self):
        """ 排序按钮校验 """
        before1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/a').click()
        sleep(1)
        el = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/img')
        ac(driver).drag_and_drop_by_offset(el, 10, 600).perform()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[11]/a[1]').click()
        sleep(1)
        after1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text

        before2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[1]/a').click()
        sleep(1)
        el = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/img')
        ac(driver).drag_and_drop_by_offset(el, 10, 600).perform()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[11]/a[2]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[11]/a[2]').click()
        sleep(5)
        after2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[2]/div/div[1]').text
        self.assertEqual(before1, after1, '排序的退出按钮失效')
        self.assertNotEqual(before2, after2, '排序功能失效')

    # 供应商列表
    def test_2_gyslb_01(self):
        """ 每页XXX条记录按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button').text
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/a[1]').click()
        sleep(1)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/button').text
        self.assertNotEqual(before, after, '每页XXX条记录按钮失效')

    # 搜索框
    def test_2_gyslb_02(self):
        """ 搜索框校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/input').send_keys('中百')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/span/button').click()
        sleep(1)
        a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/input').clear()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/span/button').click()
        sleep(1)
        self.assertEqual(a, '中百集团')

    # 新增供货商按钮
    def test_2_gyslb_03(self):
        """ 新增供货商按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/button').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/input').send_keys('供货商1')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[3]/div/div/div[1]/span').click()
        sleep(7)
        a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]').text
        self.assertEqual(a, '供货商1', '新增失败')

    # 详情按钮
    def test_2_gyslb_04(self):
        """ 详情按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[2]/div[3]/span[1]').click()
        sleep(1)
        a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/ul/li/div[1]').text
        self.assertNotEqual(a, '', '详情页信息不能正常展示')

    # 详情页
    def test_2_gyslb_05(self):
        """ 详情页检测 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[3]/span[1]').click()
        sleep(1)
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/div[2]/div').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/div[2]/span').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/div[2]/input').send_keys('1')
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]').click()
        sleep(7)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/div[2]/div').text

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/button').click()
        sleep(2)
        pyautogui.click(900, 330)
        pyautogui.typewrite('zhijiang street 888')
        pyautogui.click(900, 440)
        pyautogui.typewrite('zhangsan')
        pyautogui.click(900, 490)
        pyautogui.typewrite('13211112222')
        pyautogui.click(900, 565)
        sleep(2)
        pyautogui.click(950, 360)
        pyautogui.typewrite('112222')
        pyautogui.click(950, 410)
        pyautogui.typewrite('13211112222')
        pyautogui.click(1000, 570)
        sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[6]/span[1]').click()  # 编辑
        sleep(1)
        pyautogui.click(1000, 330)
        pyautogui.typewrite('1')
        pyautogui.click(920, 550)
        pyautogui.click(1000, 420)
        pyautogui.typewrite('123321')
        pyautogui.click(1000, 560)
        sleep(3)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[6]/a').click()  # 日志
        sleep(2)
        text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]').text
        driver.back()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[3]/span[1]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/ul/li[1]/div[6]/span[2]').click()  # 删除
        sleep(2)
        pyautogui.click(1100, 420)
        sleep(3)

        self.assertNotEqual(before, after, '无法正常修改供应商名称')
        self.assertNotEqual(text, '暂无数据', '日志为空')

    # 日志按钮
    def test_2_gyslb_06(self):
        """ 日志按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[3]/a').click()
        sleep(1)
        a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]').text
        driver.back()
        sleep(1)
        self.assertNotEqual(a, '', '日志按钮失效')

    # 删除按钮
    def test_2_gyslb_07(self):
        """ 删除按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[2]/a').click()
        sleep(1)
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[3]/span[2]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.ng-isolate-scope.in > div > div > div > div.modal-footer > button.btn.btn-sure.btn-danger.wd80').click()
        sleep(5)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div/ul/li[1]/div[1]').text
        self.assertNotEqual(before, after, '删除失败')

    # 核销列表
    def test_3_hxlb(self):
        """ 核销列表校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[3]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/a[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/a[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/button/span[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[3]/div/a[3]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/button/span[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[4]/div/a[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[5]/div/input').send_keys('天')
        sleep(1)
        pyautogui.click(1000, 180)
        sleep(1)
        pyautogui.click(1000, 300)
        sleep(1)
        pyautogui.click(1200, 180)
        sleep(1)
        pyautogui.click(1200, 400)
        sleep(2)

    # 订单管理
    def test_4_ddgl(self):
        """ 订单管理校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[4]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/a[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/a[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[3]/button/span[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[3]/div/a[3]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[4]/button/span[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[4]/div/a[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[5]/div/input').send_keys('天')
        sleep(1)
        pyautogui.click(1000, 180)
        sleep(1)
        pyautogui.click(1000, 300)
        sleep(1)
        pyautogui.click(1200, 180)
        sleep(1)
        pyautogui.click(1200, 400)
        sleep(2)

    # 分类管理
    # 排序按钮
    def test_5_flgl_01(self):
        """ 排序按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        sleep(1)
        before1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[1]/a').click()
        sleep(3)
        sleep(1)
        pyautogui.moveTo(600, 300)
        pyautogui.mouseDown()
        pyautogui.dragTo(600, 520, duration=1, button='left')
        pyautogui.mouseUp()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[6]/a[1]').click()
        sleep(1)
        after1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text

        before2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[1]/a').click()
        sleep(1)
        pyautogui.moveTo(600, 300)
        pyautogui.mouseDown()
        pyautogui.dragTo(600, 520, duration=1, button='left')
        pyautogui.mouseUp()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[6]/a[2]').click()
        sleep(5)
        after2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        self.assertEqual(before1, after1, '排序的退出按钮失效')
        self.assertNotEqual(before2, after2, '排序功能失效')

    # 选择按钮
    def test_5_flgl_02(self):
        """ 单选按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[1]/label/input').click()
        checked = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[1]/label/input').get_attribute('checked')
        sleep(2)
        self.assertEqual(checked, 'true', '选中失败')

    # 全选按钮
    def test_5_flgl_03(self):
        """ 全选按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/label/input').click()
        sleep(2)
        list = []
        length = len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li'))
        for i in range(length):
            list.append(driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[{i + 1}]/div[1]/label/input').get_attribute('checked'))
            self.assertEqual(list[i], 'true', '全选失败')

    # 新增分类
    def test_5_flgl_04(self):
        """ 新增分类按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        sleep(1)
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/button').click()
        sleep(1)
        pyautogui.click(900, 300)
        pyautogui.typewrite('class1')
        sleep(1)
        pyautogui.click(1000, 640)
        sleep(7)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        self.assertNotEqual(before, after, '新增失败')

    # 编辑按钮
    def test_5_flgl_05(self):
        """ 编辑按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        sleep(1)
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        pyautogui.click(1827, 314)
        sleep(1)
        pyautogui.click(900, 300)
        pyautogui.typewrite('123')
        sleep(1)
        pyautogui.click(1000, 640)
        sleep(7)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        self.assertNotEqual(before, after, '修改失败')

    # 删除按钮
    def test_5_flgl_06(self):
        """ 删除按钮校验 """
        driver.refresh()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        sleep(1)
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        pyautogui.moveTo(1874, 311)
        pyautogui.click(1874, 311)
        sleep(1)
        pyautogui.click(1000, 420)
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[1]/label/input').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/button').click()
        sleep(1)
        pyautogui.click(1100, 420)
        sleep(7)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/ul/li[1]/div[3]').text
        self.assertNotEqual(before, after, '删除失败')

    # 日志按钮
    def test_5_flgl_07(self):
        """ 日志按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        sleep(1)
        pyautogui.moveTo(1850, 310)
        pyautogui.click(1850, 310)
        sleep(1)
        a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/ul/li[1]/div[1]/a').text
        driver.back()
        sleep(2)
        self.assertNotEqual(a, '', '日志为空')

    def test_5_flgl_08(self):
        """ 每页XXX条记录按钮校验 """
        driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/ul/li[5]/a').click()
        before = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/button').text
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/button').click()
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/a[1]').click()
        sleep(1)
        after = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/button').text
        self.assertNotEqual(before, after, '每页XXX条记录按钮失效')
