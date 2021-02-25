from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('http://yundeng-console.common.aliyun.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element_by_id('tenantCode').send_keys('yuedantest')
# driver.find_element_by_id('username').send_keys('yuedantestadmin')
# driver.find_element_by_id('password').send_keys('Qwer@2020')
# driver.execute_script('arguments[0].click();', driver.find_element_by_id("check_submit"))
# time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/section/header/ul/li[3]/i').click()
driver.find_element_by_css_selector("")
# time.sleep(2)
# #管理
# a = driver.find_elements_by_css_selector('.ant-row .ant-col .item___2VSxG .link___1BNhq')
# a[0].click()
# #单位
# time.sleep(2)
# driver.find_element_by_css_selector('.tabs____iMBm span:nth-child(2)').click()
# time.sleep(2)
# #driver.find_element_by_css_selector('.operation___1HLO8 .ant-btn-primary').click()
# # e = driver.find_elements_by_css_selector('.ant-table-tbody a:nth-child(1)')
# # e[0].click()
# f = driver.find_elements_by_css_selector('.ant-table-tbody a:nth-child(3)')
# f[0].click()


import requests
import time

from selenium import webdriver
from PIL import Image
from Base.creenShot import sav_creenshot
#
#
# def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
#     driver.maximize_window()
#     driver.find_element_by_css_selector('.forget_password').click()
#     img = driver.find_element_by_css_selector('#refreshImg')
#     time.sleep(2)
#     location = img.location
#     print(location)
#     size = img.size
#     left = location['x']
#     top = location['y']
#     right = left + size['width']
#     bottom = top + size['height']
#     page_snap_obj = sav_creenshot(driver)
#     image_obj = page_snap_obj.crop((left, top, right, bottom))
#     return image_obj  # 得到的就是验证码
#
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("http://yundeng-console.common.aliyun.com/")
#     b = get_image(driver)
#     b.save("1.png")
#     print(b)
#     driver.quit()  # 一定要退出！不退出会有残留进程！


import pytesseract
from PIL import Image
import PIL
import cv2


def part_screenshot(driver):
    driver.save_screenshot("hello1.png")
    return Image.open("hello1.png")

def forget_password():
    driver = webdriver.Chrome()
    driver.get("http://yundeng-console.common.aliyun.com/")
    driver.maximize_window()
    driver.find_element_by_css_selector('.forget_password').click()
      # 截取当前网页，该网页有我们需要的验证码
    time.sleep(2)
    page_snap_obj = part_screenshot(driver)
    image_obj = page_snap_obj.crop((1247, 412,1390,458))
    image_obj.show()
    image_obj.save("image_obj.png")
    image = Image.open('genPicVerifyCode.png')
    imgry = image.convert('L')
    imgry.show()

    # threshold = 140
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    # out = imgry.point(table, '1')
    # out.show()
    # im_inv = cv2.threshold(out,127,255,cv2.THRESH_BINARY_INV)
    # im_inv.show()
    text = pytesseract.image_to_string(imgry,lang='eng').split()
    print(text)
     # 得到的就是验证码


    # text = image_to_string('result.png', 'eng').strip()

forget_password()


