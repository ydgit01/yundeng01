import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Data.execl_data import Execl_data
import Page
from Base import driver
from Base.base import base
from Base.creenShot import sav_creenshot
from Page.organization_page import organization
from Page.top_page import top
from Page.login_page import login
from Page.management_page import management
import time
@allure.feature('组织与单位/组织管理模块')
class Test_org:
    def setup_class(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
        login(self.driver).log(Execl_data("登录").case_test_data(1, 3))
        top(self.driver).click_management()
        management(self.driver).click_tab(0)

    def teardown_class(self):
        time.sleep(2)
        self.driver.close()

    @pytest.mark.run(order=31)
    @allure.title(Execl_data('组织与单位').case_data(1,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_cte01(self):
        organization(self.driver).create_org(Execl_data("组织与单位").case_test_data(1,3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_org = base(self.driver).text(Page.obtain_org[0], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(1, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(1, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(1, 4)), '预期结果')
        assert "成功" in text_org

    @pytest.mark.run(order=32)
    @allure.title(Execl_data('组织与单位').case_data(2, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_cte02(self):
        organization(self.driver).create_org(Execl_data("组织与单位").case_test_data(2,3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_org = base(self.driver).text(Page.obtain_org[1], timeout=10, poll_frequency=1.0)
        self.driver.refresh()
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(2, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(2, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(2, 4)), '预期结果')
        assert "已存在" in text_org

    @pytest.mark.run(order=33)
    @allure.title(Execl_data('组织与单位').case_data(3, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_cte03(self):
        organization(self.driver).create_org(Execl_data("组织与单位").case_test_data(3,3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_org = base(self.driver).text(Page.obtain_org[2], timeout=10, poll_frequency=1.0)
        self.driver.refresh()
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(3, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(3, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(3, 4)), '预期结果')
        assert "请填写组织名称" in text_org

    @pytest.mark.run(order=34)
    @allure.title(Execl_data('组织与单位').case_data(4, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_cte04(self):
        organization(self.driver).create_org(Execl_data("组织与单位").case_test_data(4, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_org = base(self.driver).text(Page.obtain_org[3], timeout=10, poll_frequency=1.0)
        self.driver.refresh()
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(4, 4)), '预期结果')
        assert "2到30位" in text_org


    @pytest.mark.run(order=35)
    @allure.title(Execl_data('组织与单位').case_data(5, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_upt(self):
        organization(self.driver).update_org(Execl_data('组织与单位').case_test_data(5, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        text_org02 = base(self.driver).text(Page.obtain_org02, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(5, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(5, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(5, 4)), '预期结果')
        assert text_org02 == '组织0101'

    @pytest.mark.run(order=36)
    @allure.title(Execl_data('组织与单位').case_data(6, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_del(self):
        organization(self.driver).delete_org(0)
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        text_org03 = base(self.driver).text(Page.obtain_org03[0], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(6, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(6, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(6, 4)), '预期结果')
        assert '删除' in text_org03

    @pytest.mark.run(order=37)
    @allure.title(Execl_data('组织与单位').case_data(7, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_del01(self):
        organization(self.driver).delete_org(1)
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        text_org03 = base(self.driver).text(Page.obtain_org03[1], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(7, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(7, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(7, 4)), '预期结果')
        assert '组织存在用户' in text_org03

    @pytest.mark.run(order=38)
    @allure.title(Execl_data('组织与单位').case_data(8, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_num(self):
        text_list = organization(self.driver).number_personnel()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(8, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(8, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(8, 4)), '预期结果')
        assert '成员列表' in text_list

    @pytest.mark.run(order=39)
    @allure.title(Execl_data('组织与单位').case_data(9, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_org_(self):
        pass
        # text_list = organization(self.driver).search_org()
        # time.sleep(1)
        # file = sav_creenshot(self.driver)
        # allure.attach(file, '截图')
        # allure.attach("{0}".format(Execl_data('组织与单位').case_data(9, 2)), '测试步骤')
        # allure.attach("{0}".format(Execl_data('组织与单位').case_data(9, 3)), '测试数据')
        # allure.attach("{0}".format(Execl_data('组织与单位').case_data(9, 4)), '预期结果')
        # assert '成员列表' in text_list