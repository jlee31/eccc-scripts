# have selenium installed
# you also need an app that can control the web browser

# https://www.youtube.com/watch?v=NB8OceGZGjA

'''
Quick Selenium Notes:

For automating web browsers and scraping
Selenium webdriver - for browser interactions
selenium grid - for parallel testing on multiple machines or browsers
selenium ide - for testing (not sure if i need that though)

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

