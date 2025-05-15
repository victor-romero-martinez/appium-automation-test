from time import sleep

import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.driver_factory import get_driver

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = get_driver()

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        el = wait.until(ec.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Login"]')))
        el.click()
        sleep(5)


if __name__ == '__main__':
    unittest.main()
