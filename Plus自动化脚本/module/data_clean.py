from Plus自动化脚本.base import *
import unittest


class test(unittest.TestCase, base):
    '''清除测试数据'''

    @classmethod
    def setUpClass(self) -> None:
        self.plus = base('文稿')

    @classmethod
    def tearDownClass(self) -> None:
        self.plus.driver.quit()

    def test_01(self):
        # 3,1,0,1,4,2

        # 删除新增的稿件
        # 文稿
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(1)
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(3)

        # 图集
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '图集').click()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(1)
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')
        sleep(3)

        # 专题
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '专题').click()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(1)
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')  # 删除
        sleep(3)

        # 视频
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '视频').click()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[4]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(1)
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')  # 删除
        sleep(3)

        # 音频
        self.plus.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.plus.driver.find_element(By.LINK_TEXT, '音频').click()
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/label/input')
        self.plus.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[3]')  # 删除
        sleep(1)
        self.plus.click('/html/body/div[4]/div/div/div/div/div[3]/button[1]')  # 删除
        sleep(3)

        # 若存在则清除用户模块中的用户 name、示例账户
        pass
