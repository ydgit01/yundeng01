import sys,os,pytest,allure
sys.path.append(os.getcwd())

from Page.login_page import login
from Base import driver
from Data.execl_data import Execl_data
import Page
from Base.base import base
from Base.creenShot import sav_creenshot
import time
@allure.feature('场景用例')
#登录页面功能点测试用例

class Test_addfun_login:
    def setup(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()

    def teardown(self):
        time.sleep(1)
        self.driver.close()


    @allure.title(Execl_data('权限管理').case_data(7, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', name='云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    @pytest.mark.run(order=1)
    def test_checking(self):
        login(self.driver).log(Execl_data("权限管理").case_test_data(7, 3))
        time.sleep(2)
        base(self.driver).click_element(Page.checking_el[1], timeout=10, poll_frequency=1.0)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        checking_pri = base(self.driver).search_elements(Page.checking_el[0], timeout=10, poll_frequency=1.0)
        for i in range(2):
            assert checking_pri[i].text in ["工作台","项目","研效","服务总览"]
        allure.attach("{0}".format(Execl_data('权限管理').case_data(7, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(7, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(7, 4)), '预期结果')