# -*- coding: utf-8 -*-
from selenium import webdriver
# from fixture.session import SessionHelper
from fixture.group import GroupHelper
import time

class Application:

    def __init__(self):
        # self.driver = webdriver.Remote(
        # desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
        # command_executor='http://192.168.1.123:4444/wd/hub')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.driver.implicitly_wait(30)
        # self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        # open home page
        wd = self.driver
        wd.get("http://www.delivery-club.ru/")

    def destroy(self):
        wd = self.driver
        wd.quit()

    def open_profile_page(self):
        wd = self.driver
        wd.find_element_by_css_selector("span.user-profile__span").click()
        wd.find_element_by_css_selector("span.user-profile__title").click()

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

    def delete_first_address(self):
        wd = self.driver
        wd.find_element_by_css_selector("a.delete_uaddress").click()
        time.sleep(2)
        alert = wd.switch_to_alert()
        time.sleep(2)
        alert.accept()
        time.sleep(5)

    def find_new_address(self):
        wd= self.driver
        wd.find_element_by_css_selector("uaddresses-str").click()

    def find_by_address_from_home_page(self):
        wd = self.driver
        wd.find_element_by_id("user-addr__input").click()
        wd.find_element_by_id("user-addr__input").clear()
        wd.find_element_by_id("user-addr__input").send_keys("Москва, улица Александра Солженицына, 23Ас4")
        wd.find_element_by_css_selector("a.user-addr__submit.sbm-btn").click()
        time.sleep(5)

    def open_vendor_from_search(self):
        wd = self.driver
        wd.find_element_by_id("fast_search_rest_input").click()
        wd.find_element_by_id("fast_search_rest_input").send_keys("Тануки")
        time.sleep(1)
        wd.get("http://www.delivery-club.ru/srv/Tanuki/#Volgogradskij_prospjekt/Sushhjevskij_Val")
        time.sleep(2)

    def ordering_products(self):
        wd = self.driver
        wd.find_element_by_css_selector("i.quantity").click()
        wd.find_element_by_css_selector("a.inc").click()
        wd.find_element_by_css_selector("a.inc").click()
        wd.find_element_by_css_selector("a.inc").click()
        wd.find_element_by_css_selector("a.inc").click()
        wd.find_element_by_css_selector("a.done").click()
        time.sleep(3)

    def open_cart(self):
        wd = self.driver
        wd.find_element_by_xpath("//div[@id='middle']/div[3]/a[2]").click()

    def open_checkout(self):
        wd = self.driver
        wd.find_element_by_link_text("ОФОРМИТЬ ЗАКАЗ").click()
        time.sleep(3)

    def assert_balls(self):
        wd = self.driver
        wd.find_elements_by_id("user-points")

    def assert_title_profile(self):
        wd = self.driver
        wd.find_element_by_xpath("//div[@class='card_address']//h1[.='Мои адреса']")
        wd.find_element_by_css_selector("h1")

    def assert_vendor_page(self):
        wd = self.driver
        wd.find_element_by_xpath("//h2[@id='anchor_test']//b[.='Популярное']")
        wd.find_element_by_link_text("Инфо").click()
        wd.find_element_by_css_selector("h1")
        time.sleep(2)
        # wd.get("http://www.delivery-club.ru/srv/ILPatio/feedbacks/#Taganskaja/")
        wd.find_element_by_link_text("Меню").click()

    def assert_checkout(self):
        wd = self.driver
        wd.find_element_by_name("tel_number_change")


    def login(self):
        wd = self.driver
        wd.find_element_by_link_text("Вход / Регистрация").click()
        wd.find_element_by_name("c_l").click()
        wd.find_element_by_name("c_l").clear()
        wd.find_element_by_name("c_l").send_keys("w@w.com")
        wd.find_element_by_name("c_p").click()
        wd.find_element_by_name("c_p").clear()
        wd.find_element_by_name("c_p").send_keys("111111")
        wd.find_element_by_link_text("ВОЙТИ").click()
        time.sleep(2)
        self.open_profile_page()
        time.sleep(2)

    def logout(self):
        wd = self.driver
        time.sleep(3)
        wd.find_element_by_xpath("//ul[@class='user-profile__list']//span[.='Выход']").click()
        time.sleep(3)