from selenium.webdriver.common.by import By
from behave import given, when, then


HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
USER_ACCOUNT_TXT = (By.CSS_SELECTOR, '[aria-label*="Hi,"]')

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product(search_word)

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@when('Click on Account')
def click_account_button(context):
   # context.driver.wait.until(EC.element_to_be_clickable(ACCOUNT_BTN)).click()
     context.app.header.click_account_button()


@when('Click Sign in button')
def click_sign_in_button(context):
    #context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()
     context.app.header.click_sign_in_button()

@when('Input "{email}" in Email field')
def input_email(context, email):
    context.app.header.input_email(email)

@when('Click Continue button')
def click_continue_button(context):
    context.app.header.click_continue_button()

@when('Input "{password}" in Password field')
def input_password(context, password):
    context.app.header.input_password(password)

@when('Click Sign in with Password button')
def click_sign_in_with_password_button(context):
    context.app.header.click_sign_in_with_password_button()

@then('Verify User is logged in')
def verify_user_is_logged_in(context):
    context.app.header.verify_user_is_logged_in()

@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")

    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)

