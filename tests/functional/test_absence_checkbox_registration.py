from pytest_bdd import given, when, then, scenario


@scenario('../../features/frontend/auth/registration.feature',
          '[NEGATIVE] The absence checkbox of the user agreement')
def test_absence_checkbox_registration():
    pass


@given('I open homepage and open registration form')
def open_home_page_open_reg_form(web_application):
    app = web_application
    app.open_homepage()
    app.open_header_menu()
    app.click_registration_link()


@when('I input <name>, <phone>, <mail>, <password>')
def fill_registration_fields(web_application, name, phone, mail, password):
    app = web_application
    app.fill_registration_form(name, phone, mail, password)


@when('I click on the checkbox User Agreement to uncheck it')
def click_checkbox(web_application):
    app = web_application
    app.uncheck_user_agreement_checkbox()


@when('I click on submit form button')
def click_submit_button(web_application):
    app = web_application
    app.submit_registration_form()


@then('I see error message')
def check_message(web_application):
    app = web_application
    app.check_error_message()
    # TODO: add assert here
