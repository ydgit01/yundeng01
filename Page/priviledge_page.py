from Base.base import base
import time
import Page
class Priviledge:
    def __init__(self,driver):
        self.bas = base(driver)
        self.driver = driver

    def create_role(self,cte_data):
        time.sleep(1)
        self.bas.click_element(Page.create_role_el,timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.role_send_el[0],cte_data["角色名称"],timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.role_send_el[1], cte_data["角色标识"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.role_send_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.role_send_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.role_send_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.role_send_el[5], cte_data["角色描述"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.role_send_el[6], timeout=10, poll_frequency=1.0)

    def update_role(self, upt_data):
        time.sleep(1)
        self.bas.click_element(Page.pri_update_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.pri_update_el[1], upt_data["角色名称"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.role_send_el[6], timeout=10, poll_frequency=1.0)
        textup_pri = base(self.driver).text(Page.pri_update_el[2], timeout=10, poll_frequency=1.0)
        return textup_pri

    def search_role(self,sea_data):
        time.sleep(1)
        self.bas.send_text(Page.search_role_el[0], sea_data["角色名称"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.search_role_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        text_sea = self.bas.text(Page.search_role_el[2], timeout=10, poll_frequency=1.0)
        return text_sea

    def add_people(self):
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[9], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[4], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[5], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[6], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[7], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        text_num = self.bas.text(Page.add_people_el[8], timeout=10, poll_frequency=1.0)
        return text_num

    def details_search(self,sea_data):
        time.sleep(1)
        self.bas.click_element(Page.add_people_el[8], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.details_search_el[0],sea_data["人员姓名"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.details_search_el[1],sea_data["登录账号"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_search_el[2], timeout=10, poll_frequency=1.0)
        text_sea = self.bas.text(Page.details_search_el[3], timeout=10, poll_frequency=1.0)
        return text_sea

    def details_delete(self):
        # self.bas.click_element(Page.add_people_el[8], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        element = self.bas.search_element(Page.details_delete_el[0])
        self.driver.execute_script("arguments[0].click();", element)
        # self.bas.click_element(Page.details_delete_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        element = self.bas.search_element(Page.details_delete_el[1])
        self.driver.execute_script("arguments[0].click();", element)
        # self.bas.click_element(Page.details_delete_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_delete_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_delete_el[3], timeout=10, poll_frequency=1.0)
        message_delete = self.bas.text(Page.details_delete_el[4], timeout=10, poll_frequency=1.0)
        return message_delete

    def role_details(self):
        time.sleep(1)
        self.bas.click_element(Page.role_details_el[0], timeout=10, poll_frequency=1.0)
        text_pri = self.bas.text(Page.role_details_el[1], timeout=10, poll_frequency=1.0)
        return text_pri


    def remove_people(self,re_reason):
        time.sleep(1)
        self.bas.click_element(Page.remove_people_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_people_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_people_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.remove_people_el[3], re_reason["移除原因"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_people_el[4], timeout=10, poll_frequency=1.0)
        message_remove = self.bas.text(Page.remove_people_el[5], timeout=10, poll_frequency=1.0)
        return message_remove

    def delete_role01(self):
        time.sleep(1)
        self.bas.click_element(Page.delete_role01_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.delete_role01_el[1], timeout=10, poll_frequency=1.0)
        message_delete = self.bas.text(Page.delete_role01_el[2], timeout=10, poll_frequency=1.0)
        return message_delete

    def delete_role02(self):#删除存在人员的角色
        time.sleep(1)
        self.bas.click_element(Page.delete_role02_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.delete_role02_el[1], timeout=10, poll_frequency=1.0)
        message_delete = self.bas.text(Page.delete_role02_el[2], timeout=10, poll_frequency=1.0)
        return message_delete

    def delete_roles(self):#批量删除存在人员的角色
        time.sleep(1)
        # self.bas.click_element(Page.delete_roles_el[0], timeout=10, poll_frequency=1.0)
        element = self.bas.search_element(Page.delete_roles_el[0])
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        self.bas.click_element(Page.delete_roles_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.delete_roles_el[2], timeout=10, poll_frequency=1.0)
        message_delete = self.bas.text(Page.delete_roles_el[3], timeout=10, poll_frequency=1.0)
        return message_delete

    def remove_admin(self, re_reason):
        time.sleep(1)
        self.bas.click_element(Page.remove_admin_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_admin_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_admin_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.remove_admin_el[3], re_reason["移除原因"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_admin_el[4], timeout=10, poll_frequency=1.0)
        message_remove = self.bas.text(Page.remove_admin_el[5], timeout=10, poll_frequency=1.0)
        return message_remove

    def add_authority(self):
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el, timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authority_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[4], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[5], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[6], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.data_authority_el[7], timeout=10, poll_frequency=1.0)

    def details_add(self):
        time.sleep(1)
        self.bas.click_element(Page.data_authority_el[7], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_add_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_add_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_add_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_add_el[3], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.details_add_el[4], timeout=10, poll_frequency=1.0)

    def details_search_aut(self,sear_data):
        # time.sleep(1)
        # self.bas.click_element(Page.data_authority_el[7], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.details_search_aut_el[0],sear_data["人员姓名"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.details_search_aut_el[1], sear_data["登录账号"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_search_aut_el[2], timeout=10, poll_frequency=1.0)
        search_text = self.bas.text(Page.details_add_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_search_aut_el[4], timeout=10, poll_frequency=1.0)
        return search_text

    def details_removes(self):
        time.sleep(1)
        self.bas.click_element(Page.details_removes_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_removes_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_removes_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_removes_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_removes_el[5], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_removes_el[4], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.details_removes_el[6], timeout=10, poll_frequency=1.0)

    def details_modify_role(self):
        time.sleep(1)
        self.bas.click_element(Page.details_modify_role_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_modify_role_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_modify_role_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_modify_role_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.details_modify_role_el[4], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.details_modify_role_el[5], timeout=10, poll_frequency=1.0)

    def add_authoritys(self):
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[4], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[5], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[6], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.add_authoritys_el[7], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.add_authoritys_el[8], timeout=10, poll_frequency=1.0)

    def remove_authority(self,remove_reason):
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[8], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[9], timeout=10, poll_frequency=1.0)
        # time.sleep(1)
        # self.bas.click_element(Page.remove_authority_el[4], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.remove_authority_el[5],remove_reason["移除原因"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_authority_el[6], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.remove_authority_el[7], timeout=10, poll_frequency=1.0)

    def remove_only(self,remove_reason):
        time.sleep(1)
        self.bas.click_element(Page.remove_only_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_only_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_only_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.remove_only_el[3],remove_reason["移除原因"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.remove_only_el[4], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.remove_only_el[5], timeout=10, poll_frequency=1.0)




