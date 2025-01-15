import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    # Установите драйвер через Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.python.org")
    print(driver.title)
    time.sleep(3)
    driver.quit()
