import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

try:
  
  browser = webdriver.Chrome()
  browser.get(link)

  value = browser.find_element(By.ID, "treasure").get_attribute("valuex")
  browser.find_element(By.ID, "answer").send_keys(calc(value))

  browser.find_element(By.ID, "robotCheckbox").click()

  browser.find_element(By.ID, "robotsRule").click()

  button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  button.click()

finally:
  time.sleep(10)
  browser.quit()