from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
       
class BaseApp:
    def __init__(self, driver):
        self.driver = driver
        self.link = 'https://testpages.eviltester.com/styled/dynamic-buttons-simple.html'

    def go_to_site(self):
        self.driver.get(self.link)

    def find_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))