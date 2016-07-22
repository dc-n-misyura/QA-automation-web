from pytest_bdd import given, when, then

@given('I navigate to the DC Home page and login')
#  Открытие страницы логин, проверка профиля и обратно на главную
def open_home_page(app, new_address):
    app.open_home_page()
    app.login()
    app.assert_title_profile()
    app.open_home_page()
    app.assert_balls()

@when('I input in search "<new_address>"')
#  Ввожу адрес из Exapmple {new_address} и попадаю в выдачу
def search_vendor(app, new_address):
    app.find_by_address_from_home_page(new_address)

@when('Search and open "<vendor_title>"')
#  Ищу необходимый ресторан через поиск
def find_by_address_from_home_page(app,vendor_title):
    app.open_vendor_from_search(vendor_title)

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

@given('Open home-page and open registration form')
#Открываем главную страницу, далее открываем форму регистрации
def open_registration_form(app):
    app.open_home_page()
    app.open_registration_form()

@when('Input all required fields "<username>", "<phone>", "<password>"')
#Вводим все обязательные поля
def input_required_fields(app,username,phone, password):
    app.input_required_fields(username,phone, password)

@then('I press submit button and see homepage authorized user')
# Нажимаем кнопку зарегистрироваться и видим главную страницу авторизованного пользователя
def submit_and_check_results_registration(app):
    app.submit_and_check_results_registration()
    app.assert_balls()

@when('Click to heart')
def click_by_favorite_hearth(app):
    app.click_by_favorite_hearth()

@when('Open favorite-vendor list')
def open_favorite_list(app):
    app.open_favorite_list()

@then('I see this vendor')
def found_favorite_vendor_in_list(app):
    app.found_favorite_vendor_in_list()