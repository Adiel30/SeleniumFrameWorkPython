from Pages.courses.register_courses_page import RegistrationCoursesPage
from utilities.teststatus import CheckStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from Pages.navigate_pages import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistrationCoursesPage(self.driver)
        self.cs = CheckStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.moveBack()
        self.nav.navigateToAllCourses()


    @pytest.mark.run(order=1)
    @data(("Learn Python 3 from scratch", "1234 5678 9123 4567", "1121", "123", "12345"), ())
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv, zipCode):
        self.courses.searchBox(courseName)
        self.courses.selectCourse(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, ccv=ccCvv, zip=zipCode)
        verification = self.courses.verifyEnrollFailed()
        self.cs.markFinal(" Test invalid Enrollment ", verification, "Error Message Is Correct")
        #self.courses.allCourses()



