import utilities.custom_logger as cl
import logging
from Base.basepage import BasePage
from Base.webdriverfactory import WebDriverFactory


class RegistrationCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wdf = WebDriverFactory(driver)
        # Locators
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "//a[contains(text(),'All Courses')]"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip = "postal"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"
    _enroll_error_message = "//div[@class='payment-error-box']//span[contains(text(),'The card was declined.')]"

    def searchBox(self, course):
        self.sendKeys(course, self._search_box)

    def selectCourse(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), locatorType="xpath")

    def selectEnrollCourse(self):
        self.elementClick(self._enroll_button)

    def cardNumber(self, num):
        if self.wdf.browser == "firefox":
            self.switchToFrame(name="__privateStripeFrame5")
            self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
            self.switchToDefaultContent()
        else:
            self.wdf.browser == "chrome"
            self.switchToFrame(name="__privateStripeFrame8")
            self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
            self.switchToDefaultContent()

    def cardExp(self, exp):
        if self.wdf.browser == "firefox":
            self.switchToFrame(name="__privateStripeFrame6")
            self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
            self.switchToDefaultContent()
        else:
            self.wdf.browser == "chrome"
            self.switchToFrame(name="__privateStripeFrame9")
            self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
            self.switchToDefaultContent()
    def cardCvv(self, cvv):
        if self.wdf.browser == "firefox":
            self.switchToFrame(name="__privateStripeFrame7")
            self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
            self.switchToDefaultContent()
        else:
            self.wdf.browser == "chrome"
            self.switchToFrame(name="__privateStripeFrame10")
            self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
            self.switchToDefaultContent()
    def enterZip(self, zip):
        if self.wdf.browser == "firefox":
            self.switchToFrame(name="__privateStripeFrame8")
            self.sendKeys(zip, locator=self._zip, locatorType="name")
            self.switchToDefaultContent()
        else:
            self.wdf.browser == "chrome"
            self.switchToFrame(name="__privateStripeFrame11")
            self.sendKeys(zip, locator=self._zip, locatorType="name")
            self.switchToDefaultContent()

    def agreeCheackBox(self):
        self.elementClick(locator=self._agree_to_terms_checkbox)

    def clickSubminEnroll(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def ccDetails(self, num="", exp="", ccv="", zip=""):
        self.cardNumber(num)
        self.cardExp(exp)
        self.cardCvv(ccv)
        self.enterZip(zip)

    def enrollCourse(self, num="", exp="", ccv="", zip=""):
        self.selectEnrollCourse()
        self.webScroll(direction="down")
        self.ccDetails(num, exp, ccv, zip)
        self.agreeCheackBox()
        #self.clickSubminEnroll()

    def verifyErrorMessage(self):
        messageElement = self.waitForElement(locator=self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="Enroll Button")
        return result

    def allCourses(self):
        self.moveInBrowser(move="back")
        self.elementClick(locator=self._all_courses,locatorType="xpath")





