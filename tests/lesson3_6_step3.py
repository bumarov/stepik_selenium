from selenium import webdriver
import pytest
import math
import time

urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


class TestUrls():

    @pytest.mark.parametrize("link", urls)
    def test_parametrized_urls(self, driver, link):
        answer = math.log(int(time.time()))
        driver.get(link)
        driver.implicitly_wait(5)
        text_area = driver.find_element_by_xpath("//div//textarea")
        text_area.send_keys(str(answer))

        button = driver.find_element_by_xpath("//button")
        button.click()

        hint_text = driver.find_element_by_xpath("//pre")
        assert hint_text.text == "Correct!"
        driver.quit()
