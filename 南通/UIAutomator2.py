import uiautomator2
from time import sleep
import unittest


# 环境搭建及使用 https://blog.csdn.net/m0_37602827/article/details/108249779
# 启动inspector  python -m weditor

# 存在则点击
def exist_and_click(ele_xpath):
    if d.xpath(ele_xpath).exists:
        d.xpath(ele_xpath).click()
        sleep(2)


# 点击后休眠
def click_with_sleep(ele_xpath, time=1):
    d.xpath(ele_xpath).click()
    d.sleep(time)


def exist(ele_xpath):
    return d.xpath(ele_xpath).exists


def launch():
    d.app_start("com.cutv.mobile.zsntclient")
    sleep(2)
    exist_and_click('//*[@resource-id="android:id/button1"]')  # 允许发送通知
    sleep(1)
    exist_and_click('//*[@resource-id="com.cutv.mobile.zsntclient:id/txt_i_know"]')  # 同意并继续
    sleep(1)
    d.click(0.913, 0.036)  # 右上角开屏广告
    sleep(2)
    exist_and_click('//*[@resource-id="com.cutv.mobile.zsntclient:id/ad_close"]')  # 广告


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        global d
        d = uiautomator2.connect('23482c0b')
        d.implicitly_wait(3)
        launch()  # 启动APP

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)
        # d.app_stop("com.cutv.mobile.zsntclient")
        # d.app_clear("com.cutv.mobile.zsntclient")

    def test_01(self):
        '''搜索'''
        d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/tab_child_layout"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
        d.send_keys('会议')
        d.press('enter')
        sleep(3)
        exist = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/empty_layout"]/android.widget.LinearLayout[1]').exists

        self.assertEqual(exist, False, '搜索结果为空')

    def test_02(self):
        '''搜索分类、筛选切换'''
        click_with_sleep('//*[@text="文稿"]', 2)
        click_with_sleep('//*[@text="图集"]', 2)
        click_with_sleep('//*[@text="视频"]', 2)
        click_with_sleep('//*[@text="全部"]', 2)

        d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/search_result_filter_tv"]').click()  # 筛选
        click_with_sleep('//*[@text="一天"]', 2)
        click_with_sleep('//*[@text="一月"]', 2)
        d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/search_cancle"]').click()  # 取消

    def test_03(self):
        '''天气'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/weather_icon"]', 3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/weather_add_city"]').exists
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/weather_back"]')

        self.assertEqual(flag1, True, '未进入天气页面')

    def test_04(self):
        '''导航栏切换'''
        click_with_sleep('//*[@text="时政"]', 3)
        click_with_sleep('//*[@text="政企"]', 3)  # 进入新页面
        d.click(0.062, 0.097)
        click_with_sleep('//*[@text="人大"]', 3)
        click_with_sleep('//*[@text="时评"]', 3)
        click_with_sleep('//*[@text="理论"]', 3)
        click_with_sleep('//*[@text="辟谣"]', 3)
        click_with_sleep('//*[@text="汽车"]', 3)
        click_with_sleep('//*[@text="热点"]', 3)
        click_with_sleep('//*[@text="民生"]', 3)
        click_with_sleep('//*[@text="报料"]', 3)  # 进入新页面
        d.click(0.062, 0.097)
        click_with_sleep('//*[@text="政协"]', 3)
        click_with_sleep('//*[@text="专题"]', 3)
        click_with_sleep('//*[@text="法润"]', 3)
        click_with_sleep('//*[@text="楼市"]', 3)
        click_with_sleep('//*[@text="图漫"]', 3)
        click_with_sleep('//*[@text="推荐"]', 3)

    def test_05(self):
        '''推荐-新闻文字'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/content_recyclerview"]/android.widget.LinearLayout[1]', 2)  # 新闻文字
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()

    def test_06(self):
        '''推荐-轮播图'''
        d.swipe(0.874, 0.45, 0.044, 0.45)
        sleep(2)
        d.swipe(0.874, 0.45, 0.044, 0.45)
        d.click(0.609, 0.464)
        sleep(3)
        d.click(0.06, 0.071)  # 返回
        sleep(2)

    def test_07(self):
        '''直播'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/marquee_title"]', 3)
        if d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/guid_sort_icon"]').exists:  # 引导提示
            d.click(0.5, 0.5)
            sleep(1)
        d.click(0.057, 0.069)  # 返回
        sleep(1)

    def test_08(self):
        '''听广播'''
        click_with_sleep('//android.widget.GridView/android.widget.LinearLayout[1]', 3)
        flag1 = d.xpath('//*[@content-desc="广播频道"]/android.widget.ImageView[1]').exists
        d.click(0.219, 0.138)  # 广播频道
        sleep(3)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/list_view"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]')
        flag2 = d.xpath('//*[@text="正在播放"]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
        d.click(0.157, 0.386)  # 精品栏目
        sleep(3)
        flag3 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/root_view"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').exists
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/root_view"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
        d.click(0.089, 0.059)

        self.assertEqual(flag1, True, '广播进入失败')
        self.assertEqual(flag2, True, '节目单切换失败')
        self.assertEqual(flag3, True, '栏目进入失败')

    def test_09(self):
        '''看电视'''
        click_with_sleep('//android.widget.GridView/android.widget.LinearLayout[2]', 5)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/rl_video_container"]')
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/play_start"]')  # 暂停按钮
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_header_recycler"]/android.widget.RelativeLayout[2]', 3)  # 切换栏目

        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_program_menu_layout"]')  # 展开节目单
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/program_view_menu_layout"]')  # 关闭节目单
        # 下方栏目
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_home_recycler"]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]', 3)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/ll_vod_detail"]/android.widget.RelativeLayout[1]')
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/play_start"]')  # 暂停按钮
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]', 3)  # 返回
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

    def test_10(self):
        '''刷视频'''
        click_with_sleep('//android.widget.GridView/android.widget.LinearLayout[4]', 3)
        flag1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists

        click_with_sleep('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]', 2)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/short_video8_back_iv"]')
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '刷视频进入失败')

    def test_11(self):
        '''逛商城'''
        click_with_sleep('//android.widget.GridView/android.widget.LinearLayout[5]', 3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists

        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
        self.assertEqual(flag1, True, '逛商城进入失败')

    def test_12(self):
        '''主播秀'''
        d.swipe(0.8, 0.7, 0.08, 0.7)
        click_with_sleep('//android.widget.GridView/android.widget.LinearLayout[1]', 5)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/iv_anchorshow1_apply_for_anchor"]', 2)  # 主播申请
        # 进入登录
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/tv_login_by_psw"]')
        d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/login_user_input"]').click()
        d.send_keys('18571137076')
        d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/login_psw_input"]').click()
        d.send_keys('qq2312750867')
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/login_privacy_check"]')
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/login_normal_btn"]', 2)  # 立即登录
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/anchorshow1_actionbar_ucenter"]', 3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/usercenter_header_follow_count"]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/anchorshow1_actionbar_back"]')

        self.assertEqual(flag1, True, '个人中心进入失败')

    # 客户端卡顿 需重新打开客户端
    def test_13(self):
        '''热点专题跳转'''
        d.app_stop('com.cutv.mobile.zsntclient')
        sleep(2)
        launch()

        d.swipe(0.5, 0.9, 0.5, 0.1, 0.5)
        d.swipe(0.5, 0.9, 0.5, 0.4, 0.5)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/action_more"]', 3)  # 更多
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/viewpager"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        d.click(0.5, 0.7)  # 专题详情页
        sleep(3)
        flag2 = d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').exists
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '第二条热点直播内容不存在')
        self.assertEqual(flag2, True, '专题跳转失败')

    def test_14(self):
        '''报料跳转'''
        d.swipe(0.5, 0.9, 0.5, 0.4, 0.5)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/action_more"]', 3)  # 更多
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/contribute11_content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/contribute11_content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/item_flip_marquee"]', 3)  # 报料详情
        flag2 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/failure_retry_text"]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '报料页面跳转失败')
        self.assertNotEqual(flag2, True, '报料详情页异常')

    def test_15(self):
        '''刷视频跳转'''
        d.swipe(0.5, 0.9, 0.5, 0.1, 0.5)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/mix_list20_recycler_list"]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[3]/android.widget.TextView[2]', 3)  # 更多
        flag1 = d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').exists
        click_with_sleep('//*[@text="影像南通"]')
        click_with_sleep('//*[@text="拍客"]')
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        d.click(0.636, 0.598)  # 视频详情页
        sleep(3)
        flag2 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_player_ad_back"]').exists
        if flag2:
            click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_player_ad_back"]')
        # 两个返回都有可能
        flag3 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_back"]').exists
        if flag3:
            click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/video_back"]')

        self.assertEqual(flag1, True, '视频列表页跳转失败')
        self.assertIn(True, [flag2, flag3], '视频详情页跳转失败')

    def test_16(self):
        '''精彩活动跳转'''
        d.swipe(0.5, 0.9, 0.5, 0.4, 0.5)
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/action_more"]', 3)  # 更多
        flag1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/content_recyclerview"]/android.view.ViewGroup[1]', 3)
        flag2 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '活动列表页跳转失败')
        self.assertEqual(flag2, True, '活动详情页跳转失败')

    def test_17(self):
        '''本地模块跳转'''
        d.click(0.301, 0.974)
        sleep(2)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/tab_child_layout"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').exists

        self.assertEqual(flag1, True, '本地模块跳转失败')

    def test_18(self):
        '''稿件详情页跳转'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/viewpager"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]', 3)
        flag1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '稿件详情页跳转失败')

    def test_19(self):
        '''曝光台模块跳转'''
        d.click(0.5, 0.967)
        sleep(2)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/tab_child_layout"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').exists

        self.assertEqual(flag1, True, '曝光台模块跳转失败')

    def test_20(self):
        '''稿件详情页跳转'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/viewpager"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]', 3)
        flag1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '稿件详情页跳转失败')

    def test_21(self):
        '''栏目切换验证'''
        d.click(0.895, 0.124)
        sleep(2)

    def test_22(self):
        '''服务模块跳转'''
        d.click(0.7, 0.967)
        sleep(2)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/apps18_header_weather_view"]').exists

        self.assertEqual(flag1, True, '服务模块跳转失败')

    def test_23(self):
        '''直播跳转'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/apps18_header_left_name"]', 3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/failure_imageView"]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, False, '看直播页面加载失败')

    def test_24(self):
        '''报料跳转'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/apps18_header_right_name"]', 3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/contribute11_send_img"]').exists
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/contribute_mine_tv"]', 2)  # 我的
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')  # 返回

        self.assertEqual(flag1, True, '报料加载失败')

    def test_25(self):
        '''南通商城跳转'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/recycler_all"]/android.widget.LinearLayout[2]/android.widget.GridView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]', 3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '南通商城跳转失败')

    def test_26(self):
        '''积分商城跳转'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/recycler_all"]/android.widget.LinearLayout[2]/android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[1]', 3)
        flag1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists

        self.assertEqual(flag1, True, '积分商城跳转失败')

    def test_27(self):
        '''积分商城内部功能验证'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/goldmall_header_mymalltv01"]', 2)  # 我的商城
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/list_view"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]').exists  # 存在记录
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/goldmall_header_mymalltv02"]', 2)  # 我的积分
        flag2 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/list_view"]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').exists  # 存在记录
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]', 3)
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        self.assertEqual(flag1, True, '商城兑换记录为空')
        self.assertEqual(flag2, True, '积分变化记录为空')

    def test_28(self):
        '''我的模块跳转'''
        d.click(0.9, 0.97)
        sleep(3)
        flag1 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/tab_child_layout"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]').exists

        self.assertEqual(flag1, True, '我的模块跳转失败')

    def test_29(self):
        '''我的页面积分相关按钮验证'''
        click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/tab_child_layout"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[5]')
        flag1 = d.xpath('//*[@text="设置"]').exists
        click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

        click_with_sleep('//*[@content-desc="主页"]', 7)
        flag2 = d.xpath('//android.widget.ScrollView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]').exists
        click_with_sleep('//android.widget.ScrollView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]')

        flag3 = False
        if d.xpath('//*[@content-desc="签到"]').exists:
            click_with_sleep('//*[@content-desc="签到"]', 8)
            flag3 = d.xpath('//*[@content-desc="签到"]').exists

        d.click(0.324, 0.166)  # 积分记录
        sleep(3)
        flag4 = d.xpath('//android.widget.ScrollView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]').exists
        click_with_sleep('//android.widget.ScrollView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]')

        d.click(0.531, 0.165)  # 任务中心
        sleep(3)
        flag5 = d.xpath('//android.widget.ScrollView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]').exists
        click_with_sleep('//*[@content-desc="补签"]')
        d.click(0.5, 0.595)
        sleep(3)
        click_with_sleep('//android.widget.ScrollView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]')

        self.assertEqual(flag1, True, '设置页面跳转失败')
        self.assertEqual(flag2, True, '主页跳转失败')
        self.assertEqual(flag3, False, '签到失败')
        self.assertEqual(flag4, True, '积分记录页面失败')
        self.assertEqual(flag5, True, '任务中心页面失败')

    def test_30(self):
        '''我的页面按钮验证'''
        if exist('//*[@content-desc="媒体号订阅"]'):
            click_with_sleep('//*[@content-desc="媒体号订阅"]', 5)
            flag1 = d.xpath('//*[@text="热门"]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag1, True, '媒体号订阅页面跳转失败')

        if exist('//*[@content-desc="我的订阅"]'):
            click_with_sleep('//*[@content-desc="我的订阅"]', 3)
            flag2 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag2, True, '我的订阅页面跳转失败')

        if exist('//*[@content-desc="我的收藏"]'):
            click_with_sleep('//*[@content-desc="我的收藏"]', 3)
            flag3 = d.xpath('//*[@text="我的收藏"]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag3, True, '我的收藏页面跳转失败')

        if exist('//*[@content-desc="历史记录"]'):
            click_with_sleep('//*[@content-desc="历史记录"]', 3)
            flag4 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/list_view"]/android.widget.FrameLayout[1]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag4, True, '历史记录页面跳转失败')

        if exist('//*[@content-desc="我的评论"]'):
            click_with_sleep('//*[@content-desc="我的评论"]', 3)
            flag5 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag5, True, '我的评论页面跳转失败')

        if exist('//*[@content-desc="积分商城"]'):
            click_with_sleep('//*[@content-desc="积分商城"]', 5)
            flag6 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/goldmall_header_mymall"]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag6, True, '积分商城页面跳转失败')

        if exist('//*[@content-desc="邀请码"]'):
            click_with_sleep('//*[@content-desc="邀请码"]', 3)
            flag7 = d.xpath('//*[@text="邀请码"]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag7, True, '邀请码页面跳转失败')

        if exist('//*[@content-desc="邀请好友"]'):
            click_with_sleep('//*[@content-desc="邀请好友"]', 3)
            flag8 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
            similarity = d.image.match('1.jpg')['similarity']

            click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag8, True, '邀请好友页面跳转失败')
            self.assertGreater(similarity, 0.8, '邀请好友页面异常')

        if exist('//*[@content-desc="掌上南通商城"]'):
            click_with_sleep('//*[@content-desc="掌上南通商城"]', 3)
            flag9 = d.xpath('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').exists
            click_with_sleep('//*[@resource-id="com.cutv.mobile.zsntclient:id/web_container"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag9, True, '掌上南通商城页面跳转失败')

        if exist('//*[@content-desc="社区"]'):
            click_with_sleep('//*[@content-desc="社区"]', 3)
            flag10 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]').exists
            click_with_sleep('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
            self.assertEqual(flag10, True, '社区页面跳转失败')
