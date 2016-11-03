#!/usr/bin/env python3
"""
TODO: docstring
"""

from selenium.webdriver import Chrome
from core.pages.homepage import Homepage
from core.pages.profile import ProfilePage


class Application:
    def __init__(self):
        self.driver = Chrome('/usr/local/bin/chromedriver')
        self._max_window()
        self.driver.implicitly_wait(10)

        self.homepage = Homepage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def _max_window(self):
        self.driver.maximize_window()

    # Navigation method
    def open_homepage(self):
        base_url = 'http://www.delivery-club.ru'
        self.driver.get(base_url)

    # Base method
    def open_header_menu(self):
        self.homepage.login_register_form.click()

    # Method about user auth
    def click_registration_link(self):
        self.homepage.register_link.click()

    # Method about user auth
    def user_login(self, email, password):
        # TODO: remove this method and look at tests
        self.open_header_menu()
        self.homepage.login_email_field.enter_text(email)
        self.homepage.login_password_field.enter_text(password)

    # Method about user registration
    def fill_registration_form(self, name, phone, email, password):
        self.homepage.reg_name_field.enter_text(name)
        self.homepage.reg_phone_field.enter_text(phone)
        self.homepage.reg_email_field.enter_text(email)
        self.homepage.reg_pass_field.enter_text(password)

    def submit_registration_form(self):
        self.homepage.reg_submit_button.click()

    # Method about user registration (validation)
    def ensure_user_logged_in(self, frontend='old'):
        if frontend == 'old':
            return self.homepage.logged_username_text
        elif frontend == 'new':
            return self.homepage.logged_username_header

    def open_user_profile(self):
        self.homepage.logged_username_text.click()
        self.homepage.logged_profile_link.click()

    def enter_address(self, address):
        self.profile_page.address_field.enter_text(address)

    def submit_address_form(self):
        self.profile_page.add_address_button.click()

    def get_current_addresses(self):
            return self.profile_page.address_list.find_all()

    def quit(self):
        self.driver.quit()

    def submit_login_form(self):
        self.homepage.login_button.click()

    # Click and clear all registration fields
    def clear_registration_form_fields(self):
        self.homepage.reg_name_field.click()
        self.homepage.reg_name_field.clear()
        self.homepage.reg_phone_field.click()
        self.homepage.reg_phone_field.clear()
        self.homepage.reg_email_field.click()
        self.homepage.reg_pass_field.click()
        self.homepage.reg_pass_field.clear()

    # Click on user agreement checkbox
    def uncheck_user_agreement_checkbox(self):
        self.homepage.reg_agreement_checkbox.click()

    def check_error_message(self):
        self.homepage.tooltip_error_register_text.click()

    def check_red_field_phone(self):
        self.homepage.top_panel_masked_phone_field.find_all()
