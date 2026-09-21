from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
driver.get("https://automationtesting.co.uk/actions.html")
driver.maximize_window()
time.sleep(2)
element = driver.find_element(By.ID, "doubClickStartText")
actions = ActionChains(driver)
actions.double_click(element).perform()
time.sleep(3)
source = driver.find_element(By.ID, "dragtarget")
target = driver.find_element(By.CLASS_NAME, "droptarget")
actions.drag_and_drop(source, target).perform()
time.sleep(3)
driver.quit()
