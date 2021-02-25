
import time
import os
def sav_creenshot(driver):
    now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())) # 截图保存的文件名格式
    pic_path = 'D:\\yundeng_ui\\pictures'+os.sep+now+".png"# 截图保存的路径
    print(pic_path)
    driver.save_screenshot(pic_path)# 调用Driver的截图保存功能
    file = open(pic_path, 'rb').read()
    return file
