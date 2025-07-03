from features.locators.login_page_locators import *


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator(USERNAME_INPUT)  # Username input locator
        self.password_input = page.locator(PASSWORD_INPUT)  # Password input locator
        self.login_button = page.locator(LOGIN_BUTTON)  # Login button locator
        self.error_message = page.locator(ERROR_MESSAGE)  # Error message locator

    def login(self, username: str, password: str):
        self.username_input.fill(username)  # Fill username
        self.password_input.fill(password)  # Fill password
        self.login_button.click()  # Click login button

    def get_error_message(self) -> str:
        """Return error message if login fails"""
        if self.error_message.is_visible():
            return self.error_message.text_content()
        return ""
