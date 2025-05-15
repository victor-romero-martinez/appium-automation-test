import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selenium.webdriver.ie.webdriver import WebDriver
from utils import device_info

load_dotenv()

capability = {
    'platformName': 'Android',
    'automationName': os.environ.get('AUTOMATION_NAME'),
    'appPackage': os.environ.get('APP_PACKAGE'),
    'appActivity': os.environ.get('APP_ACTIVITY'),
    'ensureWebviewsHavePages': "true",
    'nativeWebScreenshot': "true",
    'connectHardwareKeyboard': "true"
}

merge_capability = {**capability, **device_info.get_device_info()}


def get_driver() -> WebDriver:
    return webdriver.Remote(
        os.environ.get('BASE_URL'), options=UiAutomator2Options().load_capabilities(merge_capability)
    )
