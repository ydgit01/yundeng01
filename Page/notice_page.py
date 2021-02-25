from Base.base import base
import time
import Page
class Notice:
    def __init__(self,driver):
        self.bas = base(driver)
        self.driver = driver

    def create_column(self,create_data):
        time.sleep(1)
        self.bas.click_element(Page.create_column_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_column_el[1], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.create_column_el[2],create_data["分类名称"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_column_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.create_column_el[4], create_data["原因备注"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_column_el[5], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.create_column_el[6], timeout=10, poll_frequency=1.0)

    def update_column(self,update_data):
        time.sleep(1)
        self.bas.click_element(Page.update_column_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.update_column_el[1],update_data["分类名称"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.update_column_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.update_column_el[3], update_data["原因备注"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.update_column_el[4], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.update_column_el[6], timeout=10, poll_frequency=1.0)

    def start_using(self):
        time.sleep(1)
        self.bas.click_element(Page.start_using_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.start_using_el[1], timeout=10, poll_frequency=1.0)

    def delete_column(self):
        time.sleep(1)
        self.bas.click_element(Page.delete_column_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.delete_column_el[1], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.delete_column_el[2], timeout=10, poll_frequency=1.0)

    def create_notice(self,create_data):
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.create_notice_el[1],create_data["公告标题"],timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.create_notice_el[2], create_data["公告详情"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        element = self.bas.search_element(Page.create_notice_el[3])
        self.driver.execute_script("arguments[0].click();", element)
        # self.bas.click_element(Page.create_notice_el[3], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[4], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[5], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[6], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[7], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[8], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.create_notice_el[9], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.create_notice_el[10], timeout=10, poll_frequency=1.0)

    def edit_send(self,edit_data):
        time.sleep(1)
        self.bas.click_element(Page.edit_send_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.send_text(Page.edit_send_el[1],edit_data["公告标题"], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        element = self.bas.search_element(Page.edit_send_el[2])
        self.driver.execute_script("arguments[0].click();", element)
        # self.bas.click_element(Page.edit_send_el[2], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.edit_send_el[3], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.edit_send_el[4], timeout=10, poll_frequency=1.0)

    def recall_notice(self):
        time.sleep(1)
        self.bas.click_element(Page.recall_notice_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.recall_notice_el[1], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.recall_notice_el[2], timeout=10, poll_frequency=1.0)

    def delete_notice(self):
        time.sleep(1)
        self.bas.click_element(Page.delete_notice_el[0], timeout=10, poll_frequency=1.0)
        time.sleep(1)
        self.bas.click_element(Page.delete_notice_el[1], timeout=10, poll_frequency=1.0)
        return self.bas.text(Page.delete_notice_el[2], timeout=10, poll_frequency=1.0)






