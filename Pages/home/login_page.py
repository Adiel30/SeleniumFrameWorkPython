import utilities.custom_logger as cl
import logging
from Pages.navigate_pages import NavigationPage
from Base.basepage import BasePage
import time
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "//input[@value='Log In']"
    _logout_button = "//ul[@class='dropdown-menu']//a[@href='/sign_out']"

    def clickLogingLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def typeEmail(self, email):
        self.sendKeys(email, self._email_field)

    def typePassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLogingLink()
        self.typeEmail(email)
        self.typePassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@class='gravatar']",locatorType="xpath")

        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        return result

    def clearField(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def veriftTitle(self):
        return self.verifyPageTitle("Let's kode it")

    def logout(self):
        time.sleep(2)
        self.nav.navigateToUserSettings()
        time.sleep(3)
        logOutLinkElement = self.waitForElement(locator=self._logout_button, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logOutLinkElement)
        #self.elementClick(locator=self._logout_button, locatorType="xpath")
        #self.actionPrefum(locator=self._logout_button, locatorType="xpath")

