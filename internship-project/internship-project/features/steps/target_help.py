from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open Target help page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')
    context.driver.wait.until(EC.url_contains('help'))

@then('Verify Help page has main header')
def verify_main_header(context):
    header = context.driver.find_element(By.CSS_SELECTOR, '[class="col-sm-12 bio"]')
    assert header.is_displayed(), "Main header is not visible"

@then('Verify Help page has search input')
def verify_search_input(context):
    search_input = context.driver.find_element(By.CSS_SELECTOR, '[class="search-input"]')
    assert search_input.is_displayed(), "Search input is not visible"

@then('Verify Help page has footer section')
def verify_footer_section(context):
    footer = context.driver.find_element(By.CSS_SELECTOR, '[class="accessLinks bold"]')

    assert footer.is_displayed(), "Footer section is not visible"

@then('Verify Help page has search boxes')
def verify_search_boxes(context):
    boxes = context.driver.find_elements(By.CSS_SELECTOR, '[class*="boxSmall"]')
    expected_count = 8
    actual_count = len(boxes)
    assert actual_count == expected_count, f"Expected {expected_count} search boxes, but found {actual_count}"
