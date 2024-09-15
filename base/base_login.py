from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class BaseLogin:
    def __init__(self, driver):
        self.driver: webdriver = driver

    def base_find_element(self, location, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*location))

    def base_click(self, location):
        self.base_find_element(location).click()

    def base_input(self, location, keyword):
        element = self.base_find_element(location)
        element.clear()
        element.send_keys(*keyword)

    def base_get_alert_msg(self):
        alert = self.driver.switch_to.alert
        result = alert.text
        alert.accept()
        return result


if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get("https://bilibili.com")
    location = (By.CLASS_NAME, "nav-search-input")
    keyword = ("abbb")
    print(*location)
    driver.find_element(*location).send_keys("1111")
    driver.find_element(*location).send_keys(*keyword)
    sleep(3)
    driver.quit()
    driver.switch_to.alert.accept()
