
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    ACCOUNT_BTN = (By.CSS_SELECTOR, '[id="account-sign-in"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[inputmode="email"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[id="login"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-test="login-password"]')
    PASSWORD_BTN = (By.CSS_SELECTOR, '[type="submit"]')
    USER_ACCOUNT_TXT = (By.XPATH, '//span[contains(text(), "Hi,")]')


    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep((10))

    def click_cart(self):
        #self.click(*self.CART_ICON)
        self.wait_for_element_click(*self.CART_ICON)

    def click_account_button(self):
        self.click(*self.ACCOUNT_BTN)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def input_email(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def click_continue_button(self):
        self.click(*self.CONTINUE_BTN)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_sign_in_with_password_button(self):
        self.click(*self.PASSWORD_BTN)

    def verify_user_is_logged_in(self):
        element = self.wait_for_element(*self.USER_ACCOUNT_TXT)
        text = element.text
        assert "Hi" in text, f"Expected 'Hi ' in user greeting, but got: '{text}'"



