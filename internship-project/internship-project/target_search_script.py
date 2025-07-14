from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.ID,'search').send_keys('icecream')
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

expected_text = 'icecream'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
assert expected_text in actual_text, f"Error, expected {expected_text} not in actual {actual_text}"
print('test case passed')


