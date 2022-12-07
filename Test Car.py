#import libraries
#Manage selenium and navigate the page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#manipulate the data
import pandas as pd

#import custom code
import testTools_addItems as TT
import testTools_performShop as PS

#Import driver for the browser (Microsoft Edge)
driver = webdriver.Edge(
    r'C:\Users\Admin\Documents\2. Ingenieria en Sistemas\Cuatrimestre 3-2022\Calidad de Software\Seleium Codes\msedgedriver.exe'
)

actions = ActionChains(driver)

#Start the web page
try:
    driver.start_client()
    driver.maximize_window()
    driver.get('https://magento.softwaretestingboard.com/')
    print('Home page open')
except:
    print("Error opening the page")


try:
    #Add first item to the car
    TT.addSimpleItem(driver,'Fusion Backpack')

    #Move to another section and add second item
    TT.addSimpleItemNavigate(driver,'endeavor-daytrip-backpack','https://magento.softwaretestingboard.com/gear/bags.html')

    #Move to another section and add third item with more complex set up.
    TT.addComplexItemNavigate(
        driver = driver,
        itemName = 'layla-tee',
        quantity= 2,
        size = 'M',
        color = 'Blue',
        path= 'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html'
    )
except:
    print("Error adding items to the car")

try:
    #Open the shop screen
    PS.openCartScreen(driver)

    #Start completing the form information 
    Information = [{
        'customer-email':'rufo369@hotmail.es', #email address field
        'firstname':'Cristopher',
        'lastname':'Morales',
        'company':'Universidad Fidelitas',
        'street[0]':'Costa Rica, San José, Escazú',
        'city':'San José',
        'country_id': 'Costa Rica',
        'postcode':'2501',
        'telephone':'+50622284059',
        'region':'Escazú'

    }]

    PS.performShop(driver,Information)
    time.sleep(2)

    #Get final order confirmation
    time.sleep(5)
    finalConfirmation = driver.find_element("xpath","//div[@class='checkout-success']/p").get_attribute("innerHTML")
    print(finalConfirmation)
except:
    print("Error trying to complete final shopping form")

#End Code
driver.close()