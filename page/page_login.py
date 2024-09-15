from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from po模式v4 import page
from po模式v4.base.base_login import BaseLogin


class PageLogin(BaseLogin):
    def __init__(self):
        driver = webdriver.Edge()
        driver.get("D:\JavaMainProject2024\python2024\\ut_and_sel\po模式v3\网站\login.html")
        driver.maximize_window()
        super().__init__(driver)

    def page_input_msg(self, username, password, code):
        self.base_input(page.username_loc, username)
        self.base_input(page.pwd_loc, password)
        self.base_input(page.varify_loc, code)
        self.base_click(page.sub_loc)

    def page_get_msg(self):
        return self.base_get_alert_msg()
