from Pages.courses.register_courses_page import RegistrationCoursesPage
from utilities.teststatus import CheckStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseCSVDataTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegistrationCoursesPage(self.driver)
        self.cs = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/adiellevy/PycharmProjects/FrameWorkAutomation/Testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv, zipCode):
        self.courses.searchBox(courseName)
        self.courses.selectCourse(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, ccv=ccCvv, zip=zipCode)
        verification = self.courses.verifyEnrollFailed()
        self.cs.markFinal(" Test invalid Enrollment ", verification, "Error Message Is Correct")
        self.courses.allCourses()



