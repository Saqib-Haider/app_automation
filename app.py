from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_login_logout():
    options = UiAutomator2Options()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '10')
    options.set_capability('deviceName', 'emulator-5554')
    options.set_capability('appPackage', 'com.breemobile')
    options.set_capability('appActivity', 'com.breemobile.MainActivity')
    options.set_capability('noReset', True)
    options.set_capability('automationName', 'UiAutomator2')

    driver = webdriver.Remote('http://192.168.4.24:4723', options=options)

    try:
        time.sleep(5)
        update = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Go to store")')
        update.click()

        time.sleep(3)
        login = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")')
        login.click()

        time.sleep(3)
        email = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("john@trybree.com")')
        email.send_keys("zoey+v013@trybree.com")

        time.sleep(3)
        password = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("@breepassword1")')
        password.click()
        password.send_keys("Qwe123456@")

        driver.press_keycode(4)

        login_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiSelector().text("Log in").className("android.widget.TextView").index(0)')
        login_button.click()
        time.sleep(5)

        update = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Go to store")')
        update.click()
        time.sleep(5)

        dashboard = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Zoey")')
        assert dashboard.is_displayed()

        settings = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings").index(2)')
        settings.click()
        time.sleep(3)

        logout = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log out")')
        logout.click()
        time.sleep(3)

    finally:
        driver.quit()


test_login_logout()
