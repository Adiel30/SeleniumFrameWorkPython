from Pages.courses.register_courses_page import RegistrationCoursesPage
from utilities.teststatus import CheckStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistrationCoursesPage(self.driver)
        self.cs = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.searchBox("python")
        self.courses.selectCourse("Learn Python 3 from scratch")
        self.courses.enrollCourse(num="1234 5678 9123 4567", exp="1121", ccv="123", zip="12345")
        verification = self.courses.verifyEnrollFailed()
        self.cs.markFinal(" Test invalid Enrollment ", verification, "Error Message Is Correct")


