import pytest
from appium.webdriver.common.appiumby import By


def test_find_login_btn(driver):
    try:
        element = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Logind"]')
        assert element.is_displayed()
        print('The element is visible')
    except Exception as e:
        pytest.fail(f"{e}")

def test_interation_login_btn(driver):
    try:
        element = driver.find_element(By.XPATH, '//android.view.View[@content-desc="Login"]')
        element.click()
        print("Bottom clicked")
    except Exception as e:
        pytest.fail(f"{e}")