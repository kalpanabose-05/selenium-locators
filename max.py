from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Edge
driver = webdriver.Edge()

# Open Purplle
driver.get("https://www.maxfashion.in/in/en/")
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 20)

time.sleep(5)

# Search box
search_box  = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "js-site-search-input")
    )
)
time.sleep(2)
search_box .send_keys("TShirts For Women")
search_box .send_keys(Keys.ENTER)
time.sleep(5)
# Locate all products using find_elements()
# Wait for product containers
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.product")
    )
)

products = driver.find_elements(By.CSS_SELECTOR, "div.product")

print("Total products:", len(products))

if len(products) >= 5:
    print("1.", products[0].find_element(By.TAG_NAME, "img").get_attribute("alt"))
    print("2.", products[1].find_element(By.TAG_NAME, "img").get_attribute("alt"))
    print("3.", products[2].find_element(By.TAG_NAME, "img").get_attribute("alt"))
    print("4.", products[3].find_element(By.TAG_NAME, "img").get_attribute("alt"))
    print("5.", products[4].find_element(By.TAG_NAME, "img").get_attribute("alt"))
else:
    print("Products are not loaded. Check the website page.")
time.sleep(5)
#product page
top=wait.until(
    EC.visibility_of_element_located(
        (By.ID, "product-1000016760618-OffWhite-IVORY")
    )
)
top.click()
print("product:", driver.title)

time.sleep(5)
# Switch to product tab if opened in a new tab
wait.until(lambda d: len(d.window_handles) > 1)

driver.switch_to.window(driver.window_handles[-1])

# Wait for product details
time.sleep(3)

# Print product name
print("Product Name:", driver.title)

# Print product price
price = driver.find_elements(
    By.CSS_SELECTOR, "[class*='price']"
)

if price:
    print("Product Price:", price[0].text)
else:
    print("Price locator needs to be inspected.")

# Find multiple available sizes
sizes = driver.find_elements(By.CSS_SELECTOR, ".jss576")

print("Available Sizes:")

if sizes:
    print(sizes[0].text)
    if len(sizes) > 1:
        print(sizes[1].text)
    if len(sizes) > 2:
        print(sizes[2].text)
    if len(sizes) > 3:
        print(sizes[3].text)
    if len(sizes) > 4:
        print(sizes[4].text)
    if len(sizes) > 5:
        print(sizes[5].text)
else:
    print("Sizes not found.")

time.sleep(3)
xs = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-code='1000016760627']")
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    xs
)

driver.execute_script(
    "arguments[0].click();",
    xs
)
time.sleep(6)
# Click ADD TO BASKET
basket = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[normalize-space()='ADD TO BASKET']]")
    )
)
basket.click()

print("Product added to basket")
time.sleep(3)
driver.quit()



