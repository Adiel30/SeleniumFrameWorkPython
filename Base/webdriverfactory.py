import traceback
from selenium import webdriver
import os
from selenium.webdriver import ActionChains
class WebDriverFactory():
    def __init__(self, browser):

        """
        Inits WebDriverFactory Class

        Returns: None
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

         Returns WebDriver Instance
        """
        myurl = "https://letskodeit.teachable.com/"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driverChrome = '/Users/adiellevy/Geko/chromedriver'
            os.environ["webdriver.chrome.driver"] = driverChrome
            driver = webdriver.Chrome()
            driver.set_window_size(1440,900)
        elif self.browser == "ie":
            # Set Iexplrer driver
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()
        # Set Implicit wait for element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        # Loading the URL
        driver.get(myurl)
        return driver



