from selenium import webdriver
import math
import time

url = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get(url)

    x_value = driver.find_element_by_xpath("//div[@class='form-group']//label//span[@id='input_value']")
    x = x_value.text
    y = calc(x)

    input = driver.find_element_by_xpath("//div[@class='form-group']//input[@id='answer']")
    input.send_keys(y)

    chckbox = driver.find_element_by_xpath("//label[@for='robotCheckbox']")
    chckbox.click()

    radiobtn = driver.find_element_by_xpath("//label[@for='robotsRule']")
    radiobtn.click()
    
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
