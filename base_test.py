import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from global_settings.login import perform_login
from global_settings.locators import locators


class BaseTest(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "appium:platformVersion": "9",
            "appium:appiumdeviceName": "52001064613fb429",
            "appium:app": "C:\\Users\\Aisultan\\Downloads\\otbasy_test.apk",
            "appium:automationName": "UiAutomator2"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.wait = WebDriverWait(self.driver, 30)
        self.all_locators = locators()
        perform_login(self.driver, self.wait, self.all_locators)

    def tearDown(self):
        pass

