from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://demo.opencart.com/index.php?route=common/home&language=en-gb"
browser = driver = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)

driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]/a').click()

driver.find_element(By.XPATH, '//*[@id="product-list"]/div/form/div/div[2]/div[1]/h4/a').click()

assert  driver.find_element(By.XPATH, "//p[contains(text(),'megapixels')]").is_displayed()

browser.quit()


