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
driver.get('https://www.target.com/')
sleep(5)

# click account button
driver.find_element(By.ID, "account-sign-in").click()
sleep(15)

# click Sign-in button from side navigation
driver.find_element(By.XPATH, "//button[@type='button' and @data-test='accountNav-signIn']").click()
sleep(15)

# verify Sign-in page opened & “Sign in or create account” text is shown
expected_text = 'create account'
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class,'styles_ndsHeading')]").text
print(actual_text)

assert expected_text in actual_text, f'Expected Text {expected_text} not in actual text {actual_text}'
print('Test case Passed')
sleep(5)

# Sign-in button is shown 
driver.find_element(By.ID, "login")

# quit page
sleep(10)
driver.quit()