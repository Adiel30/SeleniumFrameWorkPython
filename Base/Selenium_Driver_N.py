from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

"""

  This Class include all the locator type supported in python 

  for using import the module "SeleniumDriver"

  """




class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("*" * 40)
            print("\nLocator type " + locatorType + " \nnot correct/supported")
        return False

    """
    This Method Use Get The Element Your Provide And Search It By 
    The Locator that provide in the "getByType" method 
    This Method Just Search The Element And Check if it exist  
    After the Check the element Return
    """

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("*" * 40)
            print("\nElement Found with locator: " + locator + " \nand locatorType: " + locatorType)
        except:
            print("*" * 40)
            print("\nElement not found with locator: " + locator + " \nand locatorType: " + locatorType)
        return element

    """
    This Method Use The Element And The Locator Type That Check in the  "getElement" Method
    And "Click on it"
    """

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("*" * 40)
            print("\nClicked on element with locator: " + locator + " \nlocatorType: " + locatorType)
        except:
            print("*" * 40)
            print("\nCannot click on the element with locator: " + locator + " \nlocatorType: " + locatorType)
            print_stack()

    """
    This Method Use The Element And The Locator Type That Check in the  "getElement" Method
    And "Send A Key"
    """
    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("*" * 40)
            print("\nSent data on element with locator: " + locator + " \nlocatorType: " + locatorType)
        except:
            print("*" * 40)
            print("\nCannot Sent data on the element with locator: " + locator + " \nlocatorType: " + locatorType)
            print_stack()

    """
    Take Element And locatorType If There Is A  Value
    """

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("*" * 40)
                print("\nElement Found")
                return True
            else:
                print("*" * 40)
                print("\nElement not found")
                return False
        except:
            print("*" * 40)

            print("\nElement not found")
            return False

    """
    Take List Of Element And locatorType If There Is A  Value
    """
    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("*" * 40)
                print("\nElement Found")
                return True
            else:
                print("*" * 40)
                print("\nElement not found")
                return False
        except:
            print("*" * 40)
            print("\nElement not found")
            return False

    """
    wait for an element to be click able 
    """
    print("*" * 40)
    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            print("*" * 40)
            byType = self.getByType(locatorType)
            print("*" * 40)
            print("\nWaiting for maximum :: " + str(timeout) +
                  " \n:: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            print("*" * 40)
            print("\nElement appeared on the web page\n")
        except:
            print("*" * 40)
            print("\nElement not appeared on the web page\n")
            print("*" * 40)
            print_stack()
        return element