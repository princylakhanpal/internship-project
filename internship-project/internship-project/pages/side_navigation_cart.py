from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideNavigationCart(Page):
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def side_nav_click_add_to_cart(self):
    #context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()
        self.click(*self.SIDE_NAV_PRODUCT_NAME)
