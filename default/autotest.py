# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Login


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_bla(app):
    app.open_home_page()
    app.login(Login(login="w@w.com",password="111111"))
    app.add_new_address(new_address="Москва, улица Александра Солженицына, 23Ас1")
    app.logout()

# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.driver.implicitly_wait(30)

    def logout(self):
        wd = self.driver
        wd.find_element_by_xpath("//ul[@class='user-profile__list']//span[.='Выход']").click()
        time.sleep(3)

    def add_new_address(self, new_address):
        wd = self.driver
        wd.find_element_by_id("user-addr__input").click()
        wd.find_element_by_id("user-addr__input").clear()
        wd.find_element_by_id("user-addr__input").send_keys(new_address)
        wd.find_element_by_link_text(new_address).click()
        wd.find_element_by_css_selector("a.user-addr__submit.sbm-btn").click()
        time.sleep(2)
        wd.find_element_by_css_selector("span.user-profile__span").click()
        time.sleep(2)

    def open_home_page(self):
        # open home page
        wd = self.driver
        wd.get("http://www.delivery-club.ru/")

    def login(self, Login):
        wd = self.driver
        wd.find_element_by_link_text("Вход / Регистрация").click()
        wd.find_element_by_name("c_l").click()
        wd.find_element_by_name("c_l").clear()
        wd.find_element_by_name("c_l").send_keys(Login.login)
        wd.find_element_by_name("c_p").click()
        wd.find_element_by_name("c_p").clear()
        wd.find_element_by_name("c_p").send_keys(Login.password)
        wd.find_element_by_link_text("ВОЙТИ").click()
        time.sleep(2)
        self.open_profile_page()
        time.sleep(2)

    def open_profile_page(self):
        wd = self.driver
        wd.find_element_by_css_selector("span.user-profile__span").click()
        wd.find_element_by_css_selector("span.user-profile__title").click()

    def destroy(self):
        wd = self.driver
        wd.quit()