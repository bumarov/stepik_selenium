from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(url)

    price = driver.find_element_by_xpath("//h5[@id='price']")
    

    button = driver.find_element_by_xpath("//button[@type='submit']")
    button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x_value = driver.find_element_by_xpath("//div[@class='form-group']//label//span[@id='input_value']")
    x = x_value.text
    y = calc(x)

    input = driver.find_element_by_xpath("//div[@class='form-group']//input[@id='answer']")
    input.send_keys(y)

    button = driver.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(15)
    driver.quit()
