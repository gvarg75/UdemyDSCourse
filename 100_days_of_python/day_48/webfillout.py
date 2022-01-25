from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/Greg/Desktop/web_drivers/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys('Greg')

lname = driver.find_element_by_name("lName")
lname.send_keys('Test')

email = driver.find_element_by_name('email')
email.send_keys("Testemail@email.com")
email.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()