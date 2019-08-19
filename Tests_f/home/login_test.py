from selenium import webdriver
from Pages.home.login_page import LoginPage
import unittest
from utilities.teststatus import CheckStatus
# python3.7 -m pytest -s -v Tescs_f/home/login_test.py
import pytest
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTo(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        # lp = Login Page
        self.lp = LoginPage(self.driver)
        # cs = Test Status
        self.cs = CheckStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_ValidTest(self):
        self.lp.clearField()
        self.lp.login("adiel@newit.co.il", "abcabc")
        verification1 = self.lp.veriftTitle()
        self.cs.mark(verification1, "Title Is Correct")
        verification2 = self.lp.verifyLoginSuccessful()
        self.cs.markFinal("test_ValidTest", verification2, "You Have Successful Login")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("", "Usf")
        result = self.lp.verifyLoginFailed()
        assert result is True
