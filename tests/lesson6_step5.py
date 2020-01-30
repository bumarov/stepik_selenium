from selenium import webdriver
import math
import time

url = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    driver = webdriver.Chrome()
    driver.get(url)
    link = driver.find_element_by_link_text(str(text))
    link.click()

    input1 = driver.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id('country')
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
