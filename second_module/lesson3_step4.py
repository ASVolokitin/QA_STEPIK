import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    browser.switch_to.alert.accept()
    browser.find_element(By.ID, "answer").send_keys(calc(int(browser.find_element(By.ID, "input_value").text)))

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    ans = browser.switch_to.alert.text.split(":")[-1]
    print(ans)


finally:
    time.sleep(10)
    browser.quit()