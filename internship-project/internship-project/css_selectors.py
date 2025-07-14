
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#CSS Selectors
#Amazon Logo, by class
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#Create Account, by tag + class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Enter mobile number or email, by tag + id
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

#Your name, by id
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name_context_message_section')

#Password, by id
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Re-enter password, by id
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Continue button, by class
driver.find_element(By.CSS_SELECTOR, '.a-button-input')

#Conditions of Use, by attribute partial match
driver.find_element(By.CSS_SELECTOR, '[href*="ap_register_notification_condition_of_use?"]')

#Privacy notice, by attribute partial match
driver.find_element(By.CSS_SELECTOR, '[href*="ap_register_notification_privacy_notice"]')

#Sign in instead, by id
driver.find_element(By.CSS_SELECTOR, '#ra-sign-in-link')



