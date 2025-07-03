from behave import given, when, then
from pages.login_page import LoginPage


@given("user opens the login page")
def step_open_login(context):
    context.page.goto("https://www.saucedemo.com")


@when('user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page = LoginPage(context.page)
    context.login_page.login(username, password)


@then("user should land on the products page")
def step_verify_login(context):
    assert context.page.url.endswith("/inventory.html")


@then('user should see an error message "{expected_error}"')
def step_verify_error(context, expected_error):
    error_message = context.login_page.get_error_message()
    assert error_message == expected_error
