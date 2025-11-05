from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# Open WEb Driver
driver = webdriver.open()
driver.maximize_window()
driver.delete_all_cookies()

#Navigate to webpage
path = ""
driver.get(path)

# Set Up Waiter
waiter = webdriver.support.wait.WebDriverWait(driver, 60)
waiter.until(EC.visibility_of_element_located((By.ID, "hidden_element")))
# selenium will wait for 60 seconds until you press some button

# Locate element
label_hidden = driver.find_element(By.Id, "hidden_element")

# Print the value of the hidden element
print(label_hidden.get_attribute("innerHTML"))

# Close
driver.close()