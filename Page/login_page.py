from Base.base import base
import Page

class login:

    #登录页面
    def __init__(self,driver):
        self.driver = driver
        self.bas = base(driver)

    def log(self,log_data):
        self.bas.send_text(Page.login[0],log_data["租户"],timeout=10,poll_frequency=1.0)
        self.bas.send_text(Page.login[1], log_data["账号"], timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.login[2], log_data["密码"], timeout=10, poll_frequency=1.0)
        self.driver.execute_scrip('arguments[0].click();', self.driver.find_element_by_id("check_submit"))

        'var a = document.gtElementById("#check_submit");a.click()'

    def log_checking(self,log_data):
        self.bas.send_text(Page.login[0],log_data["租户"],timeout=10,poll_frequency=1.0)
        self.bas.send_text(Page.login[1], log_data["账号"], timeout=10, poll_frequency=1.0)
        self.bas.send_text(Page.login[2], log_data["新密码登录"], timeout=10, poll_frequency=1.0)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element_by_id("check_submit"))

