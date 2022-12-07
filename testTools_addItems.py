from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def addSimpleItem(driver,itemName):
    
    #Find the item in the web page
    productXpath = "//a[@title='" + itemName + "']"
    product = driver.find_element("xpath", productXpath)
    print('Item ' + itemName + 'found')

    #Hove the select element and click the link to open the car windown. 
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    product.click()
    print('Add to the car windown open')

    #Add the item to the car
    addButton = driver.find_element(By.ID,'product-addtocart-button')
    addButton.click()
    print('Item added to the car')

    #Wait some time to perform the final validation
    time.sleep(3)

    #Check the number of items in the car.
    itemsCount = driver.find_element(By.CLASS_NAME,'counter-number').get_attribute('innerHTML')
    print('Total items in the car: ' + str(itemsCount))

def addSimpleItemNavigate(driver,itemName,path):

    #Navigate to the selected item:
    driver.get(path)
    
    #Find the item in the web page
    productXpath = "//a[@href='https://magento.softwaretestingboard.com/" + itemName + ".html']"
    product = driver.find_element("xpath", productXpath)
    print('Item ' + itemName + ' found')

    #Hove the select element and click the link to open the car windown. 
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    product.click()
    print('Add to the car windown open')

    #Add the item to the car
    addButton = driver.find_element(By.ID,'product-addtocart-button')
    addButton.click()
    print('Item added to the car')

    #Wait some time to perform the final validation
    time.sleep(3)

    #Check the number of items in the car.
    itemsCount = driver.find_element(By.CLASS_NAME,'counter-number').get_attribute('innerHTML')
    print('Total items in the car: ' + str(itemsCount))

def addComplexItemNavigate(driver,itemName,quantity,size,color,path):

    #Navigate to the selected item:
    driver.get(path)
    
    #Find the item in the web page
    productXpath = "//a[@href='https://magento.softwaretestingboard.com/" + itemName + ".html']"
    product = driver.find_element("xpath", productXpath)
    print('Item ' + itemName + ' found')

    #Hove the select element and click the link to open the car windown. 
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    product.click()
    print('Add to the car windown open')

    time.sleep(5)

    #Select the Size
    productSizeXpath = "//div[@aria-label='" + size + "']"
    productSize = driver.find_element("xpath", productSizeXpath)
    productSize.click()

    #Select the Color
    productSizeXpath = "//div[@aria-label='" + color + "']"
    productSize = driver.find_element("xpath", productSizeXpath)
    productSize.click()
    

    #Select the quantity
    productQuantityXpath = "//input[@title='Qty']"
    productQuantity = driver.find_element("xpath", productQuantityXpath)
    productQuantity.clear()
    productQuantity.send_keys(quantity)


    #Add the item
    addButton = driver.find_element(By.ID,'product-addtocart-button')
    addButton.click()
    print('Item added to the car')

    #Wait some time to perform the final validation
    time.sleep(3)

    #Check the number of items in the car.
    itemsCount = driver.find_element(By.CLASS_NAME,'counter-number').get_attribute('innerHTML')
    print('Total items in the car: ' + str(itemsCount))

    