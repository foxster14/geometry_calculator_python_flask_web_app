import time
from selenium import webdriver


driver = webdriver.Chrome('/Users/sarahfox/Downloads/chromedriver')
driver.get('http://www.google.com/')

# Pause for 5 seconds before executing next command
time.sleep(5)

# Enter 'q' in search box & perform a google search
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

# pause for 5 seconds before exiting browser
time.sleep(5) 
driver.quit()