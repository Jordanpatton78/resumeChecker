from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
import getpass

# PATH = '/mnt/chromeos/MyFiles/Downloads/chromedriver_linux64'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "/usr/share/bash-completion/completions/google-chrome"  # Set the binary location
# chrome_options.add_argument("--headless")  # Add any desired arguments
USERNAME = input("Enter the username: ")
PASSWORD = getpass.getpass(prompt="Enter the password: ")
COMPANY = input("What company do you want to check?  ").lower()
POSITION = input("WHat position at that company? ")
passwordLen = len(PASSWORD)
# print(PATH)
print(USERNAME)
i=0
password = []
for letter in PASSWORD:
    password.append('*')
password = "".join(password)
print(password)

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/uas/login")
time.sleep(3)

email=driver.find_element(By.ID, "username")
email.send_keys(USERNAME)
password=driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)

time.sleep(5)
search = driver.find_element(By.CLASS_NAME,"search-global-typeahead__input")
search.click()
search.send_keys(COMPANY)
search.send_keys(Keys.RETURN)
time.sleep(5)

companyLink = driver.find_element(By.CSS_SELECTOR, f"a[href*='https://www.linkedin.com/company/{COMPANY}/']")
companyLink.click()
time.sleep(5)

peopleLink = driver.find_element(By.CSS_SELECTOR, f"a[href*='/company/{COMPANY}/people/']")
peopleLink.click()
time.sleep(3)

searchEmployees = driver.find_element(By.ID, "people-search-keywords")
searchEmployees.send_keys(POSITION)
searchEmployees.send_keys(Keys.RETURN)
time.sleep(3)

employee = driver.find_element(By.CLASS_NAME, "org-people-profile-card__profile-info")
employee.click()
time.sleep(3)

expUL = driver.find_element(By.CLASS_NAME, '''pvs-list
            
            
            ''')
expLI = expUL.find_element(By.TAG_NAME, "li")
print(expLI.text)

driver.quit()