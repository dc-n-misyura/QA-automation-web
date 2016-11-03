#!/usr/bin/env python3
from time import sleep

from pytest_bdd import given, when, then, scenario


@scenario('../../features/frontend/auth/registration.feature',
          '[POSITIVE] Successful registration')
def test_user_registration():
    pass


@given('I open homepage')
def open_homepage(web_application):
    app = web_application
    app.open_homepage()


@given('open header menu and click on registration link')
def open_registration_form(web_application):
    app = web_application
    sleep(1)
    app.open_header_menu()
    app.click_registration_link()


@when('I fill <name>, <phone>, email, <password> and submit the form')
def fill_registration_form(web_application, name, phone, random_email, password):
    app = web_application
    app.fill_registration_form(name, phone, random_email, password)
    app.submit_registration_form()


@then('registration was successful with <name>')
def validate_user_registration(web_application, name):
    app = web_application

    # TODO: replace sleep with selenium wait
    sleep(1)

    s = app.ensure_user_logged_in(frontend='old').text
    expected_name = ''.join(s.split()[0])

    assert name in expected_name

