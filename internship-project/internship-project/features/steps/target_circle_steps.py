from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify page has {number} cells')
def verify_benefit_cells(context, number):
    print(type(number))
    cells = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')

    print(cells)

    assert len(cells) == int(number), f'Expected {number} cells but got {len(cells)}'