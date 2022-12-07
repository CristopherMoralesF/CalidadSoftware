import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def openCartScreen(driver):
    carIcon = driver.find_element(By.CLASS_NAME,'counter-number')
    carIcon.click()

    checkOutBtn = driver.find_element(By.ID,'top-cart-btn-checkout')
    checkOutBtn.click()
    print('Open Shopping Car Window')


def performShop(driver,Information):

    #List of the fields to find by ID not Name
    listId = ['customer-email']
    

    #Declare actions package
    actions = ActionChains(driver)

    #Convert the set up in a data frame
    df_Information = pd.DataFrame(Information)

    time.sleep(3)

    #Complete the form information
    print('Start completing form information')
    for column in df_Information.columns:

        #Select the field
        if column in listId:
            field = driver.find_element(By.ID,column)
        else:
            field = driver.find_element(By.NAME,column)

        #Complete the information
        actions.move_to_element(field).perform()
        field.click()
        field.send_keys(Information[0][column])
        print('Field:' + column + ' ready')


    #Select the shipping Method
    time.sleep(3)
    ShippingOption = driver.find_element("xpath","//input[@type = 'radio']")
    actions.move_to_element(ShippingOption).perform


    if ShippingOption.is_selected() == False:
        ShippingOption.click()

    #Click the next option
    NextBtn = driver.find_element("xpath", "//button[@class = 'button action continue primary']")
    actions.move_to_element(NextBtn).perform()
    NextBtn.click()
    print("Form completed")

    #Wait for confirmation page and place order
    time.sleep(3)
    PlaceOrderBtn = driver.find_element("xpath","//button[@class='action primary checkout']")
    actions.move_to_element(PlaceOrderBtn).perform()
    PlaceOrderBtn.click()
