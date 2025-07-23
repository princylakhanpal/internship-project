from pages.base_page import Page
from selenium.webdriver.common.by import By


class ReellyProject(Page):

    EMAIL_ID = (By.ID, "email-2")
    PASSWORD = (By.CSS_SELECTOR, '[data-name="Password"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[wized="loginButton"]')
    VERIFICATION_OPTION = (By.CSS_SELECTOR, '[href*="/verification"]')
    SETTINGS_MENU = (By.CSS_SELECTOR, '[class="g-menu-text"]')
    BLOCK_TXT = (By.CSS_SELECTOR, '[class="step-1-block"]')

    def open_main_page (self):
        self.driver.get('https://soft.reelly.io')

    def input_email(self, email):
        self.input_text(email, *self.EMAIL_ID)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD)

    def click_continue_button(self):
        self.click(*self.CONTINUE_BTN)

    def click_settings_menu(self):
         self.click(*self.SETTINGS_MENU)

    def click_verification_option(self):
        self.click(*self.VERIFICATION_OPTION)

    def verify_upload_your_photo_page(self):
        self.verify_partial_text("Upload your photo", *self.BLOCK_TXT)



