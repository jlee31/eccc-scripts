from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

import time

# Open the webdriver and formatting
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()

# Navigate to web page
driver.get("http://google.com")

# Using HTML/CSS To find search fields 
search_bar = driver.find_element(By.NAME ,"q")

# Type Query
search_bar.send_keys("Hello bro")

# Click enter
search_bar.send_keys(Keys.RETURN)

time.sleep(3) # wait three seconds

# Close
driver.close()