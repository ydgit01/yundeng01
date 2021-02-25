import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Page.login_page import login
from Base import driver
from Data.execl_data import Execl_data
import Page
from Base.base import base
from Base.creenShot import sav_creenshot
import time
@allure.feature('登录模块')
#登录页面功能点测试用例
class Test_login:
    def setup(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
    def teardown(self):
        time.sleep(1)
        self.driver.close()

    @allure.title(Execl_data('登录').case_data(1,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my',name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537','用例地址')
    @pytest.mark.run(order=1)
    def test_login_case01(self):
        login(self.driver).log(Execl_data("登录").case_test_data(1,3))
        time.sleep(2)
        text_login01 = base(self.driver).search_elements(Page.obtain_login[0], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(1,2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(1,3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(1,4)), '预期结果')
        assert '管理' in text_login01[2].text

    @allure.title(Execl_data('登录').case_data(2, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=2)
    def test_login_case02(self):
        login(self.driver).log(Execl_data("登录").case_test_data(2,3))
        time.sleep(2)
        text_login02 = base(self.driver).search_elements(Page.obtain_login[0], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(2, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(2, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(2, 4)), '预期结果')
        assert 2 == len(text_login02)

    @allure.title(Execl_data('登录').case_data(3,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=3)
    def test_login_case03(self):
        login(self.driver).log(Execl_data("登录").case_test_data(3,3))
        time.sleep(2)
        text_login03 = base(self.driver).text(Page.obtain_login[1], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(3,2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(3,3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(3,4)),'预期结果')
        assert '租户错误' in text_login03

    @allure.title(Execl_data('登录').case_data(4, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=4)
    def test_login_case04(self):
        login(self.driver).log(Execl_data("登录").case_test_data(4,3))
        time.sleep(2)
        text_login04 = base(self.driver).text(Page.obtain_login[1], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 4)), '预期结果')
        assert '账号不存在' in text_login04

    @allure.title(Execl_data('登录').case_data(5, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=5)
    def test_login_case05(self):
        login(self.driver).log(Execl_data("登录").case_test_data(5, 3))
        time.sleep(2)
        text_login05 = base(self.driver).text(Page.obtain_login[1], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(5, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(5, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(5, 4)), '预期结果')
        assert '密码错误' in text_login05

    @pytest.mark.skip(reason="暂时不执行")
    @allure.title(Execl_data('登录').case_data(6, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=6)
    def test_login_case06(self):
        login(self.driver).log(Execl_data("登录").case_test_data(6, 3))
        time.sleep(1)
        login(self.driver).log(Execl_data("登录").case_test_data(6, 3))
        time.sleep(1)
        login(self.driver).log(Execl_data("登录").case_test_data(6, 3))
        time.sleep(1)
        login(self.driver).log(Execl_data("登录").case_test_data(6, 3))
        time.sleep(2)
        text_login06 = base(self.driver).text(Page.obtain_login[1], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(6, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(6, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(6, 4)), '预期结果')
        assert '已被冻结' in text_login06





