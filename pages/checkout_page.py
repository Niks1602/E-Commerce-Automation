FIRST_NAME_INPUT = "input[data-test='firstName']"
LAST_NAME_INPUT = "input[data-test='lastName']"
ZIP_CODE_INPUT = "input[data-test='postalCode']"
CONTINUE_BUTTON = "input[data-test='continue']"
FINISH_BUTTON = "button[data-test='finish']"


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def enter_shipping_info(self, first_name, last_name, zip_code):
        self.page.fill(FIRST_NAME_INPUT, first_name)
        self.page.fill(LAST_NAME_INPUT, last_name)
        self.page.fill(ZIP_CODE_INPUT, zip_code)
        self.page.click(CONTINUE_BUTTON)

    def finish_checkout(self):
        self.page.click(FINISH_BUTTON)
