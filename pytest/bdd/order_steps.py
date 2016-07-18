from pytest_bdd import given, when, then
from fixture.session import SessionHelper
from fixture.application import *

@given('I navigate to the DC Home page')
def open_home_page(app):
    app.open_home_page()

@when('I login')
def login(app):
    app.login()
    pass

@then('I see profile screen')
def open_profile_page(app):
    # app.assert_title_profile()
    pass
@given('I input in search new address')
def find_by_address_from_home_page(app):
    app.find_by_address_from_home_page(new_address="Москва, улица Александра Солженицына, 23Ас4")