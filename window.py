from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")
driver.maximize_window()
time.sleep(3)
main_window = driver.current_window_handle
driver.find_element(By.XPATH, "//button[@title='New Tab']").click()
time.sleep(3)
windows = driver.window_handles
print("Number of windows:", len(windows))
for window in windows:
    if window != main_window:
        driver.switch_to.window(window)
        break
print("New tab title:", driver.title)
time.sleep(3)
search = driver.find_element(By.CLASS_NAME, "external-link").click()
time.sleep(3)
driver.quit()