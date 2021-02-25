import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Page.login_page import login
from Base import driver
from Data.execl_data import Execl_data
from Page.top_page import top
from Base.base import base
from Base.creenShot import sav_creenshot
import Page
from Page.personnel_page import Personnel
from Page.management_page import management
import time
#人员管理页面验证登录解锁功能
class Test_resetpassword:
    def setup(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
    def teardown(self):
        time.sleep(1)
        self.driver.close()

    @pytest.mark.skip(reason="暂时不执行")
    @pytest.mark.run(order=71)
    @allure.title(Execl_data('人员管理').case_data(9, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_password01(self):
        login(self.driver).log(Execl_data("人员管理").case_test_data(9, 3))
        time.sleep(1)
        login(self.driver).log(Execl_data("人员管理").case_test_data(9, 3))
        time.sleep(1)
        login(self.driver).log(Execl_data("人员管理").case_test_data(9, 3))
        time.sleep(1)
        login(self.driver).log(Execl_data("登录").case_test_data(1, 3))
        top(self.driver).click_management()
        management(self.driver).click_tab(1)
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        deblocking_text = Personnel(self.driver).deblocking_per()
        allure.attach("{0}".format(Execl_data('人员管理').case_data(9, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(9, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(9, 4)), '预期结果')
        assert '解锁成功' in deblocking_text

    @pytest.mark.skip(reason="暂时不执行")
    @pytest.mark.run(order=72)
    @allure.title(Execl_data('人员管理').case_data(9, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_password02(self):
        time.sleep(2)
        login(self.driver).log_checking(Execl_data("人员管理").case_test_data(9, 3))
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        text_checking = base(self.driver).text(Page.text_checking, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('人员管理').case_data(9, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(9, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(9, 4)), '预期结果')
        assert "test修改功能" in text_checking