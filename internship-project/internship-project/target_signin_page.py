from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(7)

driver.get('https://www.target.com/')
driver.find_element(By.XPATH, '//a[@data-test="@web/AccountLink"]').click()
driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()


expected = 'Sign in or create account'
actual = driver.find_element(By.XPATH, '//h1[contains(@class, "styles_ndsHeading")]').text
