import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Data.execl_data import Execl_data
from Base import driver
import Page
from Base.base import base
from Base.creenShot import sav_creenshot
from Page.organization_page import company
from Page.top_page import top
from Page.login_page import login
from Page.management_page import management
import time
@allure.feature('组织与单位/单位管理模块')
class Test_com:
    def setup_class(self):
        self.driver = driver.get_driver()
        self.driver.maximize_window()
        login(self.driver).log(Execl_data("登录").case_test_data(1, 3))
        top(self.driver).click_management()
        management(self.driver).click_tab(0)
    def teardown_class(self):
        time.sleep(1)
        self.driver.close()


    @pytest.mark.run(order=41)
    @pytest.mark.repeat(3)
    @pytest.mark.skip(reason="暂时不执行")
    @allure.title(Execl_data('组织与单位').case_data(10,1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_cte01(self):
        company(self.driver).create_com(Execl_data("组织与单位").case_test_data(10,3))
        time.sleep(1)    #等待2秒
        file = sav_creenshot(self.driver)
        allure.attach(file,'截屏')
        text_com = base(self.driver).text(Page.obtain_com[0],timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(10, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(10, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(10, 4)), '预期结果')
        assert "单位01" in text_com

    @pytest.mark.run(order=42)
    @allure.title(Execl_data('组织与单位').case_data(11, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_cte02(self):
        company(self.driver).create_com(Execl_data("组织与单位").case_test_data(11, 3))
        time.sleep(1)  # 等待2秒
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_com = base(self.driver).text(Page.obtain_com[1], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(11, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(11, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(11, 4)), '预期结果')
        self.driver.refresh()
        assert "已存在" in text_com

    @pytest.mark.run(order=43)
    @allure.title(Execl_data('组织与单位').case_data(12, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_cte03(self):
        company(self.driver).create_com(Execl_data("组织与单位").case_test_data(12, 3))
        time.sleep(1)  # 等待2秒
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_com = base(self.driver).text(Page.obtain_com[2], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(12, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(12, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(12, 4)), '预期结果')
        self.driver.refresh()
        assert "请输入单位名称" in text_com

    @pytest.mark.run(order=44)
    @allure.title(Execl_data('组织与单位').case_data(13, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_upt(self):
        company(self.driver).update_com(Execl_data("组织与单位").case_test_data(13, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截图')
        text_com02 = base(self.driver).text(Page.obtain_com02, timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(13, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(13, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(13, 4)), '预期结果')
        assert text_com02 == '阿里巴巴'

    @pytest.mark.run(order=45)
    @allure.title(Execl_data('组织与单位').case_data(14, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_del(self):
        company(self.driver).delete_com(1)
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_com03 = base(self.driver).text(Page.obtain_com03[0], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(14, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(14, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(14, 4)), '预期结果')
        assert '删除' in text_com03

    @pytest.mark.run(order=46)
    @allure.title(Execl_data('组织与单位').case_data(15, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_del01(self):
        company(self.driver).delete_com(0)
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        text_com03 = base(self.driver).text(Page.obtain_com03[1], timeout=10, poll_frequency=1.0)
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(15, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(15, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(15, 4)), '预期结果')
        self.driver.refresh()
        assert '单位下存在人员' in text_com03

    @pytest.mark.run(order=47)
    @allure.title(Execl_data('组织与单位').case_data(16, 1))
    @allure.issue('http://yunxiao.cloudpm.aliyun.com/my', '云效地址')
    @allure.testcase('https://dayu.work/alita/functional?businessId=294954&projectId=537', '用例地址')
    def test_com_sea(self):
        text_sea = company(self.driver).search_com(Execl_data("组织与单位").case_test_data(16, 3))
        time.sleep(1)
        file = sav_creenshot(self.driver)
        allure.attach(file, '截屏')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(16, 2)), '测试步骤')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(16, 3)), '测试数据')
        allure.attach("{0}".format(Execl_data('组织与单位').case_data(16, 4)), '预期结果')
        assert '单位02' in text_sea

