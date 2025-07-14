from selenium.webdriver.common.by import By
from pages.base_page import Page



class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TXT)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def get_product_name(self):
        return self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text

