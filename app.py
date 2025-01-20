import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



@pytest.fixture(scope="module")
def appium_driver():
    options = UiAutomator2Options()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '10')
    options.set_capability('deviceName', 'emulator-5554')
    options.set_capability('appPackage', 'com.breemobile')
    options.set_capability('appActivity', 'com.breemobile.MainActivity')
    options.set_capability('noReset', True)
    options.set_capability('automationName', 'UiAutomator2')

    driver = webdriver.Remote('http://192.168.4.24:4723', options=options)
    yield driver 
    driver.quit()



def test_navigate_to_login(appium_driver):
    driver = appium_driver
    time.sleep(5)
    update = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Go to store")')
    update.click()
    time.sleep(3)
    login = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")')
    assert login.is_displayed()
    login.click()



def test_login(appium_driver):
    driver = appium_driver
    time.sleep(3)
    email = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("john@trybree.com")')
    email.send_keys("saqibhaider567@gmail.com")

    time.sleep(3)
    password = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("@breepassword1")')
    password.click()
    password.send_keys("rrrrrr")


    driver.press_keycode(4)

    login_button = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Log in").className("android.widget.TextView").index(0)'
    )
    login_button.click()
    time.sleep(5)


def test_dashboard(appium_driver):
    driver = appium_driver
    dashboard = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Saqib,")')
    assert dashboard.is_displayed()



def test_logout(appium_driver):
    driver = appium_driver
    settings = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
    settings.click()
    time.sleep(3)
    logout = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log out")')
    assert logout.is_displayed()
    logout.click()
    time.sleep(3)
