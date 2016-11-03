from pytest_bdd import given, when, then, scenario


@scenario('../../features/frontend/auth/registration.feature',
          '[NEGATIVE] Error message when fields are empty and uncheck user agreement')
def test_user_registration():
    pass


@given("I open homepage and open registration form")
def open_home_page_open_reg_form(web_application):
    app = web_application
    app.open_homepage()
    app.open_header_menu()
    app.click_registration_link()


@when("I click on the checkbox User Agreement to uncheck it")
def remove_check_mark(web_application):
    app = web_application
    app.clear_registration_form_fields()
    app.uncheck_user_agreement_checkbox()


@when("I click on submit form button")
def submit_registration_form(web_application):
    app = web_application
    app.submit_registration_form()


@then("I see error message")
def check_error_message(web_application):
    app = web_application
    app.check_error_message()
