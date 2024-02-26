from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 
import os
import time
class TestPr6:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def quit_driver(self):
        self.driver.quit()

    def html_form_test(self):
        self.driver.get("https://testpages.eviltester.com/styled/html5-form-test.html")

        colour_picker = self.driver.find_element(By.ID, "colour-picker")
        colour_picker.clear()
        colour_picker.send_keys('#32a852')
        assert(colour_picker.get_attribute('value') == '#32a852')

        date_picker = self.driver.find_element(By.ID, "date-picker")
        date_picker.clear()
        date_picker.send_keys('26-02-2024')
        assert(date_picker.get_attribute('value') == '2024-02-26')
        
        date_time_picker = self.driver.find_element(By.ID, "date-time-picker")
        date_time_picker.clear()
        date_time_picker.send_keys('26-02-2024', Keys.TAB, '12:00')
        assert(date_time_picker.get_attribute('value') == '2024-02-26T12:00')

        email_field = self.driver.find_element(By.ID, "email-field")
        email_field.clear()
        email_field.send_keys('artem.shevchuk0207@gmail.com')
        assert(email_field.get_attribute('value') == 'artem.shevchuk0207@gmail.com')
    
        month_field = self.driver.find_element(By.ID, "month-field")
        month_field.clear()
        month_field.send_keys('2', Keys.TAB, '2024')
        assert(month_field.get_attribute('value') == '2024-02')
    
        number_field = self.driver.find_element(By.ID, "number-field")
        number_field.clear()
        number_field.send_keys('33')
        assert(number_field.get_attribute('value') == '33')

    def auth_test(self):
        self.driver.get("https://testpages.eviltester.com/styled/auth/basic-auth-test.html")

        username = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/p[3]").text
        username = username.split(' ')[1]
        password = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/p[4]").text
        password = password.split(' ')[1]
        
        link = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/p[5]/a').get_attribute('href') 
        url = 'http://{}:{}@{}'.format(username, password, link.replace("https://", ""))
        self.driver.get(url)
        status = self.driver.find_element(By.ID, 'status').text
        assert(status == 'Authenticated')


    def file_upload_test(self):
        self.driver.get('https://testpages.eviltester.com/styled/file-upload-test.html')
        self.driver.find_element(By.ID, 'fileinput').send_keys(os.path.dirname(__file__) + "/test.txt")
        self.driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[3]/input').click()
        text = self.driver.find_element(By.ID, 'uploadedfilename').text
        assert(text == 'test.txt')

    def alerts_test(self):
        self.driver.get('https://testpages.eviltester.com/styled/alerts/alert-test.html')

        self.driver.find_element(By.ID, 'confirmexample').click()

        alert = Alert(self.driver)
        alert.accept() 
        confirm_return = self.driver.find_element(By.ID, 'confirmreturn').text
        assert(confirm_return == 'true')


        
if __name__ == '__main__':
    testPr6 = TestPr6()

    testPr6.html_form_test()
    testPr6.auth_test()
    testPr6.file_upload_test()
    testPr6.alerts_test()

    testPr6.quit_driver()