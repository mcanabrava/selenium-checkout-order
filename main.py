from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.saucedemo.com/')


driver.close()