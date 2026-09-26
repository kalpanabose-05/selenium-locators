import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")

# Maximize browser
driver.maximize_window()
time.sleep(3)

# Locate table
table = driver.find_element(By.TAG_NAME, "table")

time.sleep(3)
# Find row count
row_count = len(
    driver.find_elements(By.XPATH, "//table/tbody/tr")
)

time.sleep(3)
# Find column count
col_count = len(
    driver.find_elements(By.XPATH, "//table/thead/tr/th")
)

time.sleep(3)
# Print row and column count
print("Rows:", row_count)
print("Columns:", col_count)
time.sleep(3)

# Get all rows
rows = table.find_elements(
    By.XPATH, ".//tbody/tr"
)
time.sleep(3)

print("Total Rows:", len(rows))


# Loop through rows
for row in rows:

    cols = row.find_elements(
        By.TAG_NAME, "td"
    )

    for col in cols:
        print(col.text, "|", end=" ")

    print()
time.sleep(3)

# Close browser
driver.quit()