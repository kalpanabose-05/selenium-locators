from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.district.in/movies/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
# 1. Select location
location = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Gurugram']")
    )
)
location.click()
time.sleep(3)
# 2. Search Madurai
search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search city, area or locality']")
    )
)
search.send_keys("Madurai")
time.sleep(3)
# 3. Select Madurai
madurai = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@aria-label='Madurai']")
    )
)
madurai.click()
time.sleep(3)
# 4. Find Dorothy
dorothy = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h5[normalize-space()='Dorothy']")
    )
)
time.sleep(3)
# 5. Scroll down to Dorothy
driver.execute_script(
    "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
    dorothy
)
time.sleep(2)
# 6. Click Dorothy
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//h5[normalize-space()='Dorothy']")
    )
).click()
time.sleep(5)
driver.save_screenshot("dorothy_booking_page.png")

print("Screenshot taken successfully")
time.sleep(3)
# 7. Find Book Tickets on Dorothy page
book_tickets = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Book Tickets']")
    )
)
time.sleep(3)
# 8. Scroll to Book Tickets
driver.execute_script(
    "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
    book_tickets
)
time.sleep(2)
# 9. Click Book Tickets
book_tickets.click()
time.sleep(5)
#10.time
show_time = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[normalize-space()='03:50 PM']")
    )
)

show_time.click()
time.sleep(3)