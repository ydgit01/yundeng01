import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Data.execl_data import Execl_data
from Base import driver
import Page
from Base.base import base
from Base.creenShot import sav_creenshot
from Page.priviledge_page import Priviledge
from Page.top_page import top
from Page.login_page import login
from Page.management_page import management
import time
@allure.feature('权限管理模块')
class Test_pri:
    def setup_class(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
        login(self.driver).log(Execl_data("登录").case_test_data(1, 3))
        top(self.driver).click_management()
        management(self.driver).click_tab(2)

    def teardown_class(self):
        time.sleep(1)
        self.driver.close()

    @pytest.mark.run(order=91)
    @allure.title(Execl_data('权限管理').case_data(1, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_pri_cte01(self):
        Priviledge(self.driver).create_role(Execl_data("权限管理").case_test_data(1, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_pri = base(self.driver).text(Page.obtain_pri_el[0], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('权限管理').case_data(1, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(1, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(1, 4)), '预期结果')
        assert "功能角色01" in text_pri

    @pytest.mark.run(order=92)
    @allure.title(Execl_data('权限管理').case_data(2, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_pri_cte02(self):
        Priviledge(self.driver).create_role(Execl_data("权限管理").case_test_data(2, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_pri = base(self.driver).text(Page.obtain_pri_el[1], timeout=10, poll_frequency=1.0)
        self.driver.refresh()
        allure.attach("{0}".format(Execl_data('权限管理').case_data(2, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(2, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(2, 4)), '预期结果')
        assert "已存在" in text_pri

    @pytest.mark.run(order=93)
    @allure.title(Execl_data('权限管理').case_data(3, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_pri_cte03(self):
        Priviledge(self.driver).create_role(Execl_data("权限管理").case_test_data(3, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_pri = base(self.driver).text(Page.obtain_pri_el[2], timeout=10, poll_frequency=1.0)
        self.driver.refresh()
        allure.attach("{0}".format(Execl_data('权限管理').case_data(3, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(3, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(3, 4)), '预期结果')
        assert "请输入" in text_pri

    @pytest.mark.run(order=94)
    @allure.title(Execl_data('权限管理').case_data(4, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_pri_cte04(self):
        Priviledge(self.driver).create_role(Execl_data("权限管理").case_test_data(4, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_pri = base(self.driver).text(Page.obtain_pri_el[3], timeout=10, poll_frequency=1.0)
        self.driver.refresh()
        allure.attach("{0}".format(Execl_data('权限管理').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(4, 4)), '预期结果')
        assert "2到30位字符" in text_pri

    @pytest.mark.run(order=95)
    @allure.title(Execl_data('权限管理').case_data(5, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_pri_upt(self):
        textup_pri = Priviledge(self.driver).update_role(Execl_data("权限管理").case_test_data(5, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(5, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(5, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(5, 4)), '预期结果')
        assert "功能角色02" in textup_pri

    @pytest.mark.run(order=96)
    @allure.title(Execl_data('权限管理').case_data(6, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_add_people(self):
        text_num = Priviledge(self.driver).add_people()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(6, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(6, 4)), '预期结果')
        assert "3" in text_num

    @pytest.mark.run(order=97)
    @allure.title(Execl_data('权限管理').case_data(8, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_role_details(self):
        text_pri = Priviledge(self.driver).role_details()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        base(self.driver).click_element(Page.role_details_el[2], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('权限管理').case_data(8, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(8, 4)), '预期结果')
        assert "服务总览" in text_pri

    @pytest.mark.run(order=98)
    @allure.title(Execl_data('权限管理').case_data(18, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_details_search(self):
        text_sea = Priviledge(self.driver).details_search(Execl_data('权限管理').case_test_data(18, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        time.sleep(1)
        base(self.driver).click_element(Page.details_search_el[4], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('权限管理').case_data(18, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(18, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(18, 4)), '预期结果')
        assert "人员03" in text_sea

    @pytest.mark.run(order=99)
    @allure.title(Execl_data('权限管理').case_data(15, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_details_delete(self):
        message_delete = Priviledge(self.driver).details_delete()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        time.sleep(1)
        base(self.driver).click_element(Page.details_search_el[5], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('权限管理').case_data(15, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(15, 4)), '预期结果')
        assert "移除人员成功" in message_delete

    @pytest.mark.run(order=100)
    @allure.title(Execl_data('权限管理').case_data(9, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_remove_people(self):
        message_remove = Priviledge(self.driver).remove_people(Execl_data('权限管理').case_test_data(9, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(9, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(9, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(9, 4)), '预期结果')
        assert "删除角色成员成功" in message_remove

    @pytest.mark.run(order=101)
    @allure.title(Execl_data('权限管理').case_data(14, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_search_role(self):
        text_sea = Priviledge(self.driver).search_role(Execl_data('权限管理').case_test_data(14, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        base(self.driver).click_element(Page.search_role_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        base(self.driver).click_element(Page.search_role_el[1], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('权限管理').case_data(14, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(14, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(14, 4)), '预期结果')
        assert "普通用户" in text_sea

    @pytest.mark.run(order=102)
    @allure.title(Execl_data('权限管理').case_data(11, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_delete_role02(self):
        message_delete = Priviledge(self.driver).delete_role02()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(11, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(11, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(11, 4)), '预期结果')
        assert "角色下存在成员" in message_delete

    @pytest.mark.run(order=103)
    @allure.title(Execl_data('权限管理').case_data(12, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_delete_role01(self):
        message_delete = Priviledge(self.driver).delete_role01()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(12, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(12, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(12, 4)), '预期结果')
        assert "删除角色成功" in message_delete

    @pytest.mark.run(order=104)
    @allure.title(Execl_data('权限管理').case_data(13, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectsId=537', '用例地址')
    def test_delete_roles(self):
        message_delete = Priviledge(self.driver).delete_roles()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(13, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(13, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(13, 4)), '预期结果')
        assert "角色下存在成员，无法删除" in message_delete

    @pytest.mark.run(order=105)
    @allure.title(Execl_data('权限管理').case_data(17, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectsId=537', '用例地址')
    def test_remove_admin(self):
        message_remove = Priviledge(self.driver).remove_admin(Execl_data('权限管理').case_test_data(17, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(17, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(17, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('权限管理').case_data(17, 4)), '预期结果')
        assert "默认的租户管理员无法被移除" in message_remove





