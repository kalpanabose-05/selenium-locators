from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/alertsdemo.html#google_vignette")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, "confirmBox").click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()
time.sleep(3)
driver.quit()