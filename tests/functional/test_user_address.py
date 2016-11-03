#!/usr/bin/env python3

from time import sleep
from pytest_bdd import given, when, then, scenario


@scenario('../../features/frontend/profile/address.feature',
          '[POSITIVE] Successful address addition')
def test_successful_address_addition():
    pass


@given('I open homepage and login')
def open_homepage(web_application):
    app = web_application
    app.open_homepage()
    app.user_login(email='nnn19@ro.ru', password='Pas2sW0rd3')
    app.submit_login_form()


@when('I open user profile')
def open_open_user_profile(web_application):
    app = web_application
    sleep(1)
    app.open_user_profile()


@when('enter <address> and submit the form')
def enter_address_and_submit(web_application, address, g):
    app = web_application

    # Write addresses count to global variable
    g['old_addresses'] = len(app.get_current_addresses())
    app.enter_address(address=address)
    app.submit_address_form()


@then('I check that address has been added')
def validate_address_addition(web_application, g):
    app = web_application
    sleep(2)
    g['new_addresses'] = len(app.get_current_addresses())

    assert g['new_addresses'] == g['old_addresses'] + 1
