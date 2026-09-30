from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/login.php")
driver.maximize_window()
time.sleep(3)
textbox = driver.find_element(By.ID, "email")

driver.execute_script(
    "arguments[0].value='Anusathya';",
    textbox
)
time.sleep(5)
driver.quit()
