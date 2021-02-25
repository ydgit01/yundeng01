from Base.base import base
import time
import Page
from Data.mysql_data import Mysql_data
class Personnel:
    def __init__(self,driver):
        self.bas = base(driver)
        self.driver = driver
    def create_per(self,cte_data):
        time.sleep(2)
        self.bas.click_element(Page.create_per_el,timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.send_text(Page.per_send_el[0],cte_data["人员姓名"],timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.per_send_el[1], cte_data["登录账号"],timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.per_click_el[0],timeout=10,poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.per_click_el[1],timeout=10,poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.per_click_el[2],timeout=10,poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.per_click_el[3],timeout=10,poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.per_click_el[4],timeout=10,poll_frequency=1.0)
        time.sleep(1)
        target = self.bas.search_element(Page.per_click_el[5],timeout=10,poll_frequency=1.0)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        time.sleep(1)
        self.bas.click_element(Page.per_click_el[6],timeout=10,poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.per_click_el[7],timeout=10,poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.per_send_el[2],cte_data["邮箱地址"],timeout=10,poll_frequency=1.0)
        self.bas.send_text(Page.per_send_el[3],cte_data["手机号码"],timeout=10,poll_frequency=1.0)
        self.bas.click_element(Page.per_define_el,timeout=10,poll_frequency=1.0)

    def update_per(self,upt_data):
        time.sleep(1)
        opers = self.bas.search_elements(Page.per_opers_el,timeout=10, poll_frequency=1.0)
        self.driver.execute_script("arguments[0].click();",opers[3])
        time.sleep(1)
        self.bas.send_text(Page.per_send_el[0], upt_data["人员姓名"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.per_define1_el,timeout=10,poll_frequency=1.0)

    def stop_per(self):
        time.sleep(2)
        opers = self.bas.search_elements(Page.per_opers_el, timeout=10, poll_frequency=1.0)
        self.driver.execute_script("arguments[0].click();", opers[4])
        time.sleep(2)
        self.bas.click_element(Page.stop_define_el, timeout=10, poll_frequency=1.0)
        stop_text = Mysql_data().emp_name(42,0)
        return stop_text

    def start_per(self):
        time.sleep(2)
        self.bas.click_element(Page.start_per_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.start_per_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.start_per_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        opers = self.bas.search_elements(Page.per_opers_el, timeout=10, poll_frequency=1.0)
        self.driver.execute_script("arguments[0].click();",opers[4])
        time.sleep(2)
        self.bas.click_element(Page.start_define_el, timeout=10, poll_frequency=1.0)
        start_text = Mysql_data().emp_name(42,1)
        time.sleep(2)
        self.bas.click_element(Page.search_per_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.search_per_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.search_per_el[3], timeout=10, poll_frequency=1.0)
        return start_text

    def search_per(self,search_data):
        time.sleep(2)
        self.bas.click_element(Page.search_per_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.search_per_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.send_text(Page.search_per_el[2], search_data["登录账号"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.search_per_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        search_text = self.bas.text(Page.search_per_el[4], timeout=10, poll_frequency=1.0)
        return search_text

    def results_per(self):
        self.bas.click_element(Page.results_per_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.results_per_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        results_text = self.bas.text(Page.results_per_el[2], timeout=10, poll_frequency=1.0)
        return results_text

    def deblocking_per(self):#登录解锁
        time.sleep(1)
        opers = self.bas.search_elements(Page.per_opers_el, timeout=10, poll_frequency=1.0)
        self.driver.execute_script("arguments[0].click();", opers[5])
        time.sleep(2)
        self.bas.click_element(Page.resetpassword_define_el[0], timeout=10, poll_frequency=1.0)
        deblocking_text = self.bas.text(Page.resetpassword_define_el[1], timeout=10, poll_frequency=1.0)
        return deblocking_text

    def details_per(self):
        time.sleep(1)
        self.bas.click_element(Page.details_per_el[0], timeout=10, poll_frequency=1.0)
        details_text = self.bas.text(Page.details_per_el[1], timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.details_per_el[2], timeout=10, poll_frequency=1.0)
        return details_text

    def details_edit(self):#详情页编辑信息
        time.sleep(1)
        self.bas.click_element(Page.details_edit_el[3], timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.details_edit_el[0], timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.details_edit_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        edit_text = self.bas.text(Page.details_edit_el[2], timeout=10, poll_frequency=1.0)
        return edit_text

    def details_status(self):#详情页点击停用
        time.sleep(1)
        self.bas.click_element(Page.details_status_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_status_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        edit_text = self.bas.text(Page.details_status_el[0], timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.details_status_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_status_el[1], timeout=10, poll_frequency=1.0)
        return edit_text

    def details_resetpassword(self):#需要点击返回箭头
        time.sleep(1)
        self.bas.click_element(Page.details_resetpassword_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_resetpassword_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_resetpassword_el[1], timeout=10, poll_frequency=1.0)
        resetpassword_text = self.bas.text(Page.details_resetpassword_el[2], timeout=10, poll_frequency=1.0)
        return resetpassword_text

    def initial_password(self,data):
        time.sleep(1)
        self.bas.send_text(Page.initial_password_el[0],data["新密码"] ,timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.initial_password_el[1], data["确认密码"], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.details_resetpassword_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        password_text = self.bas.text(Page.details_resetpassword_el[3], timeout=10, poll_frequency=1.0)
        return password_text

    def btch_org(self): #批量修改组织
        time.sleep(1)
        self.bas.click_element(Page.btch_org_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        # self.bas.click_element(Page.details_resetpassword_el[1], timeout=10, poll_frequency=1.0)
        # resetpassword_text = self.bas.text(Page.details_status_el[2], timeout=10, poll_frequency=1.0)
        # time.sleep(1)
        # self.bas.click_element(Page.details_resetpassword_el[3], timeout=10, poll_frequency=1.0)
        # return resetpassword_text

    def btch_stop(self):#批量启用
        pass

    def btch_start(self):#批量停用
        pass


































