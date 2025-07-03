from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from login_steps import step_open_login


@given("user is logged into the e-commerce site")
def step_login(context):
    step_open_login(context)
    context.login_page = LoginPage(context.page)
    context.login_page.login("standard_user", "secret_sauce")
    context.products_page = ProductsPage(context.page)


@when('user adds "{product_name}" to the cart')
def step_add_to_cart(context, product_name):
    context.products_page.add_product_to_cart(product_name)


@when("user proceeds to the cart")
def step_go_to_cart(context):
    context.products_page.go_to_cart()
    context.cart_page = CartPage(context.page)


@when("user clicks on checkout")
def step_click_checkout(context):
    context.cart_page.proceed_to_checkout()
    context.checkout_page = CheckoutPage(context.page)


@when('user fills shipping info with "{first}", "{last}", "{zip}"')
def step_enter_shipping(context, first, last, zip):
    context.checkout_page.enter_shipping_info(first, last, zip)


@when("user completes the checkout")
def step_complete_checkout(context):
    context.checkout_page.finish_checkout()


@then("order confirmation page should be displayed")
def step_confirm(context):
    assert context.page.locator(".complete-header").text_content() == "Thank you for your order!"
