import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"

try:
  
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(value))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()