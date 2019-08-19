import unittest
from Tests_f.home.login_test import LoginTo
from Tests_f.courses.register_courses_csv_data import RegisterCourseCSVDataTest

# Get all Test

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseCSVDataTest)

# Create Test Suite Combining All Test Classes

smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

