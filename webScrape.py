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

PATH = '/mnt/chromeos/MyFiles/Downloads/chromedriver_linux64'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "/usr/share/bash-completion/completions/google-chrome"  # Set the binary location
# chrome_options.add_argument("--headless")  # Add any desired arguments
USERNAME = input("Enter the username: ")
PASSWORD = getpass.getpass(prompt="Enter the password: ")
passwordLen = len(PASSWORD)
print(PATH)
print(USERNAME)
i=0
password = []
while i < passwordLen:
    password.append('*')
    i+=1
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