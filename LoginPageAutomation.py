from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com")  # Website

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Form Authentication"))
)

link = driver.find_element(By.LINK_TEXT, "Form Authentication")
link.click()

user_input = driver.find_element(By.ID, "username")
user_input.clear()
user_input.send_keys("tomsmith")

password_input = driver.find_element(By.ID, "password")
password_input.clear()
password_input.send_keys("SuperSecretPassword!" + Keys.ENTER)

time.sleep(20)
driver.quit()
