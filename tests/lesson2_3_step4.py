from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.get(url)

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    modal = driver.switch_to.alert
    modal.accept()

    x_value = driver.find_element_by_xpath("//div[@class='form-group']//label//span[@id='input_value']")
    x = x_value.text
    y = calc(x)

    input = driver.find_element_by_xpath("//div[@class='form-group']//input[@id='answer']")
    input.send_keys(y)

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    driver.quit()
