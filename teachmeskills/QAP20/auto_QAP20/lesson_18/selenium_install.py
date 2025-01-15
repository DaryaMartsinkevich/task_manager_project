import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.selenium.dev/documentation/webdriver/browsers/chrome/')
time.sleep(10)
driver.close()
driver.quit()