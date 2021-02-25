from Base.base import base
import Page
import time
class organization:
    #新增组织，修改组织，查询，修改，查询组织人数
    def __init__(self,driver):
        self.driver = driver
        self.bas = base(driver)
    def create_org(self,cte_data):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div[1]/div/div[2]/div[1]/div[2]/div[2]/button').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.ant-select-selection__placeholder').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="rc-tree-select-list_1"]/ul/li/span[2]').click()
        time.sleep(2)
        self.bas.send_text(Page.create_send[0],cte_data["组织名称"],timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.create_send[1], cte_data["组织编码"], timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.create_send[2], cte_data["组织描述"], timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.org_define,timeout=10, poll_frequency=1.0)

    def update_org(self,update_org_success):
        time.sleep(3)
        self.bas.click_element(Page.update_org,timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.update_org_send,update_org_success["组织名称"],timeout=10, poll_frequency=1.0)
        js = "var q=document.documentElement.scrollTop=150"
        self.driver.execute_script(js)
        time.sleep(2)
        self.bas.click_element(Page.org_define, timeout=10, poll_frequency=1.0)

    def delete_org(self,a):
        time.sleep(3)
        self.bas.click_element(Page.delete_org[a],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.delete_org[2],timeout=10, poll_frequency=1.0)

    def number_personnel(self):
        time.sleep(1)
        self.bas.click_element(Page.number_personnel[0],timeout=10, poll_frequency=1.0)
        text_num = self.bas.text(Page.number_personnel[1], timeout=10, poll_frequency=1.0)
        return text_num

    def search_org(self):
        pass

class company:
    def __init__(self, driver):
        self.driver = driver
        self.bas = base(driver)
    def create_com(self,cte_data):
        time.sleep(2)
        self.bas.click_element(Page.company, timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.create_com_click, timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.create_com_send[0],cte_data["单位名称"], timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.create_com_send[1],cte_data["单位简称"], timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.create_com_send[2],cte_data["单位描述"], timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.com_define, timeout=10, poll_frequency=1.0)

    def update_com(self,upt_data):
        time.sleep(2)
        self.bas.click_element(Page.company, timeout=10, poll_frequency=1.0)
        e = self.bas.search_elements(Page.update_com, timeout=10, poll_frequency=1.0)
        print(e)
        e[1].click()
        self.bas.send_text(Page.update_com_send,upt_data["单位名称"],timeout=10,poll_frequency=1.0)
        self.bas.click_element(Page.com_define, timeout=10, poll_frequency=1.0)


    def delete_com(self,a):
        time.sleep(2)
        self.bas.click_element(Page.company, timeout=10, poll_frequency=1.0)
        f = self.driver.find_elements_by_css_selector('.ant-table-tbody a:nth-child(3)')
        f[a].click()
        time.sleep(2)
        self.bas.click_element(Page.delete_com, timeout=10, poll_frequency=1.0)

    def search_com(self,sea_data):
        time.sleep(2)
        self.bas.click_element(Page.company,timeout=10,poll_frequency=1.0)
        self.bas.send_text(Page.search_com[0],sea_data["单位名称"],timeout=10,poll_frequency=1.0)
        self.bas.click_element(Page.search_com[1], timeout=10, poll_frequency=1.0)
        text_sea = self.bas.text(Page.search_com[2],timeout=10, poll_frequency=1.0)
        return text_sea








