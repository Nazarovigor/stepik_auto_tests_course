from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, '.btn')
    btn1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x1 = browser.find_element(By.ID, 'input_value')
    x= x1.text

    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    btn2 = browser.find_element(By.CSS_SELECTOR, '.btn')
    btn2.click()


finally:
    time.sleep(10)
    browser.quit()
