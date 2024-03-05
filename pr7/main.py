from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestPr7:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = 'https://testpages.eviltester.com/styled/dynamic-buttons-simple.html'
        
    def quit_driver(self):
        self.driver.quit()

    def check_exists(self, id):
        try:
            self.driver.find_element(By.ID, id)
        except NoSuchElementException:
            return False
        return True

    def task1(self):
        self.driver.get(self.link)
        self.driver.find_element(By.ID, 'button00').click()
        self.driver.find_element(By.ID, 'button01').click()
        time.sleep(5)
        self.driver.find_element(By.ID, 'button02').click()
        self.check_exists('button02')

    def task2(self):
        self.driver.get(self.link)
        self.driver.find_element(By.ID, 'button00').click()
        self.driver.find_element(By.ID, 'button01').click()
        self.driver.implicitly_wait(5)
        self.check_exists('button02')
        self.driver.implicitly_wait(0)

    def task3(self):
        self.driver.get(self.link)
        self.driver.find_element(By.ID, 'button00').click()
        self.driver.find_element(By.ID, 'button01').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "button02")))
        self.check_exists('button02')
        
        
if __name__ == '__main__':
    testPr7 = TestPr7()

    testPr7.task1()
    testPr7.task2()
    testPr7.task3()

    testPr7.quit_driver()