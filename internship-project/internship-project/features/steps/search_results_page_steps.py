from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@when('Click on Add to cart button')
def click_add_to_cart(context):
    #context.driver.find_element(*ADD_TO_CART_BTN).click()
    #context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))
    context.app.search_results_page.click_add_to_cart()

@when('Store product name')
def get_product_name(context):
    #context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    #print('Product name stored: ', context.product_name)
    context.product_name = context.app.search_results_page.get_product_name()
    context.app.search_results_page.get_product_name()

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()

@then('Verify search worked for {product}')
def verify_search_results(context, product):
   # actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    #assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"
    context.app.search_results_page.verify_search_results(product)
