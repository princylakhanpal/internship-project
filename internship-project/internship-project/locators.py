
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH,'//*[@class="a-button-text"]').click()
driver.find_element(By.XPATH, '//div[@id="nav-link-accountList"]').click()
sleep(5)

#Locators + Search strategy for Amazon Sign in page

#Amazon logo, search by XPATH
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

#Email field,search by ID
driver.find_element(By.ID,"ap_email_login")

#Continue button,search by XPATH
driver.find_element(By.XPATH,"//input[@class='a-button-input']")

#Conditions of use link,search by text
driver.find_element(By.XPATH,"//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

#Privacy notice link,search by text
driver.find_element(By.XPATH,"//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

#Need help link,search by XPATH
driver.find_element(By.XPATH,"//a[contains(@href, '/gp/help/customer/account')]")

#Create account page link,search by text
driver.find_element(By.XPATH,"//a[@id='ab-registration-ingress-link']")










