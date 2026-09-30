from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php');
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 10)

username = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
username.send_keys("kalpana")

time.sleep(3)
email = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
email.send_keys('Kalpana@gmail.com')
time.sleep(3)
mobile= wait.until(EC.visibility_of_element_located((By.NAME, 'mobile')))
mobile.send_keys('9876556445')
time.sleep(3)
dob = wait.until(EC.visibility_of_element_located((By.NAME, 'dob')))
dob.send_keys('10-10-2012')
time.sleep(3)
subject= wait.until(EC.visibility_of_element_located((By.NAME, 'subjects')))
subject.send_keys('python')
time.sleep(2)
