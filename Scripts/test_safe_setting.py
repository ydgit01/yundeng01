import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Page.login_page import login
from Base import driver
from Data.execl_data import Execl_data
from Page.top_page import top
from Base.base import base
from Base.creenShot import sav_creenshot
import Page
import time
#吊顶处安全设置，修改密码
@allure.feature('场景用例')
class Test_safe_setting:
    def setup_class(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
        login(self.driver).log(Execl_data("吊顶").case_test_data(4, 3))
    def teardown_class(self):
        time.sleep(1)
        self.driver.close()

    @pytest.mark.skip(reason="暂时不执行")
    @allure.title(Execl_data('吊顶').case_data(4,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=21)
    def test_safe01(self):
        time.sleep(2)
        text_safe = top(self.driver).safe_setting(Execl_data("吊顶").case_test_data(4,3))
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 4)), '预期结果')
        assert "登 录" in text_safe

    @pytest.mark.skip(reason="暂时不执行")
    @allure.title(Execl_data('吊顶').case_data(4, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=22)
    def test_safe02(self):
        time.sleep(2)
        login(self.driver).log_checking(Execl_data("吊顶").case_test_data(4,3))
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        text_checking = base(self.driver).text(Page.text_checking, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 4)), '预期结果')
        assert "人员03" in text_checking

    @pytest.mark.skip(reason="暂时不执行")
    @allure.title(Execl_data('吊顶').case_data(4, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=23)
    def test_safe03(self):
        time.sleep(2)
        login(self.driver).log_checking(Execl_data("吊顶").case_test_data(4, 3))
        time.sleep(2)
        text_safe = top(self.driver).safe_setting(Execl_data("吊顶").case_test_data(9, 3))
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('登录').case_data(4, 4)), '预期结果')
        assert "登 录" in text_safe


