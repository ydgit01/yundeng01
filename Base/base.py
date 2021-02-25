from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class base:
    #公共方法的实现，定位方法，输入方法，点击方法
    def __init__(self,driver):
        self.driver = driver
    def search_element(self,loc,timeout=10,poll_frequency=1.0):
        """
        :param loc: 元组（By.ID,ID为属性值）（By.class,class属性值）
        :param timeout:  搜索元素超时时间
        :param poll_frequency:  搜索间隔
        :return:  定位元素
        add = lambda x:x.find_element(*loc)
        value = add(driver)
        """
        return WebDriverWait(self.driver,timeout=10,poll_frequency=1.0).until(lambda x:x.find_element(*loc))

    def search_elements(self,loc,timeout=10,poll_frequency=1.0):
        """
        :param loc: 元组（By.ID,ID为属性值）（By.class,class属性值）
        :param timeout:  搜索元素超时时间
        :param poll_frequency:  搜索间隔
        :return:  定位元素
        add = lambda x:x.find_element(*loc)
        value = add(driver)
        """
        return WebDriverWait(self.driver,timeout=10,poll_frequency=1.0).until(lambda x:x.find_elements(*loc))

    def click_element(self,loc,timeout=10,poll_frequency=1.0):
        """
        :param loc: 元组（By.ID,ID为属性值）（By.class,class属性值）
        :param timeout:  搜索元素超时时间
        :param poll_frequency:  搜索间隔
        :return:  定位元素
        add = lambda x:x.find_element(*loc
        value = add(driver)
        """
        return self.search_element(loc,timeout=10,poll_frequency=1.0).click()

    def send_text(self,loc,data,timeout=10,poll_frequency=1.0):
        """
        :param loc: 元组（By.ID,ID为属性值）（By.class,class属性值）
        :param timeout:  搜索元素超时时间
        :param poll_frequency:  搜索间隔
        :return:  定位元素
        add = lambda x:x.find_element(*loc)
        value = add(driver)
        """
        self.search_element(loc, timeout=10, poll_frequency=1.0).clear()
        return self.search_element(loc,timeout=10,poll_frequency=1.0).send_keys(data)
    def text(self,loc,timeout=10,poll_frequency=1.0):
        """
               :param loc: 元组（By.ID,ID为属性值）（By.class,class属性值）
               :param timeout:  搜索元素超时时间
               :param poll_frequency:  搜索间隔
               :return:  定位元素
               add = lambda x:x.find_element(*loc)
               value = add(driver)
               """
        return self.search_element(loc, timeout=10, poll_frequency=1.0).text
