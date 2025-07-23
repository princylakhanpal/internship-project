from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ReellyProject(Page):

    EMAIL_ID = (By.ID, "email-2")
    PASSWORD = (By.CSS_SELECTOR, '[data-name="Password"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[wized="loginButton"]')
    VERIFICATION_OPTION = (By.CSS_SELECTOR, '[href*="/verification"]')
    SETTINGS_MENU = (By.XPATH, '//div[@class="g-menu-text" and text()="Settings"]')
    BLOCK_TXT = (By.CSS_SELECTOR, ".step-1-block")

    def open_main_page (self):
        self.driver.get('https://soft.reelly.io')

    def input_email(self, email):
        self.input_text(email, *self.EMAIL_ID)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD)

    def click_continue_button(self):
        self.click(*self.CONTINUE_BTN)

    def click_settings_menu(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SETTINGS_MENU)
        )

        element = self.driver.find_element(*self.SETTINGS_MENU)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS_MENU)
        )

        element.click()
        sleep(3)

    def click_verification_option(self):
        self.click(*self.VERIFICATION_OPTION)
        sleep(3)

    def verify_upload_your_photo_page(self):
        self.verify_partial_text("Upload your photo", *self.BLOCK_TXT)



