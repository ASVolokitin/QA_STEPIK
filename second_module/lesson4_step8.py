import time
import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def copy_answer(browser):
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    ans = browser.switch_to.alert.text.split(":")[-1]
    pyperclip.copy(ans)
    return ans

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()

    browser.find_element(By.ID, "answer").send_keys(calc(int(browser.find_element(By.ID, "input_value").text)))
    
    copy_answer(browser)

    
finally:
    time.sleep(10)
    browser.quit()