from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


import time

# initialize the Chrome driver
driver = webdriver.Edge(
    r'C:\Users\Admin\Documents\2. Ingenieria en Sistemas\Cuatrimestre 3-2022\Calidad de Software\Seleium Codes\msedgedriver.exe'
)

# Luma credentials
username = "zunigabenja1@gmail.com"
password = "ABCabc123"

# head to the luma login page
driver.start_client()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")

# find username/email field and send the username itself to the input field
driver.find_element(By.ID,'email').send_keys(username)

# find password input field and insert password as well
driver.find_element(By.ID,'pass').send_keys(password)

# click login button
driver.find_element(By.NAME,'send').click()

time.sleep(5)

driver.close()