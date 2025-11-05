from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

# Open the webdriver and formatting
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()

# Navigate to web page
path = "public/"
driver.get(path)
time.sleep(1)

# Locate all the elemeents
txt_user = driver.find_element(By.ID, "user")
txt_password = driver.find_element(By.NAME, "password")

# X Path
btn_submit = driver.find_element(By.XPATH, "") # You can find the xPath via inspect element
label_banner = driver.find_element(By.CSS_SELECTOR, "p.banner") # paragraph with banner classs

# Inputting Credentials
# good practice to clear before doing anything
txt_user.clear()
txt_user.send_keys("SAMPLE USERNAME")

txt_password.clear()
txt_password.send_keys("123456789")

# Retrieve the Banner Text
print(label_banner.get_attribute("innerHTML"))

# Submit via submit button
btn_submit.click()
time.sleep(3)

# Close web driver
driver.close()