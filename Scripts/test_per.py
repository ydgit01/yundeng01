import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Base import driver
from Data.execl_data import Execl_data
import Page
from Base.base import base
from Base.creenShot import sav_creenshot
from Page.personnel_page import Personnel
from Page.top_page import top
from Page.login_page import login
from Page.management_page import management
import time
@allure.feature('人员管理')
class Test_per:
    def setup_class(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
        login(self.driver).log(Execl_data("登录").case_test_data(1, 3))
        top(self.driver).click_management()
        management(self.driver).click_tab(1)

    def teardown_class(self):
        time.sleep(2)
        self.driver.close()

    @pytest.mark.skip(reason="暂时不执行")
    @pytest.mark.run(order=51)
    @allure.title(Execl_data('人员管理').case_data(1, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_cte01(self):
        Personnel(self.driver).create_per(Execl_data("人员管理").case_test_data(1,3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_per = base(self.driver).text(Page.per_obtain_el[0],timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('人员管理').case_data(1, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(1, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(1, 4)), '预期结果')
        assert "人员01" in text_per

    @pytest.mark.skip(reason="暂时不执行")
    @pytest.mark.run(order=52)
    @allure.title(Execl_data('人员管理').case_data(2, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_cte02(self):
        Personnel(self.driver).create_per(Execl_data("人员管理").case_test_data(2, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_per = base(self.driver).text(Page.per_obtain_el[1], timeout=10, poll_frequency=1.0)
        base(self.driver).click_element(Page.per_fallback_el, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('人员管理').case_data(2, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(2, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(2, 4)), '预期结果')
        assert "请填写" in text_per

    @pytest.mark.skip(reason="暂时不执行")
    @pytest.mark.run(order=53)
    @allure.title(Execl_data('人员管理').case_data(3, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_cte03(self):
        Personnel(self.driver).create_per(Execl_data("人员管理").case_test_data(3, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_per = base(self.driver).text(Page.per_obtain_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        base(self.driver).click_element(Page.per_fallback_el, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('人员管理').case_data(3, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(3, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(3, 4)), '预期结果')
        assert "已被注册" in text_per

    @pytest.mark.skip(reason="暂时不执行")
    @pytest.mark.run(order=54)
    @allure.title(Execl_data('人员管理').case_data(4, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_upt(self):
        Personnel(self.driver).update_per(Execl_data("人员管理").case_test_data(4, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_per = base(self.driver).text(Page.per_update_el, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('人员管理').case_data(4, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(4, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(4, 4)), '预期结果')
        assert "test修改功能" in text_per

    @pytest.mark.run(order=57)
    @allure.title(Execl_data('人员管理').case_data(7, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_stop(self):
        stop_text = Personnel(self.driver).stop_per()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(7, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(7, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(7, 4)), '预期结果')
        assert 'test修改功能'== stop_text[0][0]

    @pytest.mark.run(order=58)
    @allure.title(Execl_data('人员管理').case_data(8, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_start(self):
        start_text = Personnel(self.driver).start_per()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(8, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(8, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(8, 4)), '预期结果')
        assert 'test修改功能' == start_text[2][0]

    @pytest.mark.run(order=56)
    @allure.title(Execl_data('人员管理').case_data(6, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_search(self):
        search_text = Personnel(self.driver).search_per(Execl_data("人员管理").case_test_data(6, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        self.driver.find_element_by_css_selector("[role='button'] [focusable='false']").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.btnsWrapper___M2BE1 button.ant-btn-primary').click()
        time.sleep(1)
        allure.attach("{0}".format(Execl_data('人员管理').case_data(6, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(6, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(6, 4)), '预期结果')
        assert 'yuedantestadmin' == search_text

    @pytest.mark.run(order=55)
    @allure.title(Execl_data('人员管理').case_data(5, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_results(self):
        results_text = Personnel(self.driver).results_per()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(5, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(5, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(5, 4)), '预期结果')
        assert '人员管理' == results_text


    @pytest.mark.run(order=61)
    @allure.title(Execl_data('人员管理').case_data(11, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    #进入人员详情页面
    def test_per_details(self):
        details_text = Personnel(self.driver).details_per()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(11, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(11, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(11, 4)), '预期结果')
        assert '基础信息' == details_text

    @pytest.mark.run(order=62)
    @allure.title(Execl_data('人员管理').case_data(12, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    #人员详情页面编辑用户信息
    def test_per_edit(self):
        edit_text = Personnel(self.driver).details_edit()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(12, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(12, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(12, 4)), '预期结果')
        assert '基础信息' == edit_text

    @pytest.mark.run(order=63)
    @allure.title(Execl_data('人员管理').case_data(13, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_per_status(self):
        status_text = Personnel(self.driver).details_status()
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(13, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(13, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('人员管理').case_data(13, 4)), '预期结果')
        assert '启用' == status_text



    @pytest.mark.run(order=60)
    @allure.title(Execl_data('人员管理').case_data(10, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_btch_org(self):
        # drivr = self.driver
        # log_text = Personnel(drivr).btch_org()
        # time.sleep(1)
        # file = sav_creenshot(drivr)
        # allure.attach(file, '截屏')
        # allure.attach("{0}".format(log_text), '获取的断言数据')
        # a = Mysql_data().emp_loginlog_num(42,"第一个人员")
        # assert str(a) in log_text
        pass






