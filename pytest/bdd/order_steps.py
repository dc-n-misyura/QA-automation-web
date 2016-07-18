from pytest_bdd import given, when, then
from fixture.session import SessionHelper
from fixture.application import *

@given('I navigate to the DC Home page and login')
def open_home_page(app):
    app.open_home_page()
    app.login()
    app.assert_title_profile()
    app.open_home_page()
    app.assert_balls()

@when('I input in search new address, search vendor, open him, and make order')
def find_by_address_from_home_page(app):
    app.find_by_address_from_home_page()
    app.open_vendor_from_search()
    app.assert_vendor_page()
    app.ordering_products()

@then('I have cart with order, phone and address')
def make_order_open_cart_and_open_checkout(app):
    app.open_cart()
    app.open_checkout()
    app.assert_checkout()