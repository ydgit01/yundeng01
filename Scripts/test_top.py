import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Base import driver
from Data.execl_data import Execl_data
from Page.login_page import login
import Page
from Base.base import base
from Base.creenShot import sav_creenshot
from Page.top_page import top
import time
@allure.feature('吊顶模块')
class Test_top:
    def setup(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
        login(self.driver).log(Execl_data("登录").case_test_data(1, 3))
    def teardown(self):
        time.sleep(1)
        self.driver.close()

    @pytest.mark.run(order=11)
    @allure.title(Execl_data("吊顶").case_data(1,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_logout(self):
        text_logout = top(self.driver).logout_system()
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(1, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(1, 4)), '预期结果')
        assert '登 录' in text_logout

    @pytest.mark.run(order=12)
    @allure.title(Execl_data("吊顶").case_data(2,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_per(self):
        text_per = top(self.driver).personal_setting()
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(2, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(3, 4)), '预期结果')
        assert '成功' in text_per

    @pytest.mark.run(order=13)
    @allure.title(Execl_data("吊顶").case_data(3, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_head_sculpture(self):
        pass

    @pytest.mark.run(order=15)
    @allure.title(Execl_data("吊顶").case_data(5, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_authority(self):
        text_aut = top(self.driver).my_authority()
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(5, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(5, 4)), '预期结果')
        assert '我的数据权限' in text_aut

    @pytest.mark.run(order=16)
    @allure.title(Execl_data("吊顶").case_data(6, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_help(self):
        text_help = top(self.driver).help()
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(6, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(6, 4)), '预期结果')
        assert '插件' in text_help

    @pytest.mark.run(order=17)
    @allure.title(Execl_data("吊顶").case_data(7,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_news(self):
        text_news = top(self.driver).view_news()
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(7, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(7, 4)), '预期结果')
        assert '消息列表' in text_news

    @pytest.mark.run(order=18)
    @allure.title(Execl_data("吊顶").case_data(8, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_top_mgt(self):
        top(self.driver).click_management()
        time.sleep(2)
        text_mgt = base(self.driver).text(Page.management_obtain, timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(8, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('吊顶').case_data(8, 4)), '预期结果')
        assert '乐丹' in text_mgt