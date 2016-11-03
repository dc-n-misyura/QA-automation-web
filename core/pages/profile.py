#!/usr/bin/env python3
"""
TODO: docstring
"""
from core.elements import Element
from core.locators.profile import ProfileLocators as Profile


class ProfilePage:
    """
    Docstring
    """

    def __init__(self, driver):
        self.driver = driver
        self.address_field = Element(self.driver, *Profile.ADDRESS_FIELD)
        self.add_address_button = Element(self.driver,
                                          *Profile.ADD_ADDRESS_BUTTON)
        self.address_list = Element(self.driver, *Profile.ADDRESS_LIST)
