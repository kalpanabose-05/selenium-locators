from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://testing.qaautomationlabs.com/file-download.php")
driver.maximize_window()
time.sleep(5)
# Enter text
wait = WebDriverWait(driver, 10)
text = driver.find_element(By.ID, "textInput")
text.send_keys("Hi, Hello Welcome To Innovel")
time.sleep(2)

# Click Generate button
generate = driver.find_element(
    By.XPATH,
    "/html/body/div/div[1]/section/div/div/div/div[2]/div/div/div/div/button"
)
generate.click()

# Wait for file generation
time.sleep(2)

# Click Download link
download = driver.find_element(By.XPATH, "//a[@id='downloadLink']")
download.click()

# Wait for download to complete
time.sleep(2)

# Download directory
download_dir = r"C:\Users\ELCOT\Downloads"

# Validate downloaded file
found = False

files = os.listdir(download_dir)

for file in files:
    if "myfile" in file:
        found = True
        break

# Print result
if found:
    print("Test Passed")
else:
    print("Test Failed")
time.sleep(3)
# Close browser
driver.quit()