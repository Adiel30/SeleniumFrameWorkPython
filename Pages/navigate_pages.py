import utilities.custom_logger as cl
import logging
from Base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    _my_courses = "My courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    #_user_settings_icon = "//div[@class='gravatar']//li[@class='dropdown']"
    _user_settings_icon = "//img[@class='gravatar']"

    def moveForward(self):
        self.moveInBrowser(move="forward")

    def moveBack(self):
        self.moveInBrowser(move="back")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon,
                                      locatorType="xpath")