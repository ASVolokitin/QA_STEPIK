from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)))

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()