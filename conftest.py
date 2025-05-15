import pytest
from utils.driver_factory import get_driver


@pytest.fixture(scope='session')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
