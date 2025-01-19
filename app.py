from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the options for Appium v2
options = UiAutomator2Options()
options.set_capability('platformName', 'Android')
options.set_capability('platformVersion', '10')
options.set_capability('deviceName', 'emulator-5554')
options.set_capability('appPackage', 'com.breemobile')
options.set_capability('appActivity', 'com.breemobile.MainActivity')
options.set_capability('noReset', True)
options.set_capability('automationName', 'UiAutomator2')

# Initialize the driver with the correct capabilities
driver = webdriver.Remote('http://192.168.4.24:4723', options=options)

# Example: Find an element by its text and perform an action
time.sleep(5)
update = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Go to store")')
update.click()

# Wait for a few seconds to observe the action
time.sleep(3)
login = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")')
login.click()

time.sleep(3)
email = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("john@trybree.com")')
email.send_keys("saqibhaider567@gmail.com")

time.sleep(3)
password = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("@breepassword1")')
password.click()
password.send_keys("rrrrrr")

login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in")'))
)
login.click()
time.sleep(5)

update = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Go to store")')
update.click()
time.sleep(5)

dashboard = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Good Evening,")')
assert dashboard.is_displayed()


settings = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
settings.click()
time.sleep(3)

logout = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log out")')
logout.click()
time.sleep(3)


# Close the session
driver.quit()
