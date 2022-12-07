# ------------------- Import libreries -------------------
#Selenium web drivers
from re import search
from selenium import webdriver #Recognize the drowser
from selenium.webdriver.common.keys import Keys #Allows to use the common keyboard and mouse actions.
from selenium.webdriver.common.by import By #Helps to indentify the objects in the web page by class, name or other indicators. 

#Waits. 
import time

# ------------------- Driver call -------------------
driver = webdriver.Edge(
    r'msedgedriver.exe'
)

# ------------------- Start WebPage -------------------
driver.start_client()
driver.maximize_window()
driver.get('https://www.google.com/')


# ------------------- Navigate WebPage -------------------
#Select the search bar and look for a new search value
searchBar = driver.find_element(By.NAME,'q')
searchBar.send_keys("automates testing")
searchBar.send_keys(Keys.ENTER)

# ------------------- Final Output -------------------
time.sleep(3)
print("Instalation test successfully completed")

# ------------------- Driver clousure -------------------
driver.close()

