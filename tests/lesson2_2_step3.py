from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

url = "http://suninjuly.github.io/selects1.html"


try:
    driver = webdriver.Chrome()
    driver.get(url)
    

    input1 = driver.find_element_by_xpath("//h2//span[@id='num1']")
    num1 = input1.text
    input2 = driver.find_element_by_xpath("//h2//span[@id='num2']")
    num2 = input2.text

    num = int(num1) + int(num2)

    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(num))     

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()
