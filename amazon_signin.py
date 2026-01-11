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
driver.get('https://www.amazon.com/gp/sign-in.html')
sleep(3)

# Locators: Amazon logo
# By XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Locators: Email field
# By ID
driver.find_element(By.ID, "ap_email_login")

# Locators: Continue button
# By XPATH
driver.find_element(By.XPATH, "//input[@type='submit']")
sleep(1)

# Locators: Conditions of use link
# By XPATH
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Locators: Privacy Notice link
# By XPATH
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Locators: Need help link
# By XPATH (parent/child)
driver.find_element(By.XPATH, "//a//span")
sleep(1)

# Locators:  Forgot your password link
# By XPATH (parent/child)
driver.find_element(By.XPATH, "//ul//a")
sleep(1)

# Locators:  Other issues with Sign-In link
# By XPATH
driver.find_element(By.XPATH, "//span//a")
sleep(1)

# Locators:  Create your Amazon account button
# By XPATH
driver.find_element(By.XPATH, "//span[.//a]")
sleep(1)

