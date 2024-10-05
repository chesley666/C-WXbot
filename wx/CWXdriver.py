# -*- coding=utf-8 -*-

#appium控制微信

import os,sys,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from config.mediaconfig import *

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.tencent.mm',
    # appActivity='com.tencent.mm.ui.LauncherUI',
    appActivity = 'com.tencent.mm.plugin.scanner.ui.BaseScanUI',
    fullReset=False,
    noReset=True,
    deviceReadyTimeout='30',
    unicodeKeyboard=True,
    resetKeyboard=True,
    skipUnlock=True,
    enforceXPath1=True
)
appium_server_url = 'http://localhost:4723'

class WXdriver:
    def __init__(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities)
            )
        self.driver.activate_app('com.tencent.mm')
        
    def __exit__(self):
        self.driver.quit()


    def scanqrcode(self):
        time.sleep(2)#等微信启动完
        self.driver.find_element(by=AppiumBy.ID, value='com.tencent.mm:id/jga').click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.LinearLayout[@resource-id="com.tencent.mm:id/m7g"])[3]').click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.ID, value='com.tencent.mm:id/mj5').click()
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.RelativeLayout[@resource-id="com.tencent.mm:id/root_view"])[1]').click()
        time.sleep(2)
        self.driver.quit()
        #切了windows，重建session
        # self.driver.start_session(capabilities) 
        self.driver = webdriver.Remote(
            appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities)
            )
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="登录"]').click()
        time.sleep(2)
        

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    WX = WXdriver()
    WX.scanqrcode('../meta/qrcode.jpg')
    time.sleep(3)
    