from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@when('user adds product "{product_name}" to the cart')
def step_add_product(context, product_name):
    context.products_page = ProductsPage(context.page)
    context.products_page.add_product_to_cart(product_name)


@then("cart icon should show 1 item")
def step_verify_cart_icon(context):
    count = context.products_page.get_cart_count()
    assert count == "1", f"Expected 1 item in cart, but found {count}"
