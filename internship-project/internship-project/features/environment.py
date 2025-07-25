import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    options = ChromeOptions()
    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user ='princylakhanpal_jS1l5x'
    # bs_key ='Gyf8WsgqwyPpvyx4jwrD'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = ChromeOptions()
    # bstack_options = {
    #    "os" : "OS X",
    #   "osVersion" : "Monterey",
    #   'browserName': 'Chrome',
    #   'sessionName': scenario_name,
    #   "browserVersion": "latest",
    #  }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=options)
    #options = FirefoxOptions()
    #options.headless = False
    #"""Initialize headless Chrome browser."""
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--window-size=1920,1080")

    #service = FirefoxService(GeckoDriverManager().install())
    #context.driver = webdriver.Firefox(service=service, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 20)
    context.app = Application(context.driver)
    #print("Headless mode: YES")
    #print("Window size:", context.driver.get_window_size())


def before_scenario(context, scenario):
  print('\nStarted scenario: ', scenario.name)
  browser_init(context, scenario.name)


def before_step(context, step):
  print('\nStarted step: ', step)


def after_step(context, step):
  if step.status == 'failed':
      print('\nStep failed: ', step)


def after_scenario(context, scenario):
  context.driver.quit()
