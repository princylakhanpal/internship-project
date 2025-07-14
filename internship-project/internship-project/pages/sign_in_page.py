from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    sign_in_Page = (By.CSS_SELECTOR, '[class*="styles_ndsHeading"]')

    def verify_sign_in_page_open(self):
        self.verify_text('Sign in or create account', *self.sign_in_Page)