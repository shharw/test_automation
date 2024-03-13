import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver_setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
