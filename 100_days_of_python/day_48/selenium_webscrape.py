from selenium import webdriver

chrome_driver_path = '/Users/Greg/Desktop/web_drivers/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_date = driver.find_elements_by_css_selector("div.medium-widget.event-widget.last > div > ul > li")


event_date = [i.text for i in event_date]
event_date = event_date.split('\n')

dates = event_date[::2]
event = event_date[1::2]


event = [i.text for i in event]
dates = [i.text for i in dates]
print(event_date, event, dates)
driver.quit()
