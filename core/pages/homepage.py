#!/usr/bin/env python3
"""
TODO: docstring
"""
from core.elements import Element
from core.locators.homepage import HomepageLocators as Home


class Homepage:
    """
    Docstring
    """

    def __init__(self, driver):
        self.driver = driver
        self.login_register_form = Element(self.driver,
                                           *Home.LOGIN_REGISTER_FORM)
        self.login_email_field = Element(self.driver, *Home.LOGIN_EMAIL_FIELD)
        self.login_password_field = Element(self.driver,
                                            *Home.LOGIN_PASSWORD_FIELD)
        self.login_button = Element(self.driver, *Home.LOGIN_BUTTON)
        self.register_link = Element(self.driver, *Home.REG_LINK)
        self.reg_name_field = Element(self.driver, *Home.REG_NAME_FIELD)
        self.reg_phone_field = Element(self.driver, *Home.REG_PHONE_FIELD)
        self.reg_email_field = Element(self.driver, *Home.REG_EMAIL_FIELD)
        self.reg_pass_field = Element(self.driver, *Home.REG_PASS_FIELD)
        self.reg_submit_button = Element(self.driver, *Home.REG_SUBMIT_BUTTON)

        self.reg_agreement_checkbox = Element(self.driver,
                                              *Home.REG_AGREEMENT_CHECKBOX)
        self.logged_username_text = Element(self.driver,
                                            *Home.LOGGED_USERNAME_TEXT)
        self.logged_username_header = Element(self.driver,
                                              *Home.LOGGED_USERNAME_HEADER)
        self.logged_profile_link = Element(self.driver,
                                           *Home.LOGGED_PROFILE_LINK)
        self.tooltip_error_register_text = Element(self.driver,
                                                   *Home.TOOLTIP_ERROR_REGISTER_TEXT)
        self.top_panel_masked_phone_field = Element(self.driver,
                                                    *Home.TOP_PANEL_MASKED_PHONE_FIELD)

    # def get_element_by_name(self, element):
    #     return Element(self.driver, element)
