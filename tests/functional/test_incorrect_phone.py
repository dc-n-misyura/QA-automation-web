from pytest_bdd import given, when, then, scenario

@scenario('../../features/frontend/auth/registration.feature',
          '[NEGATIVE] Incorrect format phone number')
def test_incorrect_phone():
    pass

@given('Open home-page and open registration form')
def open_homepage_open_registration_form(web_application):
    app = web_application
    app.open_homepage()
    app.open_header_menu()
    app.click_registration_link()

@when('I input <name>, <incorrectphone>, <email>, <password>')
def fill_registration_fields(web_application, name, incorrectphone, email, password):
    app = web_application
    app.fill_registration_form(name, incorrectphone, email, password)

@then('I press submit button and see all error-message')
def check_error_message(web_application):
    app = web_application
    app.submit_registration_form()
    app.check_error_message()

@then('I see red phone field')
def check_red_phone_field(web_application):
    app = web_application
    app.check_red_field_phone()

