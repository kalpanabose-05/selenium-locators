from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Alert']").click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert Message:", alert.text)
time.sleep(3)
alert.accept()
time.sleep(3)
driver.quit()