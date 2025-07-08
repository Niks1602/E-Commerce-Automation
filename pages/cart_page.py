CHECKOUT_BUTTON = "button[data-test='checkout']"


class CartPage:
    def __init__(self, page):
        self.page = page

    def proceed_to_checkout(self):
        self.page.click(CHECKOUT_BUTTON)
