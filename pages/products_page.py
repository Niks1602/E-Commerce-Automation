CART_ICON = ".shopping_cart_badge"
CART_LINK = ".shopping_cart_link"


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_badge")

    def add_product_to_cart(self, product_name: str):
        # Construct selector using product name
        product_locator = f'div.inventory_item:has-text("{product_name}")'
        add_button = self.page.locator(f'{product_locator} button:has-text("Add to cart")')
        add_button.click()

    def get_cart_count(self) -> str:
        if self.cart_icon.is_visible():
            return self.cart_icon.text_content()
        return "0"

    def go_to_cart(self):
        self.page.click('.shopping_cart_link')
