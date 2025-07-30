from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ReellyProject(Page):

    EMAIL_ID = (By.ID, "email-2")
    PASSWORD = (By.CSS_SELECTOR, '[data-name="Password"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[wized="loginButton"]')
    VERIFICATION_OPTION = (By.CSS_SELECTOR, '[href="/verification/step-0"]')
    HAMBURGER_MENU = (By.CSS_SELECTOR, "a.new-market-menu-button")
    BLOCK_TXT = (By.CSS_SELECTOR, ".step-1-block")
    PAGE_LOADED_MARKER = (By.CSS_SELECTOR, '[class*="w-layout"]')

    def open_main_page (self):
        self.driver.get('https://soft.reelly.io')
        sleep(5)
        print("Page URL:", self.driver.current_url)
        print("Page title:", self.driver.title)

        page_source = self.driver.page_source
        if 'id="email-2"' in page_source:
            print("Email input found in page source")
        else:
            print("Email input NOT found in page source")

        self.driver.save_screenshot("input_email_debug.png")

    def input_email(self, email):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_ID)
        )
        self.input_text(email, *self.EMAIL_ID)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD)

    def click_continue_button(self):
        self.click(*self.CONTINUE_BTN)

    def click_hamburger_menu(self):
        sleep(7)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.HAMBURGER_MENU)
        )
        self.click(*self.HAMBURGER_MENU)


    def click_verification_option(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.VERIFICATION_OPTION)
        )

        element = self.driver.find_element(*self.VERIFICATION_OPTION)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VERIFICATION_OPTION)
        )

        element.click()

    def verify_upload_your_photo_page(self):
        self.verify_partial_text("Upload your photo", *self.BLOCK_TXT)



