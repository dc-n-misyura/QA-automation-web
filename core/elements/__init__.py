#!/usr/bin/env python3
"""
TODO: docstring
"""


class Element:
    """
    Docstring
    """
    def __init__(self, driver, *locator):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.driver.find_element(*self.locator).click()

    def enter_text(self, text):
        self.driver.find_element(*self.locator).send_keys(text)

    def clear(self):
        self.driver.find_element(*self.locator).clear()

    def find_all(self):
        return self.driver.find_elements(*self.locator)

    @property
    def text(self):
        return self.driver.find_element(*self.locator).text
