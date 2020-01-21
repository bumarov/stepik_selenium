from selenium import webdriver
import time
import os




try:
    url = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(url)

    input_name = driver.find_element_by_xpath("//div[@class='form-group']//input[@name='firstname']")
    input_name.send_keys("Ivan")

    input_lastname = driver.find_element_by_xpath("//div[@class='form-group']//input[@name='lastname']")
    input_lastname.send_keys("Petrov")

    input_email = driver.find_element_by_xpath("//div[@class='form-group']//input[@name='email']")
    input_email.send_keys("Petrov@mail.ru")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'requirements.txt')
    element = driver.find_element_by_xpath("//input[@type='file']")
    element.send_keys(file_path)

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    driver.quit()
