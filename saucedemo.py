from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sleep = 2

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.saucedemo.com/')

# Logging in
time.sleep(sleep)
username_input = driver.find_element(By.ID, "user-name")
desired_username = "standard_user"
username_input.send_keys(desired_username)

password_input = driver.find_element(By.ID, "password")
desired_password = "secret_sauce"
password_input.send_keys(desired_password)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()


# Adding specific item to cart
time.sleep(sleep)
item_name = "Sauce Labs Backpack"  # Replace with the name of the item you want to add to cart
xpath_expression = f"//div[contains(@class, 'inventory_item_name') and contains(text(), '{item_name}')]"

wait = WebDriverWait(driver, 5)
add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))

add_to_cart_button = driver.find_element_by_xpath(xpath_expression)
add_to_cart_button.click()


# Confirming item addition to cart
time.sleep(sleep)
button_id = "add-to-cart-sauce-labs-backpack"
add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, button_id)))
add_to_cart_button.click()

# Clicking on the cart link to purchase
time.sleep(sleep)
cart_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopping_cart_container")))
cart_link = cart_container.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_link.click()

# Clicking on checkout
time.sleep(sleep)
button_id = "checkout"
checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, button_id)))
checkout_button.click()

# Adding personal information
time.sleep(sleep)

firstname_input = driver.find_element(By.ID, "first-name")
desired_fname = "Mister"
firstname_input.send_keys(desired_fname)

lastname_input = driver.find_element(By.ID, "last-name")
desired_lname = "Tester"
lastname_input.send_keys(desired_lname)

zip_input = driver.find_element(By.ID, "postal-code")
desired_zip = "Tester"
zip_input.send_keys(desired_zip)

login_button = driver.find_element(By.ID, "continue")
login_button.click()

# Completing
time.sleep(sleep)
login_button = driver.find_element(By.ID, "finish")
login_button.click()