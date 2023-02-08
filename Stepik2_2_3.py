from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('ivan@gmail.com')

    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Text.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, '.btn')
    btn.click()

finally:
    time.sleep(10)

    browser.quit()
