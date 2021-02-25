from selenium import webdriver
def get_driver():
    driver = webdriver.Chrome()
    driver.get('http://yundeng-console.common.aliyun.com/')
    return driver