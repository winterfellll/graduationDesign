import datetime, unittest, random, os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains as ac, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pathlib import Path

projectPath = Path(__file__).parent.parent  # 获取当前项目的路径
assetsPath = str(projectPath) + '/Plus自动化脚本/assets/'

path = '/Users/hoge/Downloads'
video_path = assetsPath + '武汉女生收集了1500多张核酸检测卡 想把各种款式集齐.mp4'
picture_path = assetsPath + '1.jpg'
music_path = assetsPath + '丰收电台.mp3'
user_import_path = assetsPath + '1.xls'


# v1.7.5.1.0
class base():
    wengao_lanmu = '/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]'
    qita_lanmu = '/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[7]'

    def __init__(self, module):
        # 无头模式启动
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument("--window-size=1920,1080")
        # prefs = {'download.default_directory': '/Users/hoge/Documents/file/rubbish', 'profile.password_manager_enabled': False, 'download.prompt_for_download': False}
        # options.add_experimental_option('prefs', prefs)
        # self.driver = webdriver.Chrome(options=options)

        self.driver = webdriver.Chrome()
        self.driver.get('http://demo-xingyun.hogeos.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.send_key('/html/body/div[1]/div[1]/div[1]/div/form/div[2]/div/input', 'liujifeng')
        self.send_key('/html/body/div[1]/div[1]/div[1]/div/form/div[3]/div/div/input', 'ljfHoge@2022\n')
        sleep(1)
        self.click('/html/body/div/div[1]/div[5]/div/div[3]/div[1]/div/img')
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        sleep(5)
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.driver.find_element(By.LINK_TEXT, module).click()
        sleep(5)

    def find(self, ele):
        element = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        return element

    def finds(self, ele):
        return self.driver.find_elements(By.XPATH, ele)

    def click(self, ele):
        self.find(ele).click()

    def send_key(self, ele, data):
        self.find(ele).send_keys(data)

    def fc(self, ele):
        element = self.driver.find_element(By.CSS_SELECTOR, ele)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        return element

    def tishen(self):
        # 提审一条文稿
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a')  # 文稿
        sleep(5)
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/i')
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div/div/button[7]')  # 提审
        sleep(2)
        self.click('/html/body/div[4]/div/div/div/div[2]/div[2]/button[2]')
        sleep(2)
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/div/div[2]/div[6]/ul/li[4]/a')
        sleep(3)

    def fabu(self):
        # 发布一条文稿
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[7]/i')
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a')  # 文稿
        sleep(5)
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[1]')  # 审核
        sleep(3)
        ac(self.driver).scroll_by_amount(0, -500).perform()
        sleep(2)
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/label/input')
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[11]/div[2]/div/button[4]')  # 发布
        sleep(2)
        self.fc("[type='submit']").click()
        sleep(3)
        self.fc("[data='5']").click()
        self.fc("[ng-click='vm.save()'][type='button']").click()
        sleep(3)

    def category_1(self):
        '''分类管理跳转'''
        ele = self.find('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span[1]')
        ac(self.driver).move_to_element(ele).perform()
        self.click('/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/a[2]')
        sleep(5)

        # 分类中有测试分类时删除该分类
        length = len(self.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div'))
        for i in range(length):
            if '测试分类' in self.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{i + 1}]').text:
                ac(self.driver).move_to_element(self.find(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{i + 1}]')).perform()
                self.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{i + 1}]/div[2]/i[2]')
                self.fc('.btn-sure').click()
                sleep(3)

        self.text = self.find('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]').text

    def category_2(self):
        '''分类管理页面功能验证'''
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[1]/div[2]/span')
        sleep(2)
        self.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', '测试分类' + str(random.randint(0, 100)))
        sleep(2)
        self.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[1]')
        self.click('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[2]/div[1]/div[2]/span')
        self.click('/html/body/div[3]/div/div/form/div[3]/button[2]')
        ele = self.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div')
        ac(self.driver).move_to_element(ele[-1]).perform()
        self.before = ele[-1].text
        self.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[2]/i[1]')  # 编辑按钮
        sleep(1)
        self.send_key('/html/body/div[3]/div/div/form/div[2]/div[1]/input', Keys.BACK_SPACE)
        sleep(2)
        self.click('/html/body/div[3]/div/div/form/div[3]/button[1]')
        sleep(2)
        self.after = ele[-1].text
        self.length1 = len(self.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div'))
        ac(self.driver).move_to_element(ele[-1]).perform()
        self.click(f'/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div[{len(ele)}]/div[2]/i[2]')  # 删除按钮
        self.click('/html/body/div[3]/div/div/div/div/div[3]/button[1]')  # 确认删除
        sleep(2)
        self.length2 = len(self.finds('/html/body/div[1]/div[2]/div[3]/ui-view/div/div[2]/ks-swiper-container/div/div[2]/div[1]/div[3]/div'))
