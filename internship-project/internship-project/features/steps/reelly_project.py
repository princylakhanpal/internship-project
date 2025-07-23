from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.reelly_project.open_main_page()
    sleep(5)

@when('Enter {email} into email')
def input_email(context, email):
    context.app.reelly_project.input_email(email)

@when('Enter {password} into password')
def input_password(context, password):
    context.app.reelly_project.input_password(password)

@when('Click continue button')
def click_continue_button(context):
    context.app.reelly_project.click_continue_button()
    sleep(5)

@when('Click on settings at the left side menu')
def click_settings_menu(context):
    context.app.reelly_project.click_settings_menu()

@when('Click on the verification option')
def click_verification_option(context):
    context.app.reelly_project.click_verification_option()

@then('Verify the right page opens')
def verify_verification_page(context):
    context.app.reelly_project.verify_upload_your_photo_page()