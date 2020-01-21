from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # вводим first name
    input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
    input1.send_keys("Alex")
    
    # вводим second name
    input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
    input2.send_keys("Kudryavtsev")
    
    # вводим e-mail    
    input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
    input3.send_keys("mymail@ku.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(3)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()