#!/usr/bin/env python3
"""
TODO: docstring
"""
from selenium.webdriver.common.by import By


class ProfileLocators:

    # Locators for profile page
    ADDRESS_FIELD = (By.CSS_SELECTOR, '.user-addr__input__type1')
    ADD_ADDRESS_BUTTON = (By.CSS_SELECTOR, '.user-addr__submit')
    ADDRESS_LIST = (By.CSS_SELECTOR, '.addresses')
