from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in(context):
    context.app.target_terms_condns.open_sign_in_page()
    sleep(5)


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_terms_condns.get_current_window_id()

@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions(context):
    context.app.target_terms_condns.click_on_target_terms_and_conditions()

@when('Switch to the newly opened window')
def switch_window(context):
    context.app.target_terms_condns.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.target_terms_condns.verify_terms_and_conditions_page()

@then('Close new window')
def close_new_window(context):
    context.app.base_page.close_window()

@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)

