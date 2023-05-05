from Config.config import TestData
from Pages.signUp import SignUp
from Test.test_Base import BaseTest

class TestSignup(BaseTest):
    def test_signup(self):
        self.signupPage=SignUp(self.driver)
        self.signupPage.signup(TestData.EMAIL,TestData.FIRST_NAME,TestData.LAST_NAME,TestData.PASSWORD,TestData.CONFIRM_PASS)