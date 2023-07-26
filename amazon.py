from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sleep = 2
product_to_search = "Galaxy S22"
minimum_value = 1000

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.amazon.com.br/')

# Searching for something
input_element_id = "twotabsearchtextbox"
search_input = driver.find_element_by_id(input_element_id)
desired_text = product_to_search
search_input.send_keys(desired_text)

button_id = "nav-search-submit-button"
search_button = driver.find_element_by_id(button_id)
search_button.click()


# Selecting the 'S10' with the lowest price
time.sleep(sleep)

## Find all elements with 'S10' in the URL and containing the price information
wait = WebDriverWait(driver, 10)
div_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='a-section a-spacing-base']//h2[contains(., 'Galaxy S22')]")))

# Initialize a list to store the extracted values
price_values = []

# Loop through the matching div elements to get price quotes only for the divs that have "Galaxy S10" in their h2 text
for div_element in div_elements:
    price_span = div_element.find_element(By.XPATH, ".//following::span[@class='a-price-whole'][1]")
    price_text = price_span.text.replace('.', '')
    price_values.append(int(price_text))
print(price_values)

# Get the lowest value that is higher than a minimum
filtered_values = [price for price in price_values if price > minimum_value]
lowest_value = min(filtered_values)
print(lowest_value)

# Determine the number of digits in the lowest_value
lowest_value = str(lowest_value)
num_digits = len(lowest_value)

# Format the lowest_value based on the number of digits
if num_digits > 3:
    adjusted_lowest_value = lowest_value[:-3] + "." + lowest_value[-3:]
else:
    adjusted_lowest_value = lowest_value

# Find the element containing the lowest value and click on it
element_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='a-price-whole' and contains(text(), '{adjusted_lowest_value}')]")))
element_to_click.click()

# If modal appears, close
# Wait for the modal to appear (if it's not there, it will timeout after 5 seconds)
time.sleep(sleep)
try:
    modal_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@id='attachSiNoCoverage-announce'][text()=' Não, obrigado(a) ']")))
    
    # Find the button element by its parent span
    button_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='attachSiNoCoverage-announce'][text()=' Não, obrigado(a) ']")))
    button_element.click()

except:
    pass

# Add to cart
time.sleep(sleep)
add_to_cart_button = WebDriverWait(driver, sleep).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
)
add_to_cart_button.click()

# Click to proceed to checkout
time.sleep(sleep)
proceed_to_checkout_button = WebDriverWait(driver, sleep).until(
    EC.element_to_be_clickable((By.NAME, "proceedToRetailCheckout"))
)
proceed_to_checkout_button.click()

# Exit page whem prompted for log-in, after all we don't want to buy it for real
time.sleep(sleep)
driver.close()