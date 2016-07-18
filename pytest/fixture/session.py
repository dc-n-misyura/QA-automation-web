# -*- coding: utf-8 -*-
import time

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, Login):
        wd = self.app.driver
        wd.find_element_by_link_text("Вход / Регистрация").click()
        wd.find_element_by_name("c_l").click()
        wd.find_element_by_name("c_l").clear()
        wd.find_element_by_name("c_l").send_keys(Login.login)
        wd.find_element_by_name("c_p").click()
        wd.find_element_by_name("c_p").clear()
        wd.find_element_by_name("c_p").send_keys(Login.password)
        wd.find_element_by_link_text("ВОЙТИ").click()
        time.sleep(2)
        self.app.open_profile_page()
        time.sleep(2)

    def logout(self):
        wd = self.app.driver
        time.sleep(3)
        wd.find_element_by_xpath("//ul[@class='user-profile__list']//span[.='Выход']").click()
        time.sleep(3)