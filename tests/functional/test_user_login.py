#!/usr/bin/env python3
from time import sleep

from pytest_bdd import given, when, then, scenario


@scenario('../../features/frontend/auth/login.feature',
          '[POSITIVE] Successful login')
def test_user_login():
    pass


@given('I open homepage')
def open_homepage(web_application):
    app = web_application
    app.open_homepage()


@given('open header menu and click on login-registration link')
def open_login_form(web_application):
    app = web_application
    app.open_header_menu()


@when('I fill <email>, <password> and submit the form')
def fill_login_form(web_application, email, password):
    app = web_application
    app.user_login(email, password)
    app.submit_login_form()


@then('login was successful, check <name>')
def validate_user_registration(web_application, name):
    app = web_application
    sleep(1)
    assert name in app.ensure_user_logged_in(frontend='new').text
