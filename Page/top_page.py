from Base.base import base
import Page
import time
class top:
    #工作台页面
    def __init__(self,driver):
        self.driver = driver
        self.bas = base(driver)

    def click_management(self):
        time.sleep(2)
        self.bas.click_element(Page.management,timeout=10, poll_frequency=1.0)


    def personal_setting(self):
        time.sleep(2)
        self.bas.click_element(Page.head_portrait,timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.setting[0], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        opers = self.bas.click_element(Page.personal_setting[0],timeout=10, poll_frequency=1.0)
        self.driver.execute_script("arguments[0].click();", opers)
        time.sleep(2)
        text_per = self.bas.text(Page.personal_setting[1],timeout=10,poll_frequency=1.0)
        return text_per

    def safe_setting(self,safe_data):
        time.sleep(2)
        self.bas.click_element(Page.head_portrait, timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.setting[1], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.send_text(Page.safe_setting[0],safe_data["原密码"])
        self.bas.send_text(Page.safe_setting[1], safe_data["新密码"])
        self.bas.send_text(Page.safe_setting[2], safe_data["确认密码"])
        self.bas.click_element(Page.safe_setting[3], timeout=10, poll_frequency=1.0)
        text_safe = self.bas.text(Page.login_safe, timeout=10, poll_frequency=1.0)
        return text_safe

    def my_authority(self):
        self.bas.click_element(Page.head_portrait, timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.setting[2], timeout=10, poll_frequency=1.0)
        text_aut = self.bas.text(Page.my_authority_obtain, timeout=10, poll_frequency=1.0)
        return text_aut

    def logout_system(self):
        time.sleep(2)
        self.bas.click_element(Page.head_portrait, timeout=10, poll_frequency=1.0)
        self.bas.click_element(Page.setting[3], timeout=10, poll_frequency=1.0)
        time.sleep(2)
        self.bas.click_element(Page.logout_define, timeout=10, poll_frequency=1.0)
        text_logout = self.bas.text(Page.login_safe, timeout=10, poll_frequency=1.0)
        return text_logout


    def help(self):
        time.sleep(2)
        self.bas.click_element(Page.help[0], timeout=10, poll_frequency=1.0)
        text_help = self.bas.text(Page.help[1], timeout=10, poll_frequency=1.0)
        return text_help

    def view_news(self):
        time.sleep(2)
        self.bas.click_element(Page.view_news[0], timeout=10, poll_frequency=1.0)
        text_news = self.bas.text(Page.view_news[1], timeout=10, poll_frequency=1.0)
        return text_news


    def head_portrait_modification(self):
        pass







