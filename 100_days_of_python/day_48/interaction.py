from selenium import webdriver
import time

chrome_driver_path = '/Users/Greg/Desktop/web_drivers/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element_by_css_selector("#articlecount > a:nth-child(1)")
time.sleep(3)
count.click()
time.sleep(3)


driver.quit()