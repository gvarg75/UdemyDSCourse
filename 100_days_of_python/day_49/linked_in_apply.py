from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from dotenv import load_dotenv

load_dotenv()

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
chrome_driver_path = "C:\Development\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/")
time.sleep(5)
sign_in = driver.find_element(
    By.CSS_SELECTOR, "body > div > main > div > form > section > p.authwall-join-form__swap-cta > button")
sign_in.click()
time.sleep(3)
email_field = driver.find_element(By.XPATH, '//*[@id="session_key"]')
password_field = driver.find_element(By.XPATH, '//*[@id="session_password"]')

email_field.send_keys(email)
password_field.send_keys(password)

sign_in_button = driver.find_element_by_class_name(
    "sign-in-form__submit-button")
sign_in_button.click()
try:
    driver.find_element(By.LINK_TEXT, "Confirm").click()
except:
    pass

time.sleep(3)
driver.get("https://www.linkedin.com/jobs/")
try:
    driver.find_element(By.LINK_TEXT, "See more jobs").click()
except:
    pass