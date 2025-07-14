from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify Sign in page opened')
def verify_sign_in_page_open(context):
    #actual_text = context.driver.find_element(By.CSS_SELECTOR, '[class*="styles_ndsHeading"]').text
    #assert 'Sign in or create account' in actual_text, f"Error, expected 'Sign in or create account' in actual {actual_text}"
    context.app.sign_in_page.verify_sign_in_page_open()