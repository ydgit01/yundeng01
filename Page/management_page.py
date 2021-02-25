from Base.base import base
import time
import Page
class management:
    #管理页面
    def __init__(self,driver):
        self.bas = base(driver)
        self.driver = driver
    def click_tab(self,tab):#tab为数字类型
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=120"
        self.driver.execute_script(js)
        list1 = self.bas.search_elements(Page.management_centre_el,timeout=10, poll_frequency=1.0)
        list1[tab].click()




