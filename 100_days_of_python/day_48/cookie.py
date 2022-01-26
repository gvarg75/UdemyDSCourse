from selenium import webdriver
import time

chrome_driver_path = '/Users/Greg/Desktop/web_drivers/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

start_time = time.time()
seconds = 5

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        cookie.click()
    else:
        cookie.click()
        current_time = time.time()
        money = driver.find_element_by_id("money")
        cursor_price = driver.find_element_by_xpath('//*[@id="buyCursor"]/b')
        grandma_price = driver.find_element_by_xpath('//*[@id="buyGrandma"]/b')
        factory_price = driver.find_element_by_xpath('//*[@id="buyFactory"]/b')
        mine_price = driver.find_element_by_xpath('//*[@id="buyMine"]/b')
        print(cursor_price.text, grandma_price.text, factory_price.text, mine_price.text)
        #if int(money) >
