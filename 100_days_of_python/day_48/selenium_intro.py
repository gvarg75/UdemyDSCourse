from selenium import webdriver
import time


chrome_driver_path = '/Users/Greg/Desktop/web_drivers/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://selenium-python.readthedocs.io/page-objects.html')

price = driver.find_element_by_xpath("//div[@id='test-case']/h2")
print(price.text)

driver.quit()