from pytest_bdd import given, when, then, scenario
from fixture.session import SessionHelper
from fixture.application import *

@given('I navigate to the DC Home page and login')
#  Открытие страницы логин, проверка профиля и обратно на главную
def open_home_page(app):
    app.open_home_page()
    app.login()
    app.assert_title_profile()
    app.open_home_page()
    app.assert_balls()

@when('I input in search new address')
#  Ввожу адрес и попадаю в выдачу
def search_vendor(app):
    app.find_by_address_from_home_page()

@when('Search and open vendor')
#  Ищу необходимый ресторан через поиск
def find_by_address_from_home_page(app):
    app.open_vendor_from_search()

@when('Check vendor page')
# Проверяю корректность страницы ресторана
def check_vendor_page(app):
    app.assert_vendor_page()

@when('I make order')
#  Формирую заказ больше минимальной суммы
def make_order(app):
    app.ordering_products()

@when('Open cart and checkout')
#  Проходим экран корзины и чекаута
def pass_the_cart_and_checkout(app):
    app.open_cart()
    app.open_checkout()

@then('I have cart with order, phone and address')
# Открываем чекаут где сформирован заказ, с введённым адрессом, телефоном, - готовый к отправке
def check_user_data_in_checkout(app):
    app.assert_checkout()
