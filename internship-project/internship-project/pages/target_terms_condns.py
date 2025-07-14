from pages.base_page import Page
from selenium.webdriver.common.by import By

class TargetTermsCondns(Page):

    TARGET_TERMS_CONDNS_LINK = (By.CSS_SELECTOR, '[aria-label*="terms & conditions"]')

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_on_target_terms_and_conditions(self):
        self.click(*self.TARGET_TERMS_CONDNS_LINK)

    def verify_terms_and_conditions_page(self):
        self.wait_for_url_contains('terms-conditions')




