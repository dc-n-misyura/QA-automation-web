#!/usr/bin/env python3
"""
TODO: docstring
"""
from selenium.webdriver.common.by import By


class HomepageLocators:

    # Locators for login form
    LOGIN_REGISTER_FORM = (By.LINK_TEXT, 'Вход / Регистрация')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-panel__enter-btn')
    LOGIN_EMAIL_FIELD = (By.NAME, 'c_l')
    LOGIN_PASSWORD_FIELD = (By.NAME, 'c_p')

    # Locators for registration form
    REG_LINK = (By.XPATH, '//*[contains(@class, "fast_register fast-register__link")]')
    REG_NAME_FIELD = (By.CSS_SELECTOR, '.form-register__input-name')
    REG_PHONE_FIELD = (By.CSS_SELECTOR, '.form-register__input-phone')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '.form-register__input-email')
    REG_PASS_FIELD = (By.CSS_SELECTOR, '.form-register__input-password')
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.submit-register-form')
    REG_AGREEMENT_CHECKBOX = (By.CSS_SELECTOR,
                              '.form-register__input-agreement')

    # Locators for logged-in user
    LOGGED_USERNAME_TEXT = (By.CSS_SELECTOR, '.user-profile__span')

    # TODO: rename this const and mark it as for new frontend only
    LOGGED_USERNAME_HEADER = (By.CSS_SELECTOR, '.header-home__user-name')
    LOGGED_PROFILE_LINK = (By.CSS_SELECTOR, '.user-profile__a')

    # Locators for error message at register form
    TOOLTIP_ERROR_REGISTER_TEXT = (By.CSS_SELECTOR, '.tooltip-error__mess')
    TOP_PANEL_MASKED_PHONE_FIELD = (By.CSS_SELECTOR, '.top-panel__input masked_phone form-register__input-phone has-error not-valid')

