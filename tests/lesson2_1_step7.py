from selenium import webdriver
import math
import time

url = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return ln(abs(12 * sin(x)))


try:
    driver = webdriver.Chrome()
    driver.get(url)

    x_value = driver.find_element_by_xpath("//div[@class='form-group']//label//span[@id='input_value']")
    x = x_value.text
    y = calc(x)

    input = driver.find_element_by_xpath("//div[@class='form-group']//input[@id='answer']")
    input.send_keys(y)

    chckbox = driver.find_element_by_xpath("//input[@id='robotCheckbox']")
    chckbox.click()

    radiobtn = driver.find_element_by_xpath("//input[@id='robotsRule']")
    radiobtn.click()

    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(30)
    driver.quit()
