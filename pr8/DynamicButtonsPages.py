from BaseApp import BaseApp
from selenium.webdriver.common.by import By

class DynamicButtonsLocator:
    BUTTON_0 = (By.ID, 'button00')
    BUTTON_1 = (By.ID, 'button01')
    BUTTON_2 = (By.ID, 'button02')


class SearchHelper(BaseApp):
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_button_0(self):
        return self.find_element(DynamicButtonsLocator.BUTTON_0, 10).click()

    def click_button_1(self):
        return self.find_element(DynamicButtonsLocator.BUTTON_1, 10).click()

    def click_button_2(self):
        return self.find_element(DynamicButtonsLocator.BUTTON_2, 10).click()