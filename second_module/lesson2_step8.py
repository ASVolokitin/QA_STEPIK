import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("bla")
    browser.find_element(By.NAME, "lastname").send_keys("bla")
    browser.find_element(By.NAME, "email").send_keys("bla")

    browser.find_element(By.NAME, "file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lesson1_step5.py'))

    
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()